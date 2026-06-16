#!/usr/bin/env python3
"""Intent-inference test: can M3 (with our rules) read what a non-technical or
junior user *actually* wants from a terse/ambiguous prompt?

Framing is deliberately neutral -- it does NOT tell the model how to clarify or
infer. The loaded core rules ("understand intent, then the letter" / "clarify
only on real forks") are what we're testing. Each prompt is sent as a real user
turn; we observe the first response.

Run: ./.venv/bin/python intent_test.py
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import agent as A

SYSTEM_EXTRA = (
    "You are an AI coding assistant operating inside the user's IDE (like Cursor). "
    "The next message is exactly what the user typed -- it may be terse, vague, or "
    "written by someone with little programming background, and you do not have the "
    "repository contents in front of you yet. Reply to them as you normally would "
    "in that setting."
)

# (persona, prompt-as-the-user-would-type-it)
PROMPTS = [
    ("non-dev / small-biz owner",
     "my website is really slow please make it fast"),
    ("non-dev / small-biz owner",
     "i need people to be able to book appointments with me"),
    ("non-dev",
     "the totals on my sales page dont match whats in my spreadsheet, fix it"),
    ("junior dev",
     "refactor this function to be cleaner"),  # nothing attached -- trap
    ("junior dev",
     "the api returns 500 sometimes, can you fix it"),
    ("non-dev",
     "make my site work on iphone"),
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
    print(f"[intent] model={A.DEFAULT_MODEL} rules=core prompts={len(PROMPTS)}\n")

    results = []
    for i, (persona, prompt) in enumerate(PROMPTS, 1):
        print("=" * 78)
        print(f"P{i} [{persona}]  user typed: {prompt!r}")
        print("-" * 78)
        try:
            resp = client.chat.completions.create(
                model=A.DEFAULT_MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt},
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
            "n": i, "persona": persona, "prompt": prompt, "answer": ans,
            "prompt_tokens": resp.usage.prompt_tokens if resp.usage else None,
            "completion_tokens": resp.usage.completion_tokens if resp.usage else None,
        })

    Path("intent-transcript.json").write_text(
        A.redact(json.dumps(results, indent=2, ensure_ascii=False)), encoding="utf-8"
    )
    print("=" * 78)
    print(f"SAVED intent-transcript.json ({len(results)} answers)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
