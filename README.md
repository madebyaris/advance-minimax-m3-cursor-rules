<div align="center">

# ⚡ MiniMax M2.7 Cursor Rules

#### A durable execution spine for repo-scale engineering, agent teams, deep skills, and dynamic tool use.

[![Stars](https://img.shields.io/github/stars/madebyaris/advance-minimax-m2-cursor-rules?style=flat-square&color=8b5cf6)](https://github.com/madebyaris/advance-minimax-m2-cursor-rules/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![Cursor 3](https://img.shields.io/badge/Tested-Cursor%203-blue?style=flat-square)](https://cursor.com/blog/cursor-3)
[![MiniMax M2.7](https://img.shields.io/badge/MiniMax-M2.7-8b5cf6?style=flat-square)](https://platform.minimax.io)
[![Any Model](https://img.shields.io/badge/Compatible-Any%20Model-22c55e?style=flat-square)](#-model-compatibility)

<br/>

![Always-On Rules](https://img.shields.io/badge/Always--On-2_rules-0f172a?style=for-the-badge)
![Requestable Rules](https://img.shields.io/badge/Requestable-16_rules-1e293b?style=for-the-badge)
![Skills](https://img.shields.io/badge/Skills-5_packs-14b8a6?style=for-the-badge)

<br/>

*Built for **MiniMax M2.7**, aligned with the official release and API docs, and written to stay useful across model changes.*

<sub>

[Quick Start](#-quick-start) · [Why This Repo](#-why-this-repo-exists) · [Architecture](#-rule-architecture) · [Runtime Modes](#-m27-runtime-modes) · [Solver Loop](#-the-solver-loop) · [AGENTS.md](#-agentsmd-for-other-ides-and-clis) · [References](#-references)

</sub>

</div>

---

## ✨ At A Glance

| | What you get |
|---|---|
| 🧠 **Lean always-on core** | Two durable rules carry the execution spine — solver loop, scope control, code discipline, and a strict proof contract. No persona bloat. |
| 🧩 **Progressive depth** | 16 requestable rules + 5 skill packs load only when the task needs them, so context stays clean. |
| 🛠️ **Honest tool use** | The agent works the *current* runtime — no invented tools, no stale wrappers, no promises before the path is confirmed. |
| ✅ **Evidence-backed closeouts** | Explicit status labels (`verified` / `unverified` / `blocked`) and minimum-proof rules per change type. |
| 🌐 **Portable** | `docs/AGENTS.md` carries the same behavior to non-Cursor IDEs and CLIs. |
| 🔁 **Model-resilient** | Tuned for M2.7 first, compatible with any Cursor-supported model. |

> **The bet:** MiniMax doesn't get better from persona text. It gets better from cleaner context, smaller proving slices, better tool routing, and honest verification. Every rule here optimizes for that.

---

## 🚀 Quick Start

### For Cursor

```bash
git clone https://github.com/madebyaris/advance-minimax-m2-cursor-rules.git
cp -r advance-minimax-m2-cursor-rules/.cursor your-project/.cursor
```

That's it. Two rules are **always on**:

- `.cursor/rules/minimax-m2-core.mdc` — execution behavior
- `.cursor/rules/minimax-m2-status-verification.mdc` — status & proof contract

Everything else is **requestable** and narrower by design — it loads when the task or file globs call for it.

> The official docs recommend Anthropic-compatible access for MiniMax text models, and also support OpenAI-compatible access paths. See [MiniMax text generation docs](https://platform.minimax.io/docs/guides/text-generation) · [MiniMax API overview](https://platform.minimax.io/docs/api-reference/api-overview).

### For Other IDEs and CLIs

Copy `docs/AGENTS.md` into the target repo root as `AGENTS.md`. It lives under `docs/` here on purpose, so Cursor does not auto-activate it while you edit these rules.

---

## 🗂️ Repository Layout

```text
.cursor/
├── rules/                         # 18 rules (2 always-on + 16 requestable)
│   ├── minimax-m2-core.mdc                  ★ always-on · execution spine
│   ├── minimax-m2-status-verification.mdc   ★ always-on · proof contract
│   └── …                                    requestable: runtime + domain
└── skills/                        # 5 deep, structured skill packs
    ├── anti-slop-design/
    ├── 3d-web-experiences/
    ├── deep-research/
    ├── incident-triage-harness/
    └── minimax-multimodal-toolkit/
docs/
└── AGENTS.md                      # portable agent contract (non-Cursor)
examples/
└── agent-teams-product-prototype.md
```

---

## 🎯 Why This Repo Exists

This repo makes MiniMax M2.7 feel strong exactly where the official release puts its emphasis:

- repo-scale and end-to-end engineering
- agent harnesses and multi-agent collaboration
- long skill packs and detailed tool contracts
- dynamic tool discovery in changing environments
- proportional verification with evidence-backed closeouts

The goal is **not** to make MiniMax imitate another provider's tone. It is to give M2.7 a durable execution spine that complements its official positioning around real-world engineering, complex skills, and agent workflows.

<details>
<summary><b>Why M2.7-native (and what that optimizes for)</b></summary>

<br/>

MiniMax positions M2.7 as strong at real-world software engineering, full project delivery, large skill adherence, and agent teams — rather than only one-shot code generation ([release report](https://www.minimax.io/news/minimax-m27-en) · [model page](https://www.minimax.io/models/text/m27)).

So this repo optimizes for:

- bounded repo exploration instead of reading everything
- smallest proving slices for large tasks
- explicit role and handoff discipline for multi-agent work
- strong skill contracts instead of vague long prompts
- truthful runtime and verification reporting

</details>

<details>
<summary><b>The MoE note — what you can and cannot control</b></summary>

<br/>

These rules do **not** assume you can steer a model's internal MoE routing through persona text.

The controllable levers are:

- cleaner context
- better decomposition
- better tool routing
- better verification loops
- clearer definitions of done

If MiniMax performs better after a prompt rewrite, the likely reason is improved external problem structure — not magic access to hidden experts.

</details>

---

## 🔁 The Solver Loop

The single most important behavior this repo transfers into M2.7:

```text
1. Define the outcome in operational terms.
2. Inspect the repo and runtime before deciding.
3. Find the spine: entry points, data flow, state, persistence, user-visible behavior.
4. Build the smallest vertical slice that proves the feature works.
5. Verify at the surface where the user experiences the change.
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

> **Example —** for "build a task app", prioritize `create → list → complete → persist → reload`. Delay filters, collaboration, settings, and animations until the core path works.

---

## ✅ Execution Guarantees

A few behaviors the repo treats as non-negotiable:

- New packages, frameworks, and toolchains are checked against current authoritative sources **before** they are recommended or installed.
- Scaffolding uses the framework's official CLI / `create` / `init` path when one exists.
- Scaffold output is inspected before continuing.
- Runnable work is not "done" until there is **runnable proof**, not just static confidence.
- If a required check fails or is skipped, the agent reports `blocked` or `implemented but unverified` — never a false completion.
- Browser or user-surface verification is required for UI and interaction claims.
- Tool-based promises wait until the runtime path is confirmed.

---

## 🏗️ Rule Architecture

The system is layered: a tiny always-on core, runtime rules that load on demand, and domain rules that attach via file globs. Depth lives in skills.

### ★ Always-On Core

| File | Purpose |
|------|---------|
| `minimax-m2-core.mdc` | Durable execution behavior: solver loop, scope control, **code discipline**, truthful tool use, scaffold discipline, concise progress |
| `minimax-m2-status-verification.mdc` | Status & proof contract: exact claim labels, proof matching, evidence-first closeouts |

### ⚙️ Runtime Rules

| File | Purpose |
|------|---------|
| `model-compatibility.mdc` | Prompt hierarchy, tool discipline, context control across models |
| `cursor-tools-mastery.mdc` | Current tool-selection patterns inside Cursor |
| `cursor-mcp-optimization.mdc` | Browser, Figma, and Cloudflare tools with direct-action patterns |
| `cursor-agent-orchestration.mdc` | Planning, subagents, and multi-step coordination |
| `agent-teams.mdc` | Role boundaries, handoffs, escalation, serial vs parallel teams |
| `tool-discovery.mdc` | Runtime tool inventory, MCP/schema discovery, safe fallbacks |
| `minimax-mcp-tools.mdc` | Current-doc, web, and MCP/plugin lookup guidance |
| `minimax-m2-verification.mdc` | Proportional verification playbook (shell + browser checks) |
| `minimax-m2-self-evolution.mdc` | Iterative refinement loops and autonomous debugging |
| `skill-authoring.mdc` | When to use skills, how to structure them, how to avoid bloat |
| `clarify-first-prompting.mdc` | Ask only on real forks, after inspecting first |

### 🧱 Domain Rules

Requestable rules for cross-cutting domains — **not** per-language cookbooks. Language-specific idioms come from reading the repo, official docs, and the always-on **Code Discipline** section.

| File | Purpose |
|------|---------|
| `language-agnostic-patterns.mdc` | SOLID, design patterns, change discipline, code-review heuristics |
| `design-systems.mdc` | Tokens, shadcn/ui, Tailwind v4 mechanics → aesthetics via `anti-slop-design` |
| `3d-graphics.mdc` | Three.js / R3F syntax, container sizing, import traps → quality via `3d-web-experiences` |
| `devops-infrastructure.mdc` | Docker, k8s, Terraform, CI/CD — validate-before-apply, infra traps (lean) |
| `mobile-cross-platform.mdc` | Flutter / RN / Expo — CLI-first, architecture, mobile verify (lean) |

### 🧩 Skills

Skills keep deep, domain-specific procedures out of the always-on core, then deliver large structured guidance through progressive disclosure (`SKILL.md` + optional `reference.md`).

| Skill | Purpose |
|------|---------|
| `anti-slop-design/` | Category-aware design direction, anti-slop checks, UI polish |
| `3d-web-experiences/` | Aesthetic direction, performance budgets, responsive WebGL, graceful degradation |
| `deep-research/` | Iterative mixed-source research, synthesis, anti-hallucination recovery |
| `incident-triage-harness/` | Production-style debugging and mitigation workflow |
| `minimax-multimodal-toolkit/` | MiniMax-native image, video, voice, music, and media routing |

> **Load a skill when** the task has a repeatable workflow too detailed for the core, needs examples or category heuristics, or benefits from progressive disclosure.

---

## ⚡ M2.7 Runtime Modes

The official API exposes both `MiniMax-M2.7` and `MiniMax-M2.7-highspeed`, each with a **204,800**-token context window. The docs describe standard M2.7 at roughly **60 tps** and highspeed at roughly **100 tps**, with highspeed positioned as the same capability profile at lower latency ([text generation docs](https://platform.minimax.io/docs/guides/text-generation) · [API overview](https://platform.minimax.io/docs/api-reference/api-overview)).

| Model | Best fit |
|------|---------|
| `MiniMax-M2.7` | Deep repo work, complex synthesis, richer multi-step tasks |
| `MiniMax-M2.7-highspeed` | Faster interactive loops, shorter verification cycles, lower-latency coding |

---

## 🔬 Where M2.7 Feels Different

Three areas separate M2.7 from a generic coding model — and the optional rules deepen each without bloating the core:

- **🤝 Agent Teams** — explicit roles, bounded handoffs, clear escalation points instead of vague multi-agent optimism.
- **🧩 Skills** — long, high-signal contracts rather than rare workflows stuffed into the always-on prompt.
- **🔎 Tool Discovery** — discover the live runtime surface, schemas, and MCP shape before promising capability.

---

## 🧭 Model Compatibility

The rules are designed to survive model changes:

- the core rule stays short and durable
- runtime-specific guidance lives in requestable rules
- tool advice is written around whatever the environment actually exposes
- version-sensitive claims are verified at runtime, not frozen into the rules

This makes the repo useful for MiniMax first, while staying compatible with other Cursor-supported models.

---

## 📐 Design Principles

<table>
<tr>
<td width="50%" valign="top">

**Keep the core small**
Large always-on prompts waste context and often reduce execution quality. The core carries only durable, high-leverage behavior — including Code Discipline, so per-language cookbooks are unnecessary.

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
Rules don't stop at "verify somehow" — they define the minimum proof per claim type, especially for new scaffolds and user-facing behavior.

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

## 🧪 Example Patterns

Want concrete M2.7-native patterns instead of only rules? Start here:

- [`examples/agent-teams-product-prototype.md`](examples/agent-teams-product-prototype.md) — a bounded planner / explorer / builder / verifier workflow for multi-agent product work
- [`.cursor/skills/incident-triage-harness/SKILL.md`](.cursor/skills/incident-triage-harness/SKILL.md) — a large-skill example for incident-style debugging and mitigation
- [`.cursor/skills/incident-triage-harness/reference.md`](.cursor/skills/incident-triage-harness/reference.md) — companion reference showing progressive disclosure

---

## 📦 AGENTS.md For Other IDEs and CLIs

`docs/AGENTS.md` is the portable, standalone version of M2.7 behavior for environments that use agent instruction files but don't support Cursor rules. It carries the core behavior directly instead of acting as a thin pointer.

It focuses on action-first execution, solver-loop thinking, scope control, read-before-edit discipline, proportional verification, explicit status labels, current-source version discipline, CLI-first scaffolding, and concise communication.

> **To use it elsewhere:** copy `docs/AGENTS.md` into the target repo root as `AGENTS.md`. If you run both `AGENTS.md` and `.cursor/rules`, keep them aligned rather than letting them drift into contradictory layers.

---

## 🤝 Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for contribution rules, the skill frontmatter contract, and placement guidance across always-on rules, requestable rules, and skills.

---

## 📚 References

<details open>
<summary><b>MiniMax</b></summary>

- [MiniMax M2.7 Release Report](https://www.minimax.io/news/minimax-m27-en)
- [MiniMax M2.7 Model Page](https://www.minimax.io/models/text/m27)
- [MiniMax Text Generation Docs](https://platform.minimax.io/docs/guides/text-generation)
- [MiniMax API Overview](https://platform.minimax.io/docs/api-reference/api-overview)
- [MiniMax Platform](https://platform.minimax.io)

</details>

<details>
<summary><b>Cursor & others</b></summary>

- [Cursor Changelog](https://cursor.com/changelog)
- [Cursor Rules Docs](https://cursor.com/docs/context/rules)
- [Cursor Agent Best Practices](https://cursor.com/blog/agent-best-practices)
- [OpenAI Codex Best Practices](https://developers.openai.com/codex/learn/best-practices/)
- [OpenAI Exec Plans](https://cookbook.openai.com/articles/codex_exec_plans)

</details>

---

<div align="center">

**Made with care by [Aris Setiawan](https://github.com/madebyaris) at [MiniMax](https://minimax.io)**

<sub>If this sharpened your agent, consider leaving a ⭐ — it helps others find it.</sub>

</div>
