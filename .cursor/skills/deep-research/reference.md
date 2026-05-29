# Deep Research Reference

Detailed examples, strategies, and templates for the deep-research skill. The agent should read this file on-demand when facing ambiguous research types, unfamiliar patterns, or when generating formal reports.

---

## Query Decomposition Examples

### Comparison: "React vs Vue vs Svelte for enterprise dashboard"

```
Sub-queries:
  1. "React enterprise dashboard adoption performance 2026"
  2. "Vue.js enterprise dashboard large-scale production 2026"
  3. "Svelte enterprise dashboard production experience 2026"
  4. "frontend framework comparison criteria enterprise: bundle size, hiring, ecosystem, TypeScript"

Strategy: Parallel (all 4 are independent)
Tier: Standard (well-defined scope, 3 items to compare)
```

### Explanation: "How does Raft consensus algorithm handle leader election?"

```
Sub-queries:
  1. "Raft consensus algorithm overview leader election mechanism"
  2. "Raft leader election timeout split vote resolution"
  3. "Raft vs Paxos leader election differences"

Strategy: Sequential (start broad, then narrow based on what overview reveals)
Tier: Standard (technical depth needed, but focused topic)
```

### Investigation: "Why is our CI pipeline 3x slower since last month?"

```
Sub-queries (hypothesis-driven):
  Hypothesis A: Dependency changes increased install time
    -> use `Grep` for package or lockfile references in recent changes
  Hypothesis B: New test suite added significant runtime
    -> SemanticSearch for test configuration changes
  Hypothesis C: CI runner resource constraints changed
    -> read CI config files with `Read`, then search targeted symbols with `Grep`

Strategy: Parallel hypotheses, then sequential deep-dive on most likely
Tier: Standard (codebase-focused, bounded scope)
```

### Survey: "State of AI code generation tools in 2026"

```
Sub-queries:
  1. "AI code generation tools landscape 2026 overview"
  2. "GitHub Copilot vs Cursor vs Windsurf features comparison 2026"
  3. "open source AI coding assistants 2026"
  4. "AI code generation enterprise adoption challenges 2026"
  5. "AI code generation benchmarks accuracy 2026"
  6. "emerging AI coding tools startups 2026"

Strategy: Parallel (all independent), then sequential follow-ups on gaps
Tier: Exhaustive (broad landscape, many dimensions)
Task plan: launch 3 parallel `Task` investigations for queries 1-3, then 3 more for 4-6
```

### Fact-check: "Does HTTP/3 always outperform HTTP/2?"

```
Sub-queries:
  1. "HTTP/3 vs HTTP/2 performance benchmarks"
  2. "HTTP/3 disadvantages cases where HTTP/2 is faster"
  3. "HTTP/3 QUIC overhead high-latency networks"

Strategy: Sequential (need claim evidence first, then counter-evidence)
Tier: Quick (focused factual question)
```

---

## Research Type Decision Tree

When the research type is ambiguous, use this decision tree:

```
Does the user mention 2+ specific items to evaluate?
  YES -> Comparison
  NO  -> continue

Is the user asking "how" or "why" something works?
  YES -> Explanation
  NO  -> continue

Is there a specific problem, bug, or unexpected behavior?
  YES -> Investigation
  NO  -> continue

Is the user asking to verify a specific claim?
  YES -> Fact-check
  NO  -> continue

Is the scope broad (landscape, options, overview)?
  YES -> Survey
  NO  -> Default to Explanation
```

---

## Source Priority Matrix

| Research type | Primary source | Secondary source | Avoid |
|---------------|---------------|-----------------|-------|
| **Comparison** | Official docs, benchmarks | Community blog posts, HN/Reddit threads | Marketing pages |
| **Explanation** | Academic papers, official docs, RFCs | Tutorials, conference talks | Stack Overflow answers (often outdated) |
| **Investigation** | Codebase (`Grep`, `Read`, `SemanticSearch`) | Git history, CI logs | Generic web results |
| **Survey** | Industry reports, official announcements | Developer surveys, trend analyses | Individual opinion posts |
| **Fact-check** | Primary sources (papers, official docs) | Independent benchmarks | Social media, forums |

**When to use WebFetch after WebSearch:**
- The search snippet is promising but truncated
- You need specific numbers, code examples, or configuration details
- The source is a documentation page or technical blog with depth
- Do NOT WebFetch: social media, forums (search snippet is usually sufficient), or paywalled content

---

## Reflection Prompts (Detailed)

Use these at each reflection checkpoint. Pick the 2-3 most relevant for the current situation.

### Coverage assessment
- "Which of my original sub-queries can I now answer confidently?"
- "Are there dimensions I didn't anticipate that turned out to be important?"
- "Am I covering the topic breadth the user expects, or have I narrowed too early?"

