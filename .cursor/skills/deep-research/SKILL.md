---
name: deep-research
description: Conducts multi-step deep research on any topic using iterative search, reflection, and synthesis. Use when the user asks to research, investigate, survey, compare, analyze, deep-dive, or explore a topic in depth. Covers web research, codebase analysis, documentation review, mixed-source investigation, and M3 long-context compression discipline.
license: MIT
metadata:
  version: "1.2.0"
  category: research
  sources:
    - Cursor-native tool workflows
    - Documentation review and comparative research practice
    - Repo and web synthesis patterns
  model_assumptions:
    - long-context: recommended
---

# Deep Research

Conduct thorough, multi-step research using an iterative loop of search, compress, reflect, and synthesize. Works with any Cursor-supported model.

## Effort Scaling

Before starting, calibrate depth to the question:

| Tier | When | Searches | Delegation (`Task`) | Output |
|------|------|----------|---------------------|--------|
| **Quick** | Focused factual question, single concept | 2-3 | None | Concise answer with sources |
| **Standard** | Multi-faceted topic, comparison, how-something-works | 5-8 | None | Structured analysis with sections |
| **Exhaustive** | Comprehensive survey, architecture decision, landscape review | 10+ | Parallel `Task` investigations | Full report with citations |

```
Calibration:
  Question complexity: [single-fact / multi-faceted / comprehensive]
  Source diversity needed: [one source type / mixed]
  User expectation: [quick answer / detailed analysis / full report]
  -> Tier: [Quick / Standard / Exhaustive]
```

---

## Phase 0: Scope

Immediately classify the research request before any searching.

**Step 1 -- Classify research type:**

| Type | Signal | Example |
|------|--------|---------|
| **Comparison** | "vs", "compare", "which is better", "difference between" | "React vs Vue for enterprise apps" |
| **Explanation** | "how does", "what is", "explain", "why does" | "How does Raft consensus work?" |
| **Investigation** | "debug", "find out why", "what caused", "root cause" | "Why is our build 3x slower?" |
| **Survey** | "landscape", "options for", "state of", "overview" | "State of CSS-in-JS in 2026" |
| **Fact-check** | "is it true", "verify", "confirm" | "Does React 19 still need keys?" |

**Step 2 -- Determine sources:**

| Source | When to use |
|--------|-------------|
| `WebSearch` + `WebFetch` | General knowledge, current events, library docs, community solutions |
| `SemanticSearch` + `Grep` + `Read` | Codebase-specific questions, internal patterns, project architecture |
| Mixed | "How should we implement X?" (need both external best practices and internal conventions) |

**Step 3 -- Generate a one-paragraph research brief:**

```
Research brief:
  Question: [exact user question]
  Type: [comparison / explanation / investigation / survey / fact-check]
  Sources: [web / codebase / mixed]
  Tier: [quick / standard / exhaustive]
  Key dimensions to cover: [list 3-5 specific aspects]
  Out of scope: [anything explicitly excluded]
```

Do NOT present this brief to the user. Proceed to Phase 1 immediately.

---

## Phase 1: Plan

Decompose the research brief into concrete sub-queries.

**Decomposition strategy by type:**

- **Comparison**: One sub-query per item being compared, plus one for the comparison criteria
- **Explanation**: Start broad (overview), then narrow (mechanism, edge cases, alternatives)
- **Investigation**: Hypothesis-first -- form 2-3 hypotheses, create sub-queries to test each
- **Survey**: One sub-query per category/dimension in the landscape
- **Fact-check**: One sub-query for the claim, one for counter-evidence, one for authoritative source

**For Standard/Exhaustive tier**, create a TodoWrite tracker:

```
TodoWrite(todos=[
  { id: "DR-scope", content: "Research: [brief summary]", status: "completed" },
  { id: "DR-q1", content: "Sub-query: [first sub-query]", status: "in_progress" },
  { id: "DR-q2", content: "Sub-query: [second sub-query]", status: "pending" },
  ...
  { id: "DR-synth", content: "Synthesize findings into report", status: "pending" }
], merge=false)
```

**For Exhaustive tier**, evaluate which sub-queries are independent (can run in parallel via `Task`) vs. dependent (must run sequentially because results inform next query).

---

## Phase 2: Research Loop

This is the core iterative cycle. Execute it per sub-query.

### Search

**Web research pattern:**
```
1. WebSearch(search_term="[specific, well-formed query] [current year if recency matters]")
2. If a result looks highly relevant, WebFetch the full page
3. Immediately compress: extract only the facts relevant to the sub-query
```

**Codebase research pattern:**
```
1. SemanticSearch(query="[natural language question]", target_directories=[relevant dir])
2. If results point to specific files, read them with `Read`
3. If searching for exact symbols, use `Grep`
4. Compress: extract the pattern/answer, not the full file contents
```

**Parallel Task pattern (Exhaustive tier only):**
```
Launch up to 3 parallel `Task` investigations for independent sub-queries:

Task(
  subagent_type="generalPurpose",
  model="fast",
  readonly=true,
  description="Research [topic]",
  prompt="Research the following question and return a compressed summary with sources:
    Question: [sub-query]
    Search using WebSearch and WebFetch. Return:
    1. Key findings (bullet points)
    2. Sources (title + URL for each)
    3. Confidence: certain / likely / uncertain
    Do NOT return raw search results. Summarize.",
)
```

