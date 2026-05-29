<div align="center">

# MiniMax M2.7 Cursor Rules

[![Stars](https://img.shields.io/github/stars/madebyaris/advance-minimax-m2-cursor-rules?style=flat-square)](https://github.com/madebyaris/advance-minimax-m2-cursor-rules/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![Cursor 3](https://img.shields.io/badge/Tested-Cursor%203-blue?style=flat-square)](https://cursor.com/blog/cursor-3)
[![MiniMax M2.7](https://img.shields.io/badge/MiniMax-M2.7-purple?style=flat-square)](https://platform.minimax.io)
[![Any Model](https://img.shields.io/badge/Compatible-Any%20Model-green?style=flat-square)](#model-compatibility)

**MiniMax M2.7 rules for repo-scale engineering, agent teams, skills, and dynamic tool use**

*Built for **MiniMax M2.7**, aligned with the official release and API docs, and written to stay useful across model changes.*

[Quick Start](#quick-start) | [Architecture](#rule-architecture) | [M27-runtime](#m27-runtime-modes) | [AGENTSmd](#agentsmd-for-other-ides-and-clis)

</div>

---

## Why This Repo Exists

This repo is designed to make MiniMax M2.7 feel strong in the places the official release emphasizes most:

- repo-scale and end-to-end engineering
- agent harnesses and multi-agent collaboration
- long skill packs and detailed tool contracts
- dynamic tool discovery in changing environments
- proportional verification with evidence-backed closeouts

The goal is not to make MiniMax merely imitate another provider's tone. The goal is to give M2.7 a durable execution spine that complements its official positioning around real-world engineering, complex skills, and agent workflows.

## Model Compatibility

The rules are designed to survive model changes:

- the core rule stays short and durable
- runtime-specific guidance lives in requestable rules
- tool advice is written around whatever the current environment actually exposes
- version-sensitive claims are meant to be verified at runtime, not frozen into the rules

This makes the repo useful for MiniMax first, while still compatible with other Cursor-supported models.

## Why M2.7-Native

MiniMax positions M2.7 as strong at real-world software engineering, full project delivery, large skill adherence, and agent teams rather than only one-shot code generation [MiniMax M2.7 release report](https://www.minimax.io/news/minimax-m27-en) [MiniMax M2.7 model page](https://www.minimax.io/models/text/m27).

That means this repo optimizes for:

- bounded repo exploration instead of reading everything
- smallest proving slices for large tasks
- explicit role and handoff discipline for multi-agent work
- strong skill contracts instead of vague long prompts
- truthful runtime and verification reporting

## What Changed

This refactor removes most of the old prompt bloat:

- no more Opus-style identity anchoring in the core
- a separate always-on verification contract instead of burying proof rules in prose
- far less duplicated tool and verification doctrine
- no hardcoded month/year version examples in workflow rules
- no fake `<think>` or `<thinking>` scaffolding
- less "always run everything" language in domain-specific rules
- `docs/AGENTS.md` is now a real standalone agent contract for non-Cursor environments
- M2.7-specific docs now distinguish core execution rules from optional agent-team, skill, and tool-discovery depth

## Execution Guarantees

The repo now tries to enforce a few non-negotiable behaviors:

- new packages, frameworks, and toolchains must be checked against current authoritative sources before they are recommended or installed
- scaffolding should use the framework's official CLI or official `create` or `init` path when one exists
- scaffold output must be inspected before continuing after generators or CLIs run
- runnable work is not done until there is runnable proof, not just static confidence
- if a required check fails or is skipped, the agent should report `blocked` or `implemented but unverified` instead of claiming completion
- browser or user-surface verification is required for UI and interaction claims
- tool-based promises should not be made until the current runtime path is confirmed

## M2.7 Runtime Modes

The official API docs expose both `MiniMax-M2.7` and `MiniMax-M2.7-highspeed`, each with a `204,800` token context window. The docs describe standard M2.7 at roughly `60 tps` and `M2.7-highspeed` at roughly `100 tps`, with the highspeed variant positioned as the same capability profile with lower latency [MiniMax text generation docs](https://platform.minimax.io/docs/guides/text-generation) [MiniMax API overview](https://platform.minimax.io/docs/api-reference/api-overview).

Use that split like this:

| Model | Best fit |
|------|---------|
| `MiniMax-M2.7` | Deep repo work, complex synthesis, richer multi-step tasks |
| `MiniMax-M2.7-highspeed` | Faster interactive loops, shorter verification cycles, lower-latency coding assistance |

## Solver Loop

The main thing this repo now tries to transfer into MiniMax M2.7 is a repeatable solver loop:

1. Define the outcome in operational terms.
2. Inspect the repo and runtime before deciding.
3. Find the spine: entry points, data flow, state boundaries, persistence, and user-visible behavior.
4. Build the smallest vertical slice that proves the feature works.
5. Verify at the surface where the user experiences the change.
6. Expand scope only after the core slice is working.

For app-building, this means:

- do not start with a pile of components
- resolve key flows and acceptance first
- prove one end-to-end slice early
- add polish and secondary features afterward

The minimum proving loop for a new app should usually be:

1. install or setup succeeds
2. dev server or health check starts
3. production build succeeds
4. one primary happy-path flow works
5. promised integrations such as styling, routing, persistence, or auth are actually verified

Example:

- For "build a task app", prioritize `create -> list -> complete -> persist -> reload`
- Delay filters, collaboration, settings, and animations until the core path works

## MoE Note

These rules do **not** assume you can directly control a model's internal MoE routing through persona text.

The controllable levers are:

- cleaner context
- better decomposition
- better tool routing
- better verification loops
- clearer definitions of done

If MiniMax performs better after a prompt rewrite, the likely reason is improved external problem structure, not magical direct access to hidden experts.

## Quick Start

### For Cursor

```bash
git clone https://github.com/madebyaris/advance-minimax-m2-cursor-rules.git
cp -r advance-minimax-m2-cursor-rules/.cursor your-project/.cursor
```

The always-on rules are:

- `.cursor/rules/minimax-m2-core.mdc`
- `.cursor/rules/minimax-m2-status-verification.mdc`

The rest of the rules are requestable and narrower by design.

The official docs recommend Anthropic-compatible access for MiniMax text models and also support OpenAI-compatible access paths [MiniMax text generation docs](https://platform.minimax.io/docs/guides/text-generation) [MiniMax API overview](https://platform.minimax.io/docs/api-reference/api-overview).

### For Other IDEs and CLIs

Copy `docs/AGENTS.md` into the target repo root as `AGENTS.md`, or use it as your agent instructions file in environments that support a portable agent contract.
It intentionally lives under `docs/` in this repo so Cursor does not auto-activate it while you are editing these rules.

## Rule Architecture

### Always-On Core

| File | Purpose |
|------|---------|
| `.cursor/rules/minimax-m2-core.mdc` | Durable always-on execution behavior: solver loop, scope control, code discipline, truthful tool use, scaffold discipline, and concise progress |
| `.cursor/rules/minimax-m2-status-verification.mdc` | Always-on status and proof contract: exact claim labels, proof matching, and evidence-first closeouts |

### Runtime Rules

| File | Purpose |
|------|---------|
| `.cursor/rules/model-compatibility.mdc` | Prompt hierarchy, tool discipline, and context control |
| `.cursor/rules/cursor-tools-mastery.mdc` | Current tool-selection patterns inside Cursor |
| `.cursor/rules/minimax-m2-verification.mdc` | Proportional verification guidance |
| `.cursor/rules/minimax-mcp-tools.mdc` | Current-doc, web, and MCP/plugin lookup guidance |
| `.cursor/rules/cursor-agent-orchestration.mdc` | Planning, subagents, and multi-step coordination |
| `.cursor/rules/clarify-first-prompting.mdc` | Ask only on real forks after inspecting first |
| `.cursor/rules/agent-teams.mdc` | Team-role boundaries, handoffs, escalation, and agent graph choices |
| `.cursor/rules/skill-authoring.mdc` | When to use skills, how to structure them, and how to avoid skill bloat |
| `.cursor/rules/tool-discovery.mdc` | Runtime tool inventory, MCP/schema discovery, capability mapping, and fallbacks |

### Domain Rules

Requestable rules for cross-cutting domains — not per-language cookbooks. Language-specific idioms come from reading the repo, official docs, and the always-on **Code Discipline** section in the core.

| File | Purpose |
|------|---------|
| `.cursor/rules/language-agnostic-patterns.mdc` | SOLID, design patterns, change discipline, code review heuristics |
| `.cursor/rules/design-systems.mdc` | Tokens, shadcn/ui, Tailwind v4 mechanics (aesthetics → `anti-slop-design` skill) |
| `.cursor/rules/3d-graphics.mdc` | Three.js / R3F syntax, container sizing, import traps (quality → `3d-web-experiences` skill) |
| `.cursor/rules/devops-infrastructure.mdc` | Docker, k8s, Terraform, CI/CD — validate-before-apply, infra traps (lean) |
| `.cursor/rules/mobile-cross-platform.mdc` | Flutter / RN / Expo — CLI-first, architecture, mobile verify (lean) |

### Skills

The repo's `.cursor/skills/` directory is part of the intended M2.7 workflow, not a side feature. Skills let you keep deeper, domain-specific procedures out of the always-on core while still giving the model large, structured guidance when the task warrants it.

Use skills when:

- the task has a repeatable workflow that is too detailed for the always-on core
- the task needs examples, references, or category-specific heuristics
- you want progressive disclosure through `SKILL.md` and optional companion files such as `reference.md`

Current local skills:

| Skill | Purpose |
|------|---------|
| `.cursor/skills/anti-slop-design/` | Category-aware design direction, anti-slop checks, and UI polish |
| `.cursor/skills/3d-web-experiences/` | Aesthetic direction, performance budgets, responsive WebGL, and degradation for Three.js / R3F 3D |
| `.cursor/skills/deep-research/` | Iterative mixed-source research, synthesis, and anti-hallucination recovery |
| `.cursor/skills/incident-triage-harness/` | Production-style debugging and mitigation workflow |
| `.cursor/skills/minimax-multimodal-toolkit/` | MiniMax-native image, video, voice, music, and media-processing routing |

## Design Principles

### Keep The Core Small

Large always-on prompts waste context and often reduce execution quality. The core rule should contain only durable behavior with high leverage — including **Code Discipline** (read-before-edit, minimal diff, CI discovery, common traps) so per-language cookbooks are unnecessary.

### Prefer Repo Truth Over Training Defaults

Good coding rules teach: inspect manifests and CI first, match existing conventions, verify with the repo's own commands, and load `language-agnostic-patterns` only when designing structure — not when writing everyday syntax.

### Prefer Capability Framing Over Persona Framing

Rules work better when they say:

- inspect first
- build the smallest proving slice
- verify before claiming success

They work worse when they spend lots of tokens on identity, status, or stylistic self-description.

### Make Acceptance Explicit

Good rules do not stop at "verify somehow." They define the minimum proof for the kind of claim being made, especially for new app scaffolds and user-facing behavior.

### Trust The Current Environment

Cursor's tool surface changes. The rules should teach behavior that survives those changes instead of freezing old tool names or wrappers.

## Agent Teams, Skills, And Tool Discovery

These are the three biggest places where M2.7 feels different from a generic coding model:

- **Agent Teams**: use explicit roles, bounded handoffs, and clear escalation points instead of vague multi-agent optimism
- **Skills**: invest in long, high-signal skill contracts rather than stuffing rare workflows into the always-on prompt
- **Tool Discovery**: discover the live runtime surface, schemas, and MCP shape before promising capability

The optional rules in this repo are meant to deepen those areas without bloating the always-on core.

## Example Patterns

If you want concrete M2.7-native patterns instead of only rules, start here:

- [`examples/agent-teams-product-prototype.md`](examples/agent-teams-product-prototype.md) - a bounded planner/explorer/builder/verifier workflow for multi-agent product work
- [`.cursor/skills/incident-triage-harness/SKILL.md`](.cursor/skills/incident-triage-harness/SKILL.md) - a large-skill example for incident-style debugging and mitigation
- [`.cursor/skills/incident-triage-harness/reference.md`](.cursor/skills/incident-triage-harness/reference.md) - companion reference material showing progressive disclosure for a deeper skill

## AGENTS.md For Other IDEs and CLIs

`docs/AGENTS.md` is the portable standalone version of MiniMax M2.7 behavior for environments that use agent instruction files but do not support Cursor rules.
It carries the core behavior directly instead of acting as a thin pointer file.

It is focused on:

- action-first execution
- solver-loop thinking
- scope control
- read-before-edit discipline
- proportional verification
- explicit status labels and evidence-backed completion claims
- current-source version discipline
- CLI-first scaffolding
- concise communication

To use it elsewhere, copy `docs/AGENTS.md` into the target repo root as `AGENTS.md`.

If you use both `AGENTS.md` and `.cursor/rules`, keep them aligned rather than letting them evolve into contradictory prompt layers.

The example patterns above are still useful outside Cursor: the agent-team workflow is portable markdown, while the incident-triage skill shows how to structure a large workflow even if your environment uses a different skill system.

## Warnings

Never manually fabricate:

- `.xcodeproj`
- `project.pbxproj`
- `.xcworkspace`
- complex `.sln` or similar IDE-managed project metadata

Use the relevant CLI or IDE instead, then let the agent work inside the real project.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the repo's contribution rules, skill frontmatter contract, and placement guidance for always-on rules, requestable rules, and skills.

## References

- [MiniMax M2.7 Release Report](https://www.minimax.io/news/minimax-m27-en)
- [MiniMax M2.7 Model Page](https://www.minimax.io/models/text/m27)
- [MiniMax Text Generation Docs](https://platform.minimax.io/docs/guides/text-generation)
- [MiniMax API Overview](https://platform.minimax.io/docs/api-reference/api-overview)
- [Cursor Changelog](https://cursor.com/changelog)
- [Cursor Rules Docs](https://cursor.com/docs/context/rules)
- [Cursor Agent Best Practices](https://cursor.com/blog/agent-best-practices)
- [MiniMax Platform](https://platform.minimax.io)
- [OpenAI Codex Best Practices](https://developers.openai.com/codex/learn/best-practices/)
- [OpenAI Exec Plans](https://cookbook.openai.com/articles/codex_exec_plans)

---

<div align="center">

**Made with care by [Aris Setiawan](https://github.com/madebyaris) at [MiniMax](https://minimax.io)**

</div>