### Confidence calibration
- "How many independent sources confirm my main findings?"
- "Are there any claims I'm treating as facts that come from a single informal source?"
- "Where do my sources disagree, and can I find a tiebreaker?"

### Diminishing returns check
- "Did my last 2 searches teach me anything I didn't already know?"
- "Am I searching for the same thing with different keywords?"
- "Would another search change my recommendation or conclusion?"

### Pivot detection
- "Has anything I found invalidated my original research plan?"
- "Is there a better framing of the question based on what I've learned?"
- "Should I split a sub-query that turned out to be more complex than expected?"

### Sufficiency test
- "If I had to write the report right now, what would be missing?"
- "Would a domain expert find obvious gaps in my coverage?"
- "Is the remaining uncertainty acceptable for the user's purpose?"

---

## Common Failure Modes

### 1. Context Bloat

**Symptom**: Raw search results accumulate, pushing important earlier context out of the window.

**Prevention**: Compress every search result immediately. Never carry forward full page contents. Use the evolving summary pattern -- update it, don't append to it.

**Recovery**: If context is already bloated, write a fresh evolving summary from memory of key findings, discard everything else, and continue.

### 2. Tunnel Vision

**Symptom**: Deep-diving into one sub-query while neglecting others. Over-researching a tangent.

**Prevention**: The reflection checkpoint forces periodic assessment of ALL sub-queries, not just the current one. The TodoWrite tracker makes gaps visible.

**Recovery**: Stop the current sub-query even if incomplete. Assess all sub-queries. Redistribute remaining search budget to the most important gaps.

### 3. Search Repetition

**Symptom**: Same information coming back from multiple searches with slightly different keywords.

**Prevention**: After 2 searches returning similar results, that sub-query is answered. Move on.

**Recovery**: Explicitly note "this sub-query is saturated" and redirect searches to unanswered questions.

### 4. Authority Confusion

**Symptom**: Treating all sources as equally reliable. Blog posts weighted the same as official docs.

**Prevention**: The compression template includes a confidence field. Always note whether a source is official documentation, peer-reviewed research, community content, or informal discussion.

**Recovery**: For any finding marked "uncertain", search specifically for an authoritative source to confirm or deny.

### 5. Scope Creep

**Symptom**: Research keeps expanding as new interesting tangents emerge. Never reaches synthesis.

**Prevention**: The research brief defines "out of scope" explicitly. The tier sets a search budget. Exhaustive tier has a hard cap of ~15 searches before mandatory synthesis.

**Recovery**: Return to the research brief. Ask: "Does this new tangent serve the original question?" If not, mention it as a "further reading" suggestion but don't research it.

### 6. Premature Synthesis

**Symptom**: Jumping to conclusions after 1-2 searches without checking alternative viewpoints.

**Prevention**: The reflection checkpoint requires checking for contradictions and alternative perspectives before declaring sufficiency. Minimum of 2 independent sources for any high-confidence claim.

**Recovery**: Before synthesizing, explicitly search for counter-evidence: "[main finding] criticism", "[main finding] limitations", "[main finding] alternatives".

---

## Anti-Hallucination & Failure Recovery

The six modes above are process-hygiene failures. These are the more dangerous ones for a research output that feeds code or decisions: inventing facts and trusting bad sources. The standard is honesty by construction -- every asserted fact is traceable to a source, and anything unverified is labeled as such.

### 1. Fabricated APIs / signatures / versions

**Symptom**: Asserting a function name, method signature, config flag, CLI option, or version number from memory -- the single most damaging research failure for a coding agent, because it looks authoritative and compiles into a bug.

**Prevention**:
- Never state an API, signature, flag, or version as current from memory. Confirm it against the official docs, the package's own README, or the installed source before asserting it.
- For "what's the current version / latest syntax" questions, treat memory as a hypothesis to verify, not an answer.
- Distinguish "this is how it worked in a version I remember" from "this is how it works now."

**Recovery**: If a search cannot confirm the specific API/version, drop the specific claim. Either (a) cite the doc page that does cover it, (b) state the general approach without the exact identifier, or (c) label it `unverified` and name the exact check (doc page, `package.json`, type definitions) that would resolve it.

### 2. Bad or misattributed citations

**Symptom**: A citation that does not resolve (404 / wrong URL), or a real source that does not actually support the claim attached to it. Fabricated or "close enough" URLs are a hallucination even when the underlying fact is true.

**Prevention**:
- Only cite a URL you actually fetched or that came back in search results -- never construct a plausible-looking link from memory.
- Before attributing a claim to a source, confirm the source's content actually states it (the search snippet or fetched page, not the title alone).

**Recovery**: Remove or replace any citation you cannot stand behind. If the fact is real but the source is uncertain, search specifically for the authoritative source, or mark the claim `unverified`.

