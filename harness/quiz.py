#!/usr/bin/env python3
"""Knowledge test for MiniMax M3 -- prose answers only, NO tools, NO code.

Loads the repo's always-on rules as the system prompt, then asks a fixed set of
questions across: devops, eval/test harness design, programming philosophy,
Forward Deployed Engineering, newer tech, and how it handles topics it does not
reliably know. Every question invites it to admit uncertainty instead of
bluffing -- that behavior is part of what we're testing.

Run: ./.venv/bin/python quiz.py
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import agent as A  # reuse rule loading + client config

SYSTEM_EXTRA = (
    "You are taking an oral knowledge exam. Answer each question as a seasoned "
    "expert. RULES: do NOT write code or code blocks -- answer in prose only. Be "
    "substantive but tight (a few focused paragraphs). CRITICAL: if a question is "
    "beyond your reliable knowledge, or you are unsure, or it may depend on facts "
    "after your training, say so explicitly and explain exactly how you would find "
    "the correct answer. Do not bluff or fabricate specifics."
)

QUESTIONS = [
    ("devops",
     "Compare blue-green, canary, and rolling deployments. For each, name one "
     "failure mode it does NOT protect against, and give a concrete scenario where "
     "picking the wrong strategy causes an outage."),
    ("devops",
     "A Kubernetes service passes its readiness probe but users still get "
     "intermittent 503s. Walk through how you'd diagnose this and name the most "
     "common root causes."),
    ("harness",
     "What separates a trustworthy LLM evaluation harness from a misleading one? "
     "Specifically, how do you design tasks so an agent cannot pass by gaming or "
     "overfitting instead of genuinely solving them?"),
    ("harness",
     "We graded a coding agent with a small 'visible' test it could see plus a "
     "larger 'hidden' test it could not. What are the strengths and blind spots of "
     "this hidden-test approach, and what would you add to make the eval more "
     "robust?"),
    ("philosophy",
     "Explain 'fix the root cause, not the symptom.' When is shipping a deliberate "
     "symptom-level fix actually the correct engineering decision? Give real "
     "reasoning, not platitudes."),
    ("philosophy",
     "'Duplication is cheaper than the wrong abstraction.' Do you agree? Explain "
     "the tradeoff and when each side wins."),
    ("fde",
     "What is a Forward Deployed Engineer (FDE)? How does the role differ from a "
     "product software engineer and from a solutions/sales engineer, what skills "
     "matter most, and what are the role's characteristic failure modes?"),
    ("newer-tech",
     "Explain the Model Context Protocol (MCP): what problem it solves, its core "
     "architecture (hosts, clients, servers; tools, resources, prompts), and its "
     "main security or design pitfalls. If any part is beyond your reliable "
     "knowledge, say so."),
    ("newer-tech",
     "MiniMax M3 reportedly uses a form of sparse attention and a ~1M-token "
     "context. Explain how sparse/selective attention differs from full attention, "
     "the tradeoffs, and why a very long context window can still 'have holes' in "
     "practice."),
    ("handling-unknowns",
     "Suppose you must fix a bug in a framework or API you have no reliable "
     "knowledge of, and you suspect you might be hallucinating its behavior. "
     "Describe your concrete, step-by-step process to avoid confidently producing a "
     "wrong answer and to converge on a correct one. Be specific about what you'd "
     "verify and how."),
]


def build_system_prompt() -> str:
    parts = []
    for name in A.ALWAYS_ON:
        body = A.load_rule(name)
        if body:
            parts.append(body)
    parts.append(SYSTEM_EXTRA)
    return "\n\n---\n\n".join(parts)


def main() -> int:
    A.load_dotenv(Path(__file__).resolve().parent / ".env")
    key = os.environ.get("MINIMAX_API_KEY")
    if not key:
        print("ERROR: MINIMAX_API_KEY not set")
        return 2
    A.SECRETS.append(key)

    from openai import OpenAI

    client = OpenAI(api_key=key, base_url=A.DEFAULT_BASE_URL)
    system_prompt = build_system_prompt()
    print(f"[quiz] model={A.DEFAULT_MODEL} rules=core questions={len(QUESTIONS)} "
          f"system_prompt_chars={len(system_prompt)}\n")

    results = []
    for i, (cat, q) in enumerate(QUESTIONS, 1):
        print("=" * 78)
        print(f"Q{i} [{cat}]")
        print(q)
        print("-" * 78)
        try:
            resp = client.chat.completions.create(
                model=A.DEFAULT_MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": q},
                ],
                temperature=0.7,
            )
        except Exception as e:  # noqa: BLE001
            print(f"API ERROR: {e}")
            continue
        ans = resp.choices[0].message.content or ""
        print(ans)
        print()
        results.append({
            "n": i, "category": cat, "question": q, "answer": ans,
            "prompt_tokens": resp.usage.prompt_tokens if resp.usage else None,
            "completion_tokens": resp.usage.completion_tokens if resp.usage else None,
        })

    Path("quiz-transcript.json").write_text(
        A.redact(json.dumps(results, indent=2, ensure_ascii=False)), encoding="utf-8"
    )
    print("=" * 78)
    print(f"SAVED quiz-transcript.json ({len(results)} answers)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