### Compress (after EVERY search)

Do NOT accumulate raw search results. After each search or WebFetch:

```
Compression template:
  Source: [URL or file path]
  Key finding: [1-3 sentences of relevant information]
  Confidence: [certain / likely / uncertain]
  Relevance: [directly answers sub-query / provides context / tangential]
```

Drop tangential results immediately. Only carry forward "directly answers" and "provides context" findings.

**M3 nudge:** with a 1M-token context, the failure mode shifts from "ran out of room" to "kept too much raw output." Apply the compression template aggressively. If you have run 3+ searches without compressing, the next reflection must include a compression pass. See `minimax-m3-long-context` for the broader retention/discard plan.

### Reflect (after every 2-3 searches)

Pause and evaluate using this checklist:

```
Reflection checkpoint:
  1. Coverage: Which sub-queries are answered? Which have gaps?
  2. Confidence: Am I seeing convergence across sources, or contradictions?
  3. Diminishing returns: Are my last 2 searches finding new information, or repeating what I already know?
  4. Pivots needed: Has anything I found changed what I should be searching for?
  5. Sufficiency: Can I answer the original question with what I have?

  Decision: [continue searching / pivot strategy / proceed to synthesis]
```

**Stop searching when:**
- 3+ independent sources confirm the same finding
- Last 2 searches returned no new information
- All sub-queries are answered at the target confidence level
- Maximum search budget for the tier is reached

**Pivot when:**
- Initial hypothesis was wrong -- reformulate sub-queries
- A new dimension emerged that the original plan missed -- add a sub-query
- Sources contradict each other -- search for authoritative tiebreaker

### Evolving Summary

Maintain a running summary that gets updated (not appended to) after each reflection:

```
Working summary (updated, not appended):
  [Paragraph 1: What I know with high confidence]
  [Paragraph 2: What I know with moderate confidence]
  [Paragraph 3: Open questions / contradictions / gaps]
  Sources so far: [numbered list]
```

This is the "evolving report as memory" pattern. Previous raw search results can be released from active context once compressed into this summary.

---

## Phase 3: Synthesize

Generate the final output in a SINGLE pass from the evolving summary and compressed findings.

**Do NOT:**
- Generate sections independently and merge them (produces disjointed output)
- Copy-paste raw search results into the report
- Include findings you flagged as "tangential" during compression

**Do:**
- Write the full response in one coherent pass
- Resolve contradictions explicitly ("Source A claims X, while Source B claims Y. Based on [reasoning], Y is more credible because...")
- Organize with clear headings for Standard/Exhaustive tier
- Include inline citations: `[Source Title](URL)` or file path references

**Structure by research type:**

- **Comparison**: Table or side-by-side, then analysis of tradeoffs, then recommendation
- **Explanation**: Overview, then mechanism/details, then edge cases/caveats
- **Investigation**: Hypothesis, evidence for/against, conclusion
- **Survey**: Categories, key players/options per category, trends, recommendations
- **Fact-check**: Claim, evidence, verdict (confirmed/partially true/false/unverifiable)

---

## Phase 4: Deliver

### Citation Format

Every factual claim must have a source. Use inline links:
```
React Server Components reduce bundle size by up to 30% [React Blog](https://react.dev/blog/...).
```

For codebase findings, cite file paths:
```
The auth middleware uses JWT validation (`src/middleware/auth.ts:42-58`).
```

### Confidence Flags

Honesty by construction: never assert an API, version, or fact from memory as current, and never cite a URL you did not actually retrieve. Label each finding `verified` / `unverified` / `assumption`, and if a path yields no usable signal after two reformulations, stop and escalate with one concrete question rather than looping. See the Anti-Hallucination & Failure Recovery section in [reference.md](reference.md).

End the report with an honest assessment:

```
Confidence assessment:
  - High confidence: [claims well-supported by multiple sources]
  - Moderate confidence: [claims from single authoritative source]
  - Low confidence / needs verification: [claims from informal sources or with contradictions]
```

### Mark Completion

Update TodoWrite to mark all research sub-queries and synthesis as completed.

---

## Model Compatibility

This skill uses only Cursor-native tools and plain behavioral instructions:
- No model-specific prompting syntax
- No assumptions about thinking/reasoning format
- Tool names in this skill are **illustrative**; **use the exact identifiers and schemas** from the active session. In Composer-style Cursor agents you will typically see `Read`, `Grep`, `StrReplace`, `Task` (delegation), `WebSearch`, `WebFetch`, `SemanticSearch`, `TodoWrite`, and others—names differ in older docs or other products (`ReadFile`, `ApplyPatch`, `Subagent`, etc.)
- Reflection happens in whatever reasoning mechanism the model supports

The iterative search-compress-reflect loop is a behavioral pattern, not a code construct. Any model that can call tools and reason about results can execute it.

---

## Quick Reference

```
SCOPE  -> Classify type + sources + tier (no searching yet)
PLAN   -> Decompose into sub-queries, create tracker
SEARCH -> Execute queries, compress each result immediately
REFLECT -> Every 2-3 searches: coverage? gaps? pivot? stop?
SYNTH  -> One-shot report from compressed findings
DELIVER -> Citations, confidence flags, completion
```

## Additional Resources

- For detailed examples, process failure modes, and the anti-hallucination / failure-recovery layer (fabricated APIs, bad citations, dead-end loops, confidence honesty), see [reference.md](reference.md)
