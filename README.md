<div align="center">

# MiniMax M3 Cursor Rules

#### A durable execution spine for repo-scale engineering on M3 + Cursor 3 — with frontier-agent coding judgment and reasoning protocols distilled into rules any model can run.

[![Stars](https://img.shields.io/github/stars/madebyaris/advance-minimax-m3-cursor-rules?style=flat-square&color=8b5cf6)](https://github.com/madebyaris/advance-minimax-m3-cursor-rules/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![Cursor 3](https://img.shields.io/badge/Tested-Cursor%203-blue?style=flat-square)](https://cursor.com/blog/cursor-3)
[![MiniMax M3](https://img.shields.io/badge/MiniMax-M3-8b5cf6?style=flat-square)](https://platform.minimax.io)
[![M3 1M Context](https://img.shields.io/badge/Context-1M_MSA-22c55e?style=flat-square)](https://platform.minimax.io)
[![M3 Multimodal](https://img.shields.io/badge/Multimodal-Native-3b82f6?style=flat-square)](https://platform.minimax.io)
[![Any Model](https://img.shields.io/badge/Compatible-Any%20Model-22c55e?style=flat-square)](#-model-compatibility)

<br/>

![Always-On Rules](https://img.shields.io/badge/Always--On-2_rules-0f172a?style=for-the-badge)
![Requestable Rules](https://img.shields.io/badge/Requestable-18_rules-1e293b?style=for-the-badge)
![Skills](https://img.shields.io/badge/Skills-7_packs-14b8a6?style=for-the-badge)

<br/>

*Tuned for **MiniMax M3** (1M-token MSA context, native multimodal input) and **Cursor 3** (Agents Window, `/worktree`, `/best-of-n`, `Await`, MCP Apps). Written to stay useful across model changes.*

<sub>

[Quick Start](#-quick-start) · [Why This Repo](#-why-this-repo-exists) · [Architecture](#-rule-architecture) · [Runtime Modes](#-m3-runtime-modes) · [Solver Loop](#-the-solver-loop) · [AGENTS.md](#-agentsmd-for-other-ides-and-clis) · [References](#-references)

</sub>

</div>

---

## At A Glance

| | What you get |
|---|---|
| Lean always-on core | Two durable rules carry the execution spine — reasoning protocol, solver loop, scope control, code discipline, M3 long-context discipline, M3 multimodal input discipline, and a strict proof contract. No persona bloat. |
| Frontier craft, distilled | The `fable5-*` craft rules transfer the judgment behind SWE-Bench-class agents — locate-before-write, root-cause method, simplicity taste, test integrity, hypothesis ledgers, stuck-strategy ladder — to M3 and any open model. |
| Progressive depth | 18 requestable rules + 7 skill packs load only when the task needs them, so context stays clean. |
| M3 long-context discipline | 1M-token MSA context is a real lever, but the failure mode shifts to "kept too much raw output." A dedicated skill (`minimax-m3-long-context`) teaches the retention and compression cadence. |
| M3 multimodal-native | Image and video inputs ground visual claims (`multimodal-grounded`). A dedicated skill (`minimax-m3-multimodal-input`) teaches the design-parity and screenshot-triage workflow. |
| Cursor 3 surface | Explicit guidance for the Agents Window, `/worktree`, `/best-of-n`, `Await`, MCP Apps structured content, and Composer 2. |
| Honest tool use | The agent works the *current* runtime — no invented tools, no stale wrappers, no promises before the path is confirmed. |
| Evidence-backed closeouts | Explicit status labels (`verified` / `unverified` / `blocked` / `multimodal-grounded`), minimum-proof rules per change type, and red → green proof for bug fixes. |
| Portable | `docs/AGENTS.md` carries the same behavior to non-Cursor IDEs and CLIs. |
| Model-resilient | Tuned for M3 first, compatible with any Cursor-supported model. |

> **The bet:** MiniMax doesn't get better from persona text. It gets better from cleaner context, smaller proving slices, better tool routing, honest verification — and the same judgment habits frontier agents use: fix the broken invariant, not the symptom; never game a test; update the plan after every tool result. Every rule here optimizes for that.

---

## Quick Start

### For Cursor

```bash
git clone https://github.com/madebyaris/advance-minimax-m3-cursor-rules.git
cp -r advance-minimax-m3-cursor-rules/.cursor your-project/.cursor
```

That's it. Two rules are **always on**:

- `.cursor/rules/minimax-m3-core.mdc` — reasoning protocol, execution behavior, code discipline, M3 long-context discipline, M3 multimodal input discipline
- `.cursor/rules/minimax-m3-status-verification.mdc` — status & proof contract (`multimodal-grounded` visual proof, red → green for bug fixes)

Everything else is **requestable** and narrower by design — it loads when the task or file globs call for it. The two `fable5-*` craft rules load for non-trivial coding and reasoning work; the rest attach by runtime or domain.

> The official docs recommend Anthropic-compatible access for MiniMax text models, and also support OpenAI-compatible access paths. See [MiniMax text generation docs](https://platform.minimax.io/docs/guides/text-generation) · [MiniMax API overview](https://platform.minimax.io/docs/api-reference/api-overview).

### For Other IDEs and CLIs

Copy `docs/AGENTS.md` into the target repo root as `AGENTS.md`. It lives under `docs/` here on purpose, so Cursor does not auto-activate it while you edit these rules.

---

## Repository Layout

```text
.cursor/
├── rules/                         # 20 rules (2 always-on + 18 requestable)
│   ├── minimax-m3-core.mdc                  ★ always-on · execution spine + reasoning protocol + M3 disciplines
│   ├── minimax-m3-status-verification.mdc   ★ always-on · proof contract (+ multimodal-grounded, red → green)
│   ├── fable5-coding-craft.mdc              requestable · frontier coding judgment distillation
│   ├── fable5-reasoning.mdc                 requestable · frontier thinking protocols
│   └── …                                    requestable: runtime + domain
├── agents/                        # subagents (/debugger, /verifier)
│   ├── debugger.md                          root-cause analysis: hypothesis ledger, bisection, fix-at-the-owner
│   └── verifier.md                          adversarial validation: claim-gaming hunt, proof execution
└── skills/                        # 7 deep, structured skill packs
    ├── anti-slop-design/
    ├── 3d-web-experiences/
    ├── deep-research/
    ├── incident-triage-harness/
    ├── minimax-multimodal-toolkit/
    ├── minimax-m3-long-context/             # new · 1M-context retention/compression
    └── minimax-m3-multimodal-input/         # new · native image/video input workflow
docs/
└── AGENTS.md                      # portable agent contract (non-Cursor)
examples/
└── agent-teams-product-prototype.md
```

---

## Why This Repo Exists

This repo makes MiniMax M3 feel strong exactly where the M3 release puts its emphasis:

- 1M-token MSA context — and the discipline to use it without bloating
- native multimodal input (image, video) — and the discipline to ground visual claims in the actual file
- higher agentic and coding benchmarks — leveraged through role separation and explicit verification
- frontier coding judgment — the `fable5-*` craft rules distill the habits behind SWE-Bench-class scores (root-cause method, test integrity, interleaved thinking) into a form open models can follow
- agent harnesses and multi-agent collaboration, including `/best-of-n` as a first-class team pattern
- long skill packs and detailed tool contracts that load only when relevant
- dynamic tool discovery in changing environments (Cursor 3's evolving MCP + plugin surface)

The goal is **not** to make MiniMax imitate another provider's tone. It is to transfer the *judgment* — where to change code, how to prove a fix, when to switch strategy — while M3 keeps its own voice. A durable execution spine that complements its official positioning around real-world engineering, complex skills, agent workflows, long context, and multimodal grounding.

<details>
<summary><b>Why M3-native (and what that optimizes for)</b></summary>

<br/>

MiniMax positions M3 as a generational shift: 1M-token MSA context, native multimodal input, and higher agentic and coding benchmarks ([model page](https://platform.minimax.io)).

So this repo optimizes for:

- explicit retention and compression decisions on 1M tokens (not "fit it all and hope")
- grounding every visual claim in the actual attached image/frame (`multimodal-grounded`)
- bounded repo exploration instead of reading everything
- smallest proving slices for large tasks
- explicit role and handoff discipline for multi-agent work, including `/best-of-n` for high-stakes choices
- strong skill contracts instead of vague long prompts
- truthful runtime and verification reporting

</details>

<details>
<summary><b>The MoE / MSA note — what you can and cannot control</b></summary>

<br/>

These rules do **not** assume you can steer a model's internal routing through persona text. M3 swaps full attention for MiniMax Sparse Attention (MSA), which selects KV-blocks per query — and the controllable levers are still external:

- cleaner context (with explicit retention decisions)
- better decomposition
- better tool routing (including the Cursor 3 surface)
- better verification loops, including `multimodal-grounded` visual proof
- clearer definitions of done

If M3 performs better after a rule change, the likely reason is improved external problem structure — not magic access to hidden experts.

</details>

---

## The Solver Loop

The single most important behavior this repo transfers into M3:

```text
1. Define the outcome in operational terms.
2. Inspect the repo and runtime before deciding.
3. Find the spine: entry points, data flow, state, persistence, user-visible behavior.
4. Build the smallest vertical slice that proves the feature works.
5. Verify at the surface where the user experiences the change.
   - For visual claims: re-read the actual post-change frame (multimodal-grounded).
6. Expand scope only after the core slice works.
```

**For app-building**, that means: don't start with a pile of components — resolve key flows first, prove one end-to-end slice early, then add polish.

| New-app proving loop | |
|---|---|
| 1 | install / setup succeeds |
| 2 | dev server or health check starts |
| 3 | production build succeeds |
| 4 | one primary happy-path flow works |
| 5 | promised integrations (styling, routing, persistence, auth) are actually verified |
| 6 | any visual claims are `multimodal-grounded` (re-read the post-change frame) |

> **Example —** for "build a task app", prioritize `create → list → complete → persist → reload`. Delay filters, collaboration, settings, and animations until the core path works.

---

## Execution Guarantees

A few behaviors the repo treats as non-negotiable:

- New packages, frameworks, and toolchains are checked against current authoritative sources **before** they are recommended or installed.
- Scaffolding uses the framework's official CLI / `create` / `init` path when one exists.
- Scaffold output is inspected before continuing.
- Runnable work is not "done" until there is **runnable proof**, not just static confidence.
- Bug fixes are proven **red → green**: the reproduction fails before the change and passes after. A check that was never red proves nothing.
- Tests are never weakened, skipped, or special-cased to reach green — the test is the spec; if the spec looks wrong, that goes to the user.
- Fixes land at the **root cause** (the broken invariant), not at the symptom site; shipped workarounds are labeled as workarounds.
- Stubs, mocks, and hardcoded placeholders are declared in the closeout — never presented as finished behavior.
- Visual work is not "done" until the post-change frame is re-read (`multimodal-grounded`).
- If a required check fails or is skipped, the agent reports `blocked` or `implemented but unverified` — never a false completion.
- Browser or user-surface verification is required for UI and interaction claims.
- Tool-based promises wait until the runtime path is confirmed.
- 1M-token context does not free the agent from compressing; it raises the cost of failing to compress.

---

## Rule Architecture

The system is layered: a tiny always-on core, craft rules that carry frontier judgment, runtime rules that load on demand, and domain rules that attach via file globs. Depth lives in skills.

### ★ Always-On Core

| File | Purpose |
|------|---------|
| `minimax-m3-core.mdc` | Durable execution behavior: reasoning protocol (intent-first, interleaved thinking, explicit hypotheses, end-to-end ownership), solver loop, scope control, code discipline (root-cause-first, boundary validation, test integrity), M3 long-context discipline, M3 multimodal input discipline, truthful tool use, scaffold discipline, concise progress |
| `minimax-m3-status-verification.mdc` | Status & proof contract: exact claim labels, proof matching, red → green for bug fixes, `multimodal-grounded` visual proof, evidence-first closeouts |

### Craft Rules (Fable 5 Distillation)

Frontier-agent judgment distilled into requestable rules — the habits behind SWE-Bench-class scores, made transferable to M3 and any open model:

| File | Purpose |
|------|---------|
| `fable5-coding-craft.mdc` | The craft hierarchy, locate-before-write, root-cause method (broken-invariant chain), simplicity taste, error-handling philosophy, test integrity, refactoring discipline, LLM failure modes and counters |
| `fable5-reasoning.mdc` | Three-readings task interpretation, risk-first decomposition, approach selection, interleaved thinking loop (surprise rule, stale-plan rule), hypothesis ledgers, premortems, calibration, stuck-strategy ladder |

### Runtime Rules

| File | Purpose |
|------|---------|
| `model-compatibility.mdc` | Prompt hierarchy, M3-first model selection, tool discipline, context control across models |
| `cursor-tools-mastery.mdc` | Cursor 3 tool-selection patterns: Agents Window, `/worktree`, `/best-of-n`, `Await`, Composer 2 |
| `cursor-mcp-optimization.mdc` | Browser, Figma, Cloudflare tools, MCP Apps structured content, direct action patterns |
| `cursor-agent-orchestration.mdc` | Multi-environment planning, `/best-of-n` as an orchestration primitive, `Await` for long-running branches |
| `agent-teams.mdc` | Role boundaries, multi-environment handoffs, `/best-of-n` as a team pattern, escalation, serial vs parallel |
| `tool-discovery.mdc` | Runtime tool inventory, MCP/schema discovery, MCP Apps structured content, safe fallbacks |
| `minimax-mcp-tools.mdc` | Current-doc retrieval, direct-tool preference, version-aware lookups, MCP Apps structured content |
| `minimax-m3-verification.mdc` | Proportional verification playbook (shell + browser + multimodal-grounded checks, test integrity during verification) |
| `minimax-m3-self-evolution.mdc` | Iterative refinement loops, compress-before-iterate, autonomous debugging |
| `skill-authoring.mdc` | When to use skills, how to structure them, how to declare `model_assumptions` |
| `clarify-first-prompting.mdc` | Ask only on real forks, after inspecting first |

### Domain Rules

Requestable rules for cross-cutting domains — **not** per-language cookbooks. Language-specific idioms come from reading the repo, official docs, and the always-on **Code Discipline** section.

| File | Purpose |
|------|---------|
| `language-agnostic-patterns.mdc` | Pattern judgment (when *not* to apply), SOLID, design patterns, change discipline, code-review heuristics |
| `design-systems.mdc` | Tokens, shadcn/ui, Tailwind v4 mechanics → aesthetics via `anti-slop-design` |
| `3d-graphics.mdc` | Three.js / R3F syntax, container sizing, import traps → quality via `3d-web-experiences` |
| `devops-infrastructure.mdc` | Docker, k8s, Terraform, CI/CD — validate-before-apply, infra traps (lean) |
| `mobile-cross-platform.mdc` | Flutter / RN / Expo — CLI-first, architecture, mobile verify (lean) |

### Skills

Skills keep deep, domain-specific procedures out of the always-on core, then deliver large structured guidance through progressive disclosure (`SKILL.md` + optional `reference.md`).

| Skill | Purpose |
|------|---------|
| `anti-slop-design/` | Category-aware design direction, anti-slop checks, UI polish, multimodal design parity from mocks |
| `3d-web-experiences/` | Aesthetic direction, performance budgets, responsive WebGL, graceful degradation, multimodal reference parity |
| `deep-research/` | Iterative mixed-source research, synthesis, anti-hallucination recovery, M3 long-context compression |
| `incident-triage-harness/` | Production-style debugging and mitigation workflow, with M3 visual evidence handling |
| `minimax-multimodal-toolkit/` | MiniMax-native image, video, voice, music, and media routing (output side) |
| `minimax-m3-long-context/` | 1M-token MSA context discipline: retention, compression, skill handoff, closeout context disposition |
| `minimax-m3-multimodal-input/` | Native image/video input workflow: ground in the file, design parity, visual-fidelity claims |

> **Load a skill when** the task has a repeatable workflow too detailed for the core, needs examples or category heuristics, or benefits from progressive disclosure. M3's 1M context still rewards "load the on-point skill, do not preload the catalog."

---

## M3 Runtime Modes

MiniMax M3 (released 2026-06-01) is the target model for this repo. It ships a 1M-token MSA context window and native multimodal input (text, image, video). The repo is tuned for M3 first; it stays correct on third-party models such as `composer-2`, GPT, or Claude — the M3-specific sections (long-context discipline, multimodal input discipline) become inert and the always-on core continues to apply.

> When working in a model that is **not** M3, do not promise multimodal or 1M-context behavior. The model-selection guidance in `model-compatibility.mdc` is the source of truth for which capabilities the active model actually exposes.

---

## M3 + Cursor 3 Surface

A quick reference for the new surface — when to use each.

| Surface | When to use |
|---------|-------------|
| **Agents Window** | The default work surface (`Cmd+Shift+P → Agents Window`). Multi-workspace, multi-repo, parallel agents. |
| **`/worktree`** | Isolated git worktree. Use for risky exploration, parallel branches, anything that must not collide with the main tree. |
| **`/best-of-n`** | Run the same prompt across 2–4 models in parallel worktrees, then compare. Use for high-stakes architecture, design, or refactor decisions. |
| **`Await`** | Wait for a background shell, subagent, or a specific output token (`Ready`, `Error`). Use for long-running dev servers, parallel subagents, slow CLIs. |
| **MCP Apps structured content** | When an MCP tool returns structured content, prefer the structured form over prose dumping. |
| **Composer 2** | Cursor's own model — fast, cheap iteration, ~61.7 Terminal-Bench 2.0 at $0.50/$2.50 per MTok. |

> Tool names and command names can drift across Cursor builds. The decision still stands (use an isolated worktree for risky work; await long-running jobs; prefer structured MCP outputs); if a specific identifier is not exposed in your build, fall back to the next best exposed path.

---

## Where M3 Feels Different

Three areas separate M3 from a generic coding model — and the optional rules / skills deepen each without bloating the core:

- **1M-token MSA + long-context discipline** — explicit retention, compression, and skill-handoff rules, plus a dedicated `minimax-m3-long-context` skill.
- **Native multimodal input + `multimodal-grounded` verification** — image and video inputs ground visual claims; a dedicated `minimax-m3-multimodal-input` skill teaches the workflow.
- **Agent Teams on Cursor 3** — explicit roles, bounded handoffs (with environment + model fields), `/best-of-n` as a first-class team pattern, and `Await` for long-running branches.

---

## Model Compatibility

The rules are designed to survive model changes:

- the core rule stays short and durable
- runtime-specific guidance lives in requestable rules
- tool advice is written around whatever the environment actually exposes
- version-sensitive claims are verified at runtime, not frozen into the rules

The always-on core does not depend on a specific model — it teaches tool-first, read-before-edit, scope-controlled behavior that holds across M3, Composer 2, GPT, Claude, and other strong coding models. The M3-specific sections (long-context discipline, multimodal input discipline) are inert on models that do not expose those capabilities; the agent must not promise them.

---

## Design Principles

<table>
<tr>
<td width="50%" valign="top">

**Keep the core small**
Large always-on prompts waste context and often reduce execution quality. The core carries only durable, high-leverage behavior — including Code Discipline, so per-language cookbooks are unnecessary. M3-specific guidance (long-context, multimodal) lives as short sections, with depth in skills.

</td>
<td width="50%" valign="top">

**Prefer repo truth over training defaults**
Inspect manifests and CI first, match existing conventions, verify with the repo's own commands. Load architecture rules only when designing structure — not for everyday syntax.

</td>
</tr>
<tr>
<td width="50%" valign="top">

**Capability framing over persona framing**
"Inspect first, build the smallest proving slice, verify before claiming success" beats spending tokens on identity and self-description.

</td>
<td width="50%" valign="top">

**Make acceptance explicit**
Rules don't stop at "verify somehow" — they define the minimum proof per claim type, including `multimodal-grounded` for visual claims.

</td>
</tr>
<tr>
<td width="50%" valign="top">

**Trust the current environment**
Cursor's tool surface changes. Rules teach behavior that survives those changes instead of freezing old tool names.

</td>
<td width="50%" valign="top">

**No fabricated project metadata**
Never hand-write `.xcodeproj`, `project.pbxproj`, `.xcworkspace`, or complex `.sln`. Use the CLI/IDE, then work inside the real project.

</td>
</tr>
</table>

---

## Example Patterns

Want concrete M3-native patterns instead of only rules? Start here:

- [`examples/agent-teams-product-prototype.md`](examples/agent-teams-product-prototype.md) — a bounded planner / explorer / builder / verifier workflow with M3 + Cursor 3 handoff fields (environment, model) and `/best-of-n` + `Await` notes
- [`.cursor/skills/incident-triage-harness/SKILL.md`](.cursor/skills/incident-triage-harness/SKILL.md) — a large-skill example for incident-style debugging and mitigation, now with M3 visual-evidence handling
- [`.cursor/skills/incident-triage-harness/reference.md`](.cursor/skills/incident-triage-harness/reference.md) — companion reference showing progressive disclosure
- [`.cursor/skills/minimax-m3-long-context/SKILL.md`](.cursor/skills/minimax-m3-long-context/SKILL.md) — the 1M-context discipline skill
- [`.cursor/skills/minimax-m3-multimodal-input/SKILL.md`](.cursor/skills/minimax-m3-multimodal-input/SKILL.md) — the visual-input workflow skill

---

## AGENTS.md For Other IDEs and CLIs

`docs/AGENTS.md` is the portable, standalone version of M3 behavior for environments that use agent instruction files but don't support Cursor rules. It carries the core behavior directly instead of acting as a thin pointer.

It focuses on action-first execution, the reasoning protocol (intent-first, interleaved thinking, explicit hypotheses, end-to-end ownership), solver-loop thinking, scope control, read-before-edit discipline, root-cause-first code discipline with test integrity, proportional verification (including red → green for bug fixes), explicit status labels (including `multimodal-grounded`), M3 long-context discipline, M3 multimodal input discipline, current-source version discipline, CLI-first scaffolding, and concise communication.

> **To use it elsewhere:** copy `docs/AGENTS.md` into the target repo root as `AGENTS.md`. If you run both `AGENTS.md` and `.cursor/rules`, keep them aligned rather than letting them drift into contradictory layers.

---

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for contribution rules, the skill frontmatter contract (including the optional `model_assumptions` field), and placement guidance across always-on rules, requestable rules, and skills.

---

## References

<details open>
<summary><b>MiniMax M3</b></summary>

- [MiniMax M3 launch (VentureBeat)](https://venturebeat.com/technology/minimax-m3-debuts-eclipsing-gpt-5-5-and-gemini-3-1-pro-on-key-benchmark-performance-for-just-5-10-of-the-cost)
- [MiniMax M3 review (Thomas Wiegold)](https://thomas-wiegold.com/blog/minimax-m3-review/)
- [MiniMax Text Generation Docs](https://platform.minimax.io/docs/guides/text-generation)
- [MiniMax API Overview](https://platform.minimax.io/docs/api-reference/api-overview)
- [MiniMax Platform](https://platform.minimax.io)

</details>

<details>
<summary><b>Cursor 3 & others</b></summary>

- [Cursor 3 announcement](https://cursor.com/blog/cursor-3)
- [Cursor 3.0 changelog](https://cursor.com/changelog/3-0)
- [Agents Window docs](https://cursor.com/docs/agent/agents-window)
- [Cursor Changelog](https://cursor.com/changelog)
- [Cursor Rules Docs](https://cursor.com/docs/context/rules)
- [Cursor Agent Best Practices](https://cursor.com/blog/agent-best-practices)
- [OpenAI Codex Best Practices](https://developers.openai.com/codex/learn/best-practices/)
- [OpenAI Exec Plans](https://cookbook.openai.com/articles/codex_exec_plans)

</details>

---

<div align="center">

**Made with care by [Aris Setiawan](https://github.com/madebyaris) at [MiniMax](https://platform.minimax.io)**

<sub>If this sharpened your agent, consider leaving a star — it helps others find it.</sub>

</div>
