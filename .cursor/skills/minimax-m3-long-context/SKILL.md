---
name: minimax-m3-long-context
description: How to use MiniMax M3's 1M-token MSA context productively: what to load vs. compress, when to retrieve vs. ingest, how to keep skills shallow in the always-on prompt and deep in skills, and how to plan retention across iterations. Load when the task might exceed ~200K tokens, when the user asks to "keep all of this in mind", or when you are tempted to start a fresh session to "free context".
license: MIT
metadata:
  version: "1.0.0"
  category: workflow
  sources:
    - MiniMax M3 release notes (1M-token MSA context)
    - MSA architecture overview (KV-block selection, sparse attention)
  model_assumptions:
    - long-context: required
---

# M3 Long-Context Discipline

M3 ships a 1M-token MSA context window. The room is large; the cost of using it badly is also real. This skill teaches the retention and compression decisions that keep long-context work honest.

## When to Use

- The full content (files, search results, fetched pages, transcripts, design notes) might exceed ~200K tokens.
- The user explicitly asks to "keep all of this in mind", "use the whole repo", or "don't lose anything".
- You are tempted to start a fresh session to "free context" — that is usually a compression failure, not a context failure.
- Multi-file refactors across a large codebase, transcript analysis, full-repo synthesis, or retrieval-augmented synthesis.
- A research / debugging / migration task that you expect to iterate more than 3 times.

For a single-file edit or a small bug fix, you do not need this skill.

## Step 0: Decide Retention Per Slice

For each chunk of evidence you are about to load, pick one of three retention modes **before** you load it:

- **Keep verbatim** — the file is the answer, the user asked to see it, or the next step depends on exact contents.
- **Keep summary** — the contents matter for context but you only need the high-signal lines.
- **Drop** — the chunk is tangential, redundant with something already in context, or only useful for one specific iteration that has passed.

This is the same as `deep-research` Phase 2's "drop tangential" rule, applied at the file level before loading.

## Step 1: Plan The Loader

Before the first read or search, write a 4–6 line plan in your scratchpad:

```text
Loader plan
  In context at start: [system + always-on rules + user task]
  Add verbatim:      [the few files the answer depends on]
  Add as summary:    [reference docs, fetched pages, prior search results]
  Drop:              [tangential files, duplicate docs, raw search output past its iteration]
  Compress at:       [end of each iteration; before any new search round]
```

If you cannot write this plan, the task is under-specified — go back to the user or the codebase.

## Step 2: Compression Rules

After each iteration, replace the raw block with a 2–4 line summary. Use the `deep-research` Compression template:

```
Source: [URL or file path]
Key finding: [1-3 sentences of relevant information]
Confidence: [certain / likely / uncertain]
Relevance: [directly answers sub-query / provides context / tangential]
```

Apply these caps aggressively:

- Never accumulate more than 3 raw blocks of any single source.
- After 3 iterations, the prior iteration's raw output should be down to one summary line.
- "I might need it later" is not a retention reason. If you can recover it with a fresh `Grep` or `Read`, drop it now.

## Step 3: Targeted Read vs. Full Read

Default to the smallest tool that can honestly answer the question:

| Need | Smallest tool |
|------|---------------|
| Symbol / string lookup | `Grep` |
| "How / where / what handles this?" | `SemanticSearch` |
| One specific function or block | `Read` with a small offset/limit |
| Full file required for the task | `Read` (whole file) |
| Cross-file survey of patterns | `SemanticSearch` then targeted `Read` |
| Docs / external | `WebFetch` (one page) |

Reserve full-file reads for files that are the answer, that the user asked to see, or that the next step depends on. On a 1M-token model it is tempting to read everything; that path leads to slow, expensive, and noisier reasoning.

## Step 4: Skill Handoff

Push deep recipes to skills instead of inlining them into the always-on prompt. This is the structural reason the repo has a tiny always-on core and many requestable rules / skills:

- A long domain procedure (incident triage, design system build, 3D scene setup) belongs in a skill, not in a chat message.
- When a skill is loaded, its content is in the active context; when the task shifts, drop the skill.
- Do not paste full skill contents into the conversation. Reference the skill; load it on demand.

## Step 5: Closeout Discipline

When the task touched > 100K tokens of input, add a **Context disposition** row to the standard closeout:

```text
Context disposition:
  Kept verbatim: [list with paths / pages]
  Kept as summary: [list]
  Dropped: [list with one-line reasons]
  Compressed at iteration: [N, N+1, ...]
  Skill(s) loaded mid-task: [list]
```

This makes the context state legible to the next reviewer (or to the next session in a hand-off).

## Anti-Patterns

- Full-repo re-ingest when a slice answer suffices ("let me re-read everything to be sure").
- "Load the whole docs site" without filtering — fetch the page you need, not the whole docs.
- Retaining raw search output past the iteration that used it. Compress or drop.
- Starting a fresh session to "free context" instead of compressing the current one.
- Inlining skill contents into chat instead of referencing the skill.
- Adding a new "summary of summaries" layer that hides the original evidence — summaries should replace raw blocks, not stack on top of them.

## Quick Reference

```text
PLAN    -> write a 4-6 line loader plan before the first read
SLICE   -> pick keep-verbatim / keep-summary / drop per file before loading
READ    -> smallest tool that answers the question (Grep > SemanticSearch > slice Read > full Read)
COMPRESS-> after every iteration: raw -> 2-4 line summary, cap raw blocks per source
SKILL   -> push deep recipes to skills; do not inline into the always-on prompt
CLOSEOUT-> when input > 100K tokens, add a Context disposition row
```
