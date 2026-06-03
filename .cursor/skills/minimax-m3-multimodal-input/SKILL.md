---
name: minimax-m3-multimodal-input
description: How to use MiniMax M3's native multimodal input (image, video) for grounded decisions in coding work. Covers reading attached images/frames, treating them as ground truth for visual claims, screenshot diffing, design parity from mockups, and routing visual evidence through reports and PRs. Load when the user attaches an image, screenshot, mockup, frame, or short clip — or when the task involves "make it look like this", "match this design", "why does this UI look wrong", or "read this error screenshot".
license: MIT
metadata:
  version: "1.0.0"
  category: workflow
  sources:
    - MiniMax M3 multimodal input documentation
    - Screenshot-driven development practice
  model_assumptions:
    - multimodal-input: required
---

# M3 Multimodal Input

M3 accepts text + image + video as native input. The point of this skill is to use that capability honestly: ground every visual claim in the actual file the model can read, and re-read the post-change state before declaring a visual fix done.

## When to Use

- The user attaches an image, screenshot, mockup, frame, or short clip.
- The task involves "make it look like this", "match this design", "why does this UI look wrong", "read this error screenshot", or "match this reference video".
- You are about to claim a visual or styling result. Any visual claim without a `multimodal-grounded` read is a guess.
- A bug report or feature request references a UI state the user can show you (rather than describe in words).

If the user is only talking about generating media (creating new images, video, TTS, music), the **`minimax-multimodal-toolkit`** skill is the right one — that skill is for output; this one is for input.

## Step 0: Inventory The Input

Before reasoning, identify what the user attached and what you can actually read:

- **Static image** (PNG / JPG / WebP / SVG) — `Read` the file path the user provided or that the runtime surfaces.
- **Multi-frame video or screen recording** — pick a small number of representative frames (start, mid, end) and reason about the in-between motion explicitly.
- **Inline attachment** that the runtime renders into the chat — the model sees it directly; cite it as "the attached image" with the visible region.
- **Multiple images in a set** (desktop + tablet + mobile mockups, before + after screenshots) — re-read each before claiming a responsive match or a fix.

If you cannot actually see the file, say so and ask. Do not invent the contents of an image you did not open.

## Step 1: Ground In The File, Not The Prose

Always `Read` the file/frame and reference exact paths. Do not paraphrase a guessed description.

- Cite the file path (`/path/to/screenshot.png`) and, when relevant, the region (`top-right nav`, `hero block`, `error toast`).
- Quote visible text directly — error messages, button labels, empty-state copy. Do not paraphrase.
- If the user described the image in prose, treat their prose as a hint, not as evidence. The image is the evidence.

## Step 2: Visual-Fidelity Claims

Any time the user (or you) say "looks right", "matches", "fixed", or "as designed", you owe a `multimodal-grounded` proof per the always-on status rule.

Shape:

```text
Visual claim: [what you say it looks like]
Reference (pre / target): [file path]
Actual (post / current):   [file path]
Region inspected:           [where in the frame you looked]
Verdict:                    [matches / does not match / partial — say which and why]
```

If you cannot re-read the post-change state, downgrade the claim to `unverified` — do not say "fixed" without seeing the fix.

## Step 3: Design Parity (Mock → Code)

For "match this mock" work, use the image as the contract:

- Identify the **regions** of the mock: hero, nav, primary CTA, footer, repeating components. Reason per region, not per pixel.
- Match the mock's **intent**, not its exact pixel values, when the project has its own design tokens. Override tokens only when the mock is high-fidelity and the user wants a pixel match.
- For multi-resolution mockups, hold the layout intent constant; let the responsive behavior do the work.
- For dark/light mode parity, read both the dark and light mock frames before declaring a mode-aware fix.

Cite the mock's file path in the PR / commit message so the next reviewer can re-read the contract.

## Step 4: Error UI / Bug Reports

When the user attaches a screenshot or clip of a broken UI:

- Read it. Quote the visible error or broken text directly in the bug writeup.
- Name the file path of the screenshot/clip in the report.
- If the bug is interactive, ask the user to attach a short screen recording (or trigger the interaction and screenshot the result yourself in a headless browser when possible).
- Do not invent text that is not in the image. "Likely says 'Connection failed'" without reading it is an inference, not evidence.

## Step 5: Verification

After a UI change:

1. Render or capture the post-change state (screenshot, frame, or browser snapshot).
2. `Read` the post-change file in the current session.
3. Compare to the reference (pre-change state, mock, or expected behavior).
4. State the verdict with the four fields from Step 2.
5. If the verdict is "does not match" or "partial", say what specifically diverged and the smallest next change.

This is the loop the always-on `minimax-m3-status-verification` rule calls `multimodal-grounded`. Skipping the post-change read is the most common visual-fidelity failure.

## Anti-Patterns

- Describing an image you did not actually open. If the runtime could not surface the file, say so.
- "Looks right" without re-reading the post-change state.
- Paraphrasing visible text instead of quoting it.
- Treating a single frame as evidence for a multi-frame or animated UI.
- Claiming a responsive match when you only re-read the desktop frame.
- Inventing colors / spacing / typography instead of reading them from the mock.

## Quick Reference

```text
INVENTORY  -> image, multi-frame video, inline attachment, multi-image set?
GROUND     -> Read the file; cite the path; quote visible text
CLAIM      -> any visual claim needs a reference path + actual path + region + verdict
PARITY     -> mock is the contract; match intent by region; cite the path in the PR
ERROR UI   -> read the screenshot/clip; quote visible text; name the path
VERIFY     -> render/capture post-change; re-read; compare; state verdict
```
