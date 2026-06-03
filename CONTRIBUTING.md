# Contributing

This repo is intentionally opinionated: keep the always-on core small, keep requestable rules narrow, and keep skills deep only when they cover a repeatable workflow. It is now tuned for MiniMax M3 (1M-token MSA context, native multimodal input) and Cursor 3 (Agents Window, `/worktree`, `/best-of-n`, `Await`, MCP Apps structured content).

## Core Principles

1. One change set, one purpose.
2. Prefer improving an existing rule or skill over adding a near-duplicate.
3. Keep durable behavior in always-on rules.
4. Put domain depth, references, and longer workflows in requestable rules or skills.
5. M3-native behavior (long-context strategy, multimodal input) belongs in the always-on core as **short rules** with deeper mechanics pushed to skills.
6. Verify rule changes against real agent tasks, not only by reading the prose.

## What Goes Where

### Always-on rules

Use always-on rules only for durable, high-leverage behavior such as:

- scope control
- verification language
- tool honesty
- scaffold discipline
- M3 long-context discipline (one short section in the core)
- M3 multimodal input discipline (one short section in the core)

Do not add domain-specific checklists or long examples here. The core's job is the spine, not the depth.

### Requestable rules

Use requestable rules for:

- runtime-specific tool guidance
- cross-language architecture and domain patterns (not per-language cookbooks)
- orchestration depth that should not always consume context

Per-language syntax and framework cookbooks are intentionally omitted. The always-on core's **Code Discipline** section plus repo reading, official docs, and skills cover that surface.

### Skills

Use a skill when the task has a repeatable workflow that benefits from structured guidance, references, or decision routing.

Prefer:

- a focused `SKILL.md`
- optional `reference.md`
- concrete user-language trigger conditions

Avoid omnibus skills that duplicate the core contract.

For very large work, use the `minimax-m3-long-context` skill. For visual-fidelity work, use the `minimax-m3-multimodal-input` skill. Both are first-class skills in this repo, not external dependencies.

## Skill Structure

Recommended layout:

```text
.cursor/skills/<skill-name>/
  SKILL.md
  reference.md                # optional
```

If a skill grows large, split deeper material into references rather than expanding `SKILL.md` indefinitely.

## Skill Frontmatter

Every `SKILL.md` should include:

```yaml
---
name: my-skill
description: >
  What this skill does and when to use it.
license: MIT
metadata:
  version: "1.0.0"
  category: workflow
  sources:
    - Official docs or standards
  model_assumptions: []    # optional; see below
---
```

Rules:

- `name` must match the directory name exactly
- `description` must include concrete trigger language
- `license` should be explicit
- `metadata.version` should be updated when the workflow materially changes
- `metadata.sources` should point to current authoritative references when relevant
- `metadata.model_assumptions` (optional) should name the model capabilities the skill depends on. Examples:
  - `multimodal-input: required` — the skill expects the user can attach images/video
  - `long-context: recommended` — the skill expects a 1M-class context window
  - `cursor-3-runtime: required` — the skill expects the Cursor 3 / Agents Window surface

## Review Checklist

Before submitting a change, check:

- Does this duplicate an existing rule or skill?
- Is the smallest appropriate layer being changed?
- Does the wording teach behavior instead of adding persona fluff?
- Are examples short and behavior-changing, not decorative?
- For skills: does the opening tell the agent exactly when to load it?
- For rules: is this durable enough to justify its token cost?
- For M3-native behavior: is the always-on core still small? If not, push depth into a skill.

## Documentation Sync

When adding or materially changing a skill or major rule:

- update `README.md` if discovery or usage has changed
- keep `docs/AGENTS.md` aligned with the core contract when relevant
- keep examples and references consistent with the current repo structure

## Portable AGENTS Contract

`docs/AGENTS.md` is stored outside the repo root on purpose so Cursor does not auto-activate it while editing this repo.

If you want to use the portable contract in another repo:

1. copy `docs/AGENTS.md`
2. place it at that target repo's root as `AGENTS.md`

## What Not To Add

Do not add:

- fake `<think>` scaffolding
- large duplicated verification doctrine in every file
- brittle tool names or wrappers that are not guaranteed by the runtime
- giant lists of preferences that are already covered elsewhere
- generated project metadata such as `.xcodeproj`, `.pbxproj`, or similar hand-written artifacts
- "AI slop" UI patterns in any design guidance or skill
- visual-fidelity claims without a `multimodal-grounded` path to back them