### 3. Dead-end / no-signal loops

**Symptom**: Repeated searches return nothing usable, or every result is low-quality / contradictory, and the loop continues with no new information.

**Prevention**: Apply the stop conditions from the core loop. After two reformulations of the same sub-query with no usable signal, that path is exhausted.

**Recovery**: Stop searching that path. Report what was tried and what is missing, then escalate with ONE concrete forked question to the user (e.g. "I can't find an authoritative source for X; do you have a preferred doc, or should I proceed on the most-cited community answer and flag it?") rather than burning budget on more variations. This mirrors the repo's stuck-loop policy: after two failed attempts on the same hypothesis, change strategy instead of repeating it.

### 4. Confidence honesty (label, don't imply)

**Symptom**: Presenting single-source, dated, or inferred claims with the same certainty as well-corroborated ones.

**Prevention**: Map every finding to an explicit status before it enters the report:

| Status | Meaning | Use when |
|--------|---------|----------|
| `verified` | Confirmed against an authoritative source (or 2+ independent sources) | Official docs, RFC, multiple converging sources |
| `unverified` | Plausible but not confirmed; the proving check was not run | Single informal source, or memory not yet checked |
| `assumption` | Depends on inference, not direct evidence | Reasoning across sources, filling a gap |

**Recovery**: Before synthesis, downgrade any claim whose evidence does not match its asserted confidence, and surface the `unverified` / `assumption` items in the report's confidence assessment rather than hiding them in the prose.

---

## Output Templates

### Quick Tier -- Concise Answer

```markdown
## [Question restated as heading]

[2-4 paragraph answer with inline citations]

**Key takeaway**: [1 sentence summary]

**Sources**:
1. [Title](URL)
2. [Title](URL)
```

### Standard Tier -- Structured Analysis

```markdown
## [Research topic]

### Overview
[1-2 paragraph summary of the landscape / answer]

### [Dimension 1]
[Detailed findings with citations]

### [Dimension 2]
[Detailed findings with citations]

### [Dimension 3]
[Detailed findings with citations]

### Recommendations
[Actionable conclusions based on findings]

### Confidence Assessment
- **High confidence**: [well-supported claims]
- **Moderate confidence**: [single-source or indirect evidence]
- **Needs verification**: [uncertain areas]

### Sources
1. [Title](URL) -- [brief description of what it contributed]
2. [Title](URL) -- [brief description]
...
```

### Standard Tier -- Comparison Table

```markdown
## [Item A] vs [Item B] vs [Item C]

### Quick Comparison

| Criterion | Item A | Item B | Item C |
|-----------|--------|--------|--------|
| [Criterion 1] | ... | ... | ... |
| [Criterion 2] | ... | ... | ... |
| [Criterion 3] | ... | ... | ... |

### Detailed Analysis

#### [Item A]
[Strengths, weaknesses, best suited for...]

#### [Item B]
[Strengths, weaknesses, best suited for...]

#### [Item C]
[Strengths, weaknesses, best suited for...]

### Recommendation
[When to choose each, based on context]

### Sources
...
```

### Exhaustive Tier -- Full Research Report

```markdown
## [Research Topic]: A Comprehensive Analysis

### Executive Summary
[3-5 sentences capturing the most important findings and recommendations]

### Background
[Context needed to understand the research question]

### Methodology
[Brief note on sources consulted and approach taken]

### Findings

#### [Section 1: Major theme]
[Detailed findings with citations]

#### [Section 2: Major theme]
[Detailed findings with citations]

#### [Section 3: Major theme]
[Detailed findings with citations]

### Analysis
[Cross-cutting insights, trends, contradictions resolved]

### Recommendations
[Numbered, actionable items]

### Limitations
[What this research did NOT cover, known gaps, areas needing further investigation]

### Confidence Assessment
- **High confidence**: [list]
- **Moderate confidence**: [list]
- **Needs verification**: [list]

### Sources
[Numbered list with URLs and brief descriptions]
```

### Investigation Report

```markdown
## Investigation: [Problem Statement]

### Hypothesis
[What we suspected]

### Evidence

#### Supporting evidence
- [Finding 1 with source]
- [Finding 2 with source]

#### Contradicting evidence
- [Finding 3 with source]

### Root Cause
[Determined cause based on evidence]

### Recommended Fix
[Actionable steps]

### Verification
[How to confirm the fix works]
```

### Fact-Check Report

```markdown
## Fact-check: "[Claim being checked]"

**Verdict**: [Confirmed / Partially True / False / Unverifiable]

### Evidence For
- [Source and what it says]

### Evidence Against
- [Source and what it says]

### Context
[Nuance that affects the verdict]

### Sources
...
```
