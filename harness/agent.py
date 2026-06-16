#!/usr/bin/env python3
"""MiniMax M3 agentic test harness.

A minimal but real tool-using agent loop, built to *test* MiniMax M3 against the
rules in this repo. It loads the repo's always-on rules as the system prompt, so
you exercise the model AND the rules together, and it instruments the failure
modes that matter for open-weight models:

  - endless loops        -> repeated-tool-call detection + hard step cap
  - context "holes"      -> every tool result is logged so you can see what the
                            model actually had vs. what it acted on
  - hit-or-miss coding   -> full transcript saved for diffing across runs

Access path: OpenAI-compatible endpoint (https://api.minimax.io/v1), model
"MiniMax-M3". The official docs also expose an Anthropic-compatible path; this
harness uses the OpenAI one because tool-calling is the most portable there.

Usage:
    export MINIMAX_API_KEY=sk-...            # or put it in harness/.env
    python harness/agent.py "Create a Python script that prints the first 20 primes and run it"

    python harness/agent.py --task-file task.txt --max-steps 25
    python harness/agent.py --no-rules "..."          # test the bare model
    python harness/agent.py --rules fable5-coding-craft "..."  # add a requestable rule
    python harness/agent.py --list-rules
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
RULES_DIR = REPO_ROOT / ".cursor" / "rules"
ALWAYS_ON = ["minimax-m3-core", "minimax-m3-status-verification"]

DEFAULT_MODEL = "MiniMax-M3"
DEFAULT_BASE_URL = "https://api.minimax.io/v1"

# Commands we refuse to run even in a sandbox. This is a guard, not a security
# boundary -- treat the workdir as disposable.
DESTRUCTIVE = re.compile(
    r"(rm\s+-rf\s+/(?!\w)|mkfs|:\(\)\s*\{|dd\s+if=|>\s*/dev/sd|sudo\b|shutdown|reboot|"
    r"chmod\s+-R\s+777\s+/|chown\s+-R\s+\S+\s+/(?!\w))",
    re.IGNORECASE,
)


# --------------------------------------------------------------------------- #
# Colours / logging
# --------------------------------------------------------------------------- #
class C:
    DIM = "\033[2m"
    BOLD = "\033[1m"
    RESET = "\033[0m"
    BLUE = "\033[34m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    RED = "\033[31m"
    CYAN = "\033[36m"
    MAGENTA = "\033[35m"


# Secret values (e.g. the API key) to scrub from anything we log, send to the
# model, or persist. Populated in main(). The model never needs these.
SECRETS: list[str] = []


def redact(text: str | None) -> str:
    if not text:
        return text or ""
    for secret in SECRETS:
        if secret and len(secret) >= 8:
            text = text.replace(secret, "***REDACTED***")
    return text


def clamp(text: str, limit: int) -> str:
    if len(text) <= limit:
        return text
    return (
        text[:limit]
        + f"\n... [harness truncated {len(text) - limit} chars; narrow your "
        "command/output instead of dumping large results]"
    )


def log(tag: str, msg: str, color: str = "") -> None:
    print(f"{color}{C.BOLD}[{tag}]{C.RESET} {color}{redact(msg)}{C.RESET}")


def truncate(text: str, limit: int = 1600) -> str:
    if len(text) <= limit:
        return text
    head = text[: limit // 2]
    tail = text[-limit // 2 :]
    return f"{head}\n{C.DIM}... [{len(text) - limit} chars elided] ...{C.RESET}\n{tail}"


# --------------------------------------------------------------------------- #
# System prompt assembly
# --------------------------------------------------------------------------- #
def strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            nl = text.find("\n", end + 1)
            return text[nl + 1 :] if nl != -1 else ""
    return text


def load_rule(name: str) -> str | None:
    path = RULES_DIR / f"{name}.mdc"
    if not path.exists():
        return None
    return strip_frontmatter(path.read_text(encoding="utf-8")).strip()


def list_rules() -> list[str]:
    if not RULES_DIR.exists():
        return []
    return sorted(p.stem for p in RULES_DIR.glob("*.mdc"))


HARNESS_CONTRACT = """\
# Harness Operating Contract

You are running inside a minimal autonomous agent loop with real tools. There is
no human to answer mid-task questions, so make reasonable decisions and proceed.

Tools available: read_file, write_file, list_dir, run_shell, finish.

- All file and shell operations are confined to the working directory shown below.
- Prove your work by running it (run_shell), not by asserting it. Bug fixes must
  be red -> green.
