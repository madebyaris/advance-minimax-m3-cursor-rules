# Harness — evaluate the rules against a real model

A minimal, tool-using agent loop for putting **MiniMax M3** (or any OpenAI-compatible
model) through real work *with these rules loaded as its system prompt*. It exists so
the claims in the root README are reproducible: run a task, watch the agent inspect →
act → verify, read the transcript.

This is an evaluation tool, not production code. It is intentionally small.

---

## What it does

- Loads the repo's **always-on rules** (`minimax-m3-core`, `minimax-m3-status-verification`)
  as the system prompt — or runs bare with `--no-rules` to A/B the difference.
- Gives the model five tools: `read_file`, `write_file`, `list_dir`, `run_shell`, `finish`.
- Confines all file/shell actions to a working directory (a sandbox you point it at).
- Logs every step and writes a redacted `transcript.json`.
- Detects identical repeated tool calls (a loop guard) and caps tool-output size so a
  huge command can't blow up the context.

---

## Setup

```bash
cd harness
python3 -m venv .venv
./.venv/bin/pip install -r requirements.txt
cp .env.example .env          # then edit .env and set MINIMAX_API_KEY
```

`harness/.env` is gitignored. The key is scrubbed from logs and transcripts.

---

## Run an agentic task

Point it at a working directory (which can contain a project to fix) and give it a task
in plain words:

```bash
./.venv/bin/python agent.py "fix the failing test in calc.py" --workdir ./workspace
```

Useful flags:

| Flag | Purpose |
|---|---|
| `--workdir PATH` | Sandbox the agent works in (default `harness/workspace`). |
| `--no-rules` | Run the bare model with no repo rules (for A/B comparisons). |
| `--rules a,b` | Also load named requestable rules (e.g. `--rules fable5-coding-craft`). |
| `--max-steps N` | Cap the agent loop (default 20). |
| `--max-tool-output N` | Max chars of a tool result fed back to the model (default 8000). |
| `--no-shell` | Disable `run_shell`. |
| `--list-rules` | Print available rules and exit. |
| `--model` / `--base-url` | Override the model or endpoint. |

The run writes `<workdir>/transcript.json` and prints a summary (steps, tool calls,
looped calls, tokens, elapsed).

---

## Q&A tests (no tools, no code)

Two scripts probe the model in pure-answer mode, with the rules loaded:

```bash
./.venv/bin/python quiz.py          # knowledge test (devops, harness, FDE, MCP, ...)
./.venv/bin/python intent_test.py   # can it read intent from vague non-dev prompts?
```

Each writes a redacted `*-transcript.json` with the questions, answers, and token counts.

---

## Seeds

`seeds/` holds small, self-contained tasks used to measure consistency. Each pairs a
**visible** spec/test with a **hidden** grader the model never sees, so a pass means it
generalized rather than overfit the example:

- `seeds/calc/` — a buggy integer expression evaluator (precedence, truncating division, unary minus)
- `seeds/roman/` — Swift: Roman-numeral conversion with subtractive notation
- `seeds/tally/` — Swift: a data-race fixed with `actor` (strict concurrency)

Copy a seed into a fresh `--workdir`, run the agent against it, then run the hidden tests.

---

## What's committed vs. ignored

Committed: the harness (`agent.py`, `quiz.py`, `intent_test.py`), `requirements.txt`,
`.env.example`, `run_matrix.sh`, and `seeds/`.

Ignored (regenerated per run): `.env`, `.venv/`, every `*-run/` and `run-*/` working
directory, `*.log`, and `*-transcript.json`.

---

## Safety

- The API key lives only in `harness/.env` (gitignored) and is redacted from all output.
- The agent can only touch its `--workdir`.
- Still: treat any `run_shell` agent as you would a script with shell access — run it on
  throwaway projects, not your production tree.