- When the task is genuinely complete and verified, call `finish` with a short
  evidence-backed summary. Do not call `finish` with unverified work.
- Do not repeat an identical tool call hoping for a different result. If a step
  failed twice, change strategy.
"""


def build_system_prompt(use_rules: bool, extra_rules: list[str], workdir: Path) -> str:
    parts: list[str] = []
    if use_rules:
        for name in ALWAYS_ON:
            body = load_rule(name)
            if body:
                parts.append(body)
            else:
                log("WARN", f"always-on rule not found: {name}", C.YELLOW)
        for name in extra_rules:
            body = load_rule(name)
            if body:
                parts.append(body)
            else:
                log("WARN", f"requested rule not found: {name}", C.YELLOW)
    parts.append(HARNESS_CONTRACT + f"\nWorking directory: {workdir}\n")
    return "\n\n---\n\n".join(parts)


# --------------------------------------------------------------------------- #
# Tools
# --------------------------------------------------------------------------- #
TOOL_SCHEMA = [
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read a UTF-8 text file relative to the working directory.",
            "parameters": {
                "type": "object",
                "properties": {"path": {"type": "string"}},
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": "Create or overwrite a UTF-8 text file relative to the working directory.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string"},
                    "content": {"type": "string"},
                },
                "required": ["path", "content"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "list_dir",
            "description": "List entries in a directory relative to the working directory.",
            "parameters": {
                "type": "object",
                "properties": {"path": {"type": "string", "default": "."}},
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "run_shell",
            "description": "Run a shell command in the working directory and return stdout/stderr/exit code.",
            "parameters": {
                "type": "object",
                "properties": {"command": {"type": "string"}},
                "required": ["command"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "finish",
            "description": "Declare the task complete. Provide an evidence-backed summary of what was done and verified.",
            "parameters": {
                "type": "object",
                "properties": {"summary": {"type": "string"}},
                "required": ["summary"],
            },
        },
    },
]


@dataclass
class Tools:
    workdir: Path
    allow_shell: bool = True
    shell_timeout: int = 120

    def _resolve(self, rel: str) -> Path:
        target = (self.workdir / rel).resolve()
        if self.workdir not in target.parents and target != self.workdir:
            raise ValueError(f"path escapes working directory: {rel}")
        return target

    def read_file(self, path: str) -> str:
        p = self._resolve(path)
        if not p.exists():
            return f"ERROR: no such file: {path}"
        return p.read_text(encoding="utf-8", errors="replace")

    def write_file(self, path: str, content: str) -> str:
        p = self._resolve(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
        return f"wrote {len(content)} chars to {path}"

    def list_dir(self, path: str = ".") -> str:
        p = self._resolve(path)
        if not p.exists():
            return f"ERROR: no such directory: {path}"
        entries = sorted(
            f"{e.name}/" if e.is_dir() else e.name for e in p.iterdir()
        )
        return "\n".join(entries) if entries else "(empty)"

    def run_shell(self, command: str) -> str:
        if not self.allow_shell:
            return "ERROR: shell is disabled (run without --no-shell to enable)"
        if DESTRUCTIVE.search(command):
            return "ERROR: refused (matched destructive-command guard)"
        try:
            proc = subprocess.run(
                command,
                shell=True,
                cwd=self.workdir,
                capture_output=True,
                text=True,
                timeout=self.shell_timeout,
            )
        except subprocess.TimeoutExpired:
            return f"ERROR: timed out after {self.shell_timeout}s"
        out = proc.stdout or ""
        err = proc.stderr or ""
        return f"exit_code={proc.returncode}\n--- stdout ---\n{out}\n--- stderr ---\n{err}"

    def dispatch(self, name: str, args: dict) -> str:
        fn = getattr(self, name, None)
        if fn is None:
            return f"ERROR: unknown tool {name}"
        try:
            return fn(**args)
        except TypeError as e:
            return f"ERROR: bad arguments for {name}: {e}"
        except Exception as e:  # surface tool errors to the model, don't crash the loop
            return f"ERROR: {type(e).__name__}: {e}"


# --------------------------------------------------------------------------- #
# Agent loop
# --------------------------------------------------------------------------- #
@dataclass
class RunStats:
    steps: int = 0
    prompt_tokens: int = 0
    completion_tokens: int = 0
    tool_calls: int = 0
    repeated_calls: int = 0
    finished: bool = False
    finish_summary: str = ""
    transcript: list = field(default_factory=list)


def call_signature(name: str, args: dict) -> str:
    return name + "::" + json.dumps(args, sort_keys=True, ensure_ascii=False)


def run_agent(
    client,
    model: str,
    system_prompt: str,
    task: str,
    tools: Tools,
    max_steps: int,
    loop_threshold: int,
    temperature: float,
    max_tool_output: int,
) -> RunStats:
    from openai import OpenAI  # noqa: F401  (imported for type clarity)

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": task},
    ]
    stats = RunStats()
    sig_counts: dict[str, int] = {}

    for step in range(1, max_steps + 1):
        stats.steps = step
        log("STEP", f"{step}/{max_steps}", C.MAGENTA)
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=messages,
                tools=TOOL_SCHEMA,
                tool_choice="auto",
                temperature=temperature,
            )
        except Exception as e:
            log("API-ERROR", f"{type(e).__name__}: {e}", C.RED)
            stats.finish_summary = f"API error: {e}"
            return stats

        if getattr(resp, "usage", None):
            stats.prompt_tokens += resp.usage.prompt_tokens or 0
            stats.completion_tokens += resp.usage.completion_tokens or 0

        msg = resp.choices[0].message

        reasoning = getattr(msg, "reasoning_content", None)
        if reasoning:
            log("THINK", truncate(reasoning, 1200), C.DIM)

        if msg.content:
            log("ASSISTANT", truncate(msg.content), C.CYAN)

        assistant_entry: dict = {"role": "assistant", "content": msg.content or ""}
        if msg.tool_calls:
            assistant_entry["tool_calls"] = [
                {
                    "id": tc.id,
                    "type": "function",
                    "function": {
                        "name": tc.function.name,
                        "arguments": tc.function.arguments,
                    },
                }
                for tc in msg.tool_calls
            ]
        messages.append(assistant_entry)
        stats.transcript.append(assistant_entry)

        if not msg.tool_calls:
            # Model answered with no tool call -> treat as completion.
            stats.finish_summary = msg.content or "(no content)"
            log("DONE", "model ended without a tool call", C.GREEN)
            return stats

        for tc in msg.tool_calls:
            name = tc.function.name
            try:
                args = json.loads(tc.function.arguments or "{}")
            except json.JSONDecodeError:
                args = {}
                result = f"ERROR: could not parse arguments: {tc.function.arguments!r}"
                log("TOOL", f"{name} -> arg parse error", C.RED)
                messages.append(
                    {"role": "tool", "tool_call_id": tc.id, "content": result}
                )
                stats.transcript.append(
                    {"role": "tool", "name": name, "content": result}
                )
                continue

            stats.tool_calls += 1
            sig = call_signature(name, args)
            sig_counts[sig] = sig_counts.get(sig, 0) + 1

            if name == "finish":
                stats.finished = True
                stats.finish_summary = args.get("summary", "")
                log("FINISH", truncate(stats.finish_summary), C.GREEN)
                return stats

            preview = json.dumps(args, ensure_ascii=False)
            log("TOOL", f"{name}({truncate(preview, 300)})", C.BLUE)

            if sig_counts[sig] >= loop_threshold:
                stats.repeated_calls += 1
                nudge = (
                    f"LOOP GUARD: you have called {name} with identical arguments "
                    f"{sig_counts[sig]} times. This is not making progress. Stop "
                    f"repeating it. Either change your approach, inspect different "
                    f"state, or call finish if you are blocked."
                )
                log("LOOP-GUARD", f"{name} repeated {sig_counts[sig]}x -> nudging", C.YELLOW)
                messages.append(
                    {"role": "tool", "tool_call_id": tc.id, "content": nudge}
                )
                stats.transcript.append(
                    {"role": "tool", "name": name, "content": nudge}
                )
                continue

            result = clamp(redact(tools.dispatch(name, args)), max_tool_output)
            log("RESULT", truncate(result), C.DIM)
            messages.append(
                {"role": "tool", "tool_call_id": tc.id, "content": result}
            )
            stats.transcript.append({"role": "tool", "name": name, "content": result})

    log("CAP", f"hit max_steps={max_steps} without finishing", C.YELLOW)
    return stats


# --------------------------------------------------------------------------- #
# Entry point
# --------------------------------------------------------------------------- #
def load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        os.environ.setdefault(key.strip(), val.strip().strip("'\""))


def main() -> int:
    parser = argparse.ArgumentParser(description="MiniMax M3 agentic test harness")
    parser.add_argument("task", nargs="?", help="task description for the agent")
    parser.add_argument("--task-file", help="read the task from a file instead")
    parser.add_argument("--model", default=os.environ.get("MINIMAX_MODEL", DEFAULT_MODEL))
    parser.add_argument("--base-url", default=os.environ.get("MINIMAX_BASE_URL", DEFAULT_BASE_URL))
    parser.add_argument("--max-steps", type=int, default=20)
    parser.add_argument("--loop-threshold", type=int, default=3,
                        help="identical tool calls before the loop guard fires")
    parser.add_argument("--max-tool-output", type=int, default=8000,
                        help="max chars of a tool result fed back to the model")
    parser.add_argument("--temperature", type=float, default=1.0)
    parser.add_argument("--workdir", default=str(Path(__file__).resolve().parent / "workspace"))
    parser.add_argument("--no-rules", action="store_true", help="omit repo rules (test bare model)")
    parser.add_argument("--rules", default="", help="comma-separated requestable rules to also load")
    parser.add_argument("--no-shell", action="store_true", help="disable the run_shell tool")
    parser.add_argument("--list-rules", action="store_true", help="print available rules and exit")
    args = parser.parse_args()

    load_dotenv(Path(__file__).resolve().parent / ".env")

    if args.list_rules:
        for name in list_rules():
            marker = " (always-on)" if name in ALWAYS_ON else ""
            print(f"  {name}{marker}")
        return 0

    if args.task_file:
        task = Path(args.task_file).read_text(encoding="utf-8")
    elif args.task:
        task = args.task
    else:
        parser.error("provide a task (positional) or --task-file")

    api_key = os.environ.get("MINIMAX_API_KEY")
    if not api_key:
        log("ERROR", "MINIMAX_API_KEY is not set (export it or add harness/.env)", C.RED)
        return 2
    SECRETS.append(api_key)

    try:
        from openai import OpenAI
    except ImportError:
        log("ERROR", "openai SDK not installed -> pip install -r harness/requirements.txt", C.RED)
        return 2

    workdir = Path(args.workdir).resolve()
    workdir.mkdir(parents=True, exist_ok=True)

    extra_rules = [r.strip() for r in args.rules.split(",") if r.strip()]
    system_prompt = build_system_prompt(not args.no_rules, extra_rules, workdir)

    log("CONFIG", f"model={args.model} base={args.base_url}", C.BOLD)
    log("CONFIG", f"workdir={workdir}", C.BOLD)
    log("CONFIG", f"rules={'off' if args.no_rules else ['core'] + extra_rules} "
                  f"shell={'off' if args.no_shell else 'on'} "
                  f"system_prompt_chars={len(system_prompt)}", C.BOLD)
    log("TASK", task.strip(), C.BOLD)

    client = OpenAI(api_key=api_key, base_url=args.base_url)
    tools = Tools(workdir=workdir, allow_shell=not args.no_shell)

    t0 = time.time()
    stats = run_agent(
        client=client,
        model=args.model,
        system_prompt=system_prompt,
        task=task,
        tools=tools,
        max_steps=args.max_steps,
        loop_threshold=args.loop_threshold,
        temperature=args.temperature,
        max_tool_output=args.max_tool_output,
    )
    elapsed = time.time() - t0

    transcript_path = workdir / "transcript.json"
    transcript_path.write_text(
        redact(json.dumps(
            {
                "task": task,
                "model": args.model,
                "stats": {
                    "steps": stats.steps,
                    "tool_calls": stats.tool_calls,
                    "repeated_calls": stats.repeated_calls,
                    "prompt_tokens": stats.prompt_tokens,
                    "completion_tokens": stats.completion_tokens,
                    "finished": stats.finished,
                    "elapsed_s": round(elapsed, 1),
                },
                "messages": stats.transcript,
            },
            indent=2,
            ensure_ascii=False,
        )),
        encoding="utf-8",
    )

    print()
    log("SUMMARY", "", C.BOLD)
    print(f"  finished cleanly : {stats.finished}")
    print(f"  steps            : {stats.steps}/{args.max_steps}")
    print(f"  tool calls       : {stats.tool_calls}  (repeated/looped: {stats.repeated_calls})")
    print(f"  tokens           : {stats.prompt_tokens} in / {stats.completion_tokens} out")
    print(f"  elapsed          : {elapsed:.1f}s")
    print(f"  transcript       : {transcript_path}")
    if stats.finish_summary:
        print(f"\n{C.GREEN}{redact(stats.finish_summary)}{C.RESET}")
    return 0 if stats.finished else 1


if __name__ == "__main__":
    sys.exit(main())
