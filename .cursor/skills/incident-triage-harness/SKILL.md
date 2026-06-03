---
name: incident-triage-harness
description: Production-style incident triage workflow for logs, metrics, code, safe mitigations, and M3 multimodal visual evidence (screenshots, screen recordings). Use when debugging alerts, regressions, outages, or suspicious runtime behavior.
license: MIT
metadata:
  version: "1.1.0"
  category: debugging
  sources:
    - Incident response and SRE triage practice
    - Evidence-first debugging workflows
    - Production mitigation and verification patterns
  model_assumptions:
    - multimodal-input: recommended
---

# Incident Triage Harness

Investigate production-style failures with an evidence-first loop: confirm symptoms, narrow the blast radius, correlate signals, inspect code, and prove the smallest safe mitigation.

## When to Use

- User asks to debug an outage, incident, alert, regression, or mysterious failure
- Logs, traces, deployments, migrations, config drift, or runtime behavior are involved
- You need a structured loop for "hypothesis -> check -> narrow -> mitigate -> verify"

**For deeper prompts, evidence templates, and mitigation checklists**, also read `reference.md` in this skill directory.

---

## Step 0: Triage The Situation

Before doing anything else, identify:

1. **User-visible symptom**: What is broken right now?
2. **Blast radius**: Which route, job, service, or user segment is affected?
3. **Recent change surface**: Deploys, migrations, feature flags, config changes, dependency bumps
4. **Available evidence**: logs, traces, dashboards, DB data, repo history, local repro, tests

Do not jump into code edits until you have at least one concrete failure hypothesis.

### Step 0a: Visual Evidence (M3)

When the user attaches a screenshot of a broken UI, a screen recording of the failure, or a short clip of the symptom, the visual is primary evidence — not a supplement.

- Read the actual file in the current session. Quote the visible text (error message, broken layout, empty state) directly in the report.
- Name the file path in the closeout; do not describe the image from memory.
- For a UI regression, treat the screenshot as the "what is broken" input. Treat a re-rendered post-fix frame as the "what is fixed" proof (`multimodal-grounded`).
- For animation / interaction bugs, prefer a short clip over a single frame; cite the timestamp region of the relevant behavior.

---

## Step 1: Evidence Loop

Use this sequence:

```text
1. Confirm the symptom
2. Correlate recent changes with the failure window
3. Form the smallest plausible hypothesis
4. Check the hypothesis with the strongest available evidence
5. Narrow the cause before changing code
6. Prefer safe mitigation before broad refactors
7. Verify the mitigation at the affected surface
```

---

## Step 2: What To Inspect

Inspect in this order when relevant:

1. **User symptom**
   - broken page, failing endpoint, timeout, data corruption, auth issue
2. **Runtime evidence**
   - logs, traces, metrics, console errors, network failures
3. **Recent change history**
   - deploy timeline, feature flags, migrations, dependency changes
4. **Code surface**
   - likely entry points, data flow, integration boundaries
5. **Persistence layer**
   - DB schema, indexes, missing migrations, stale data, queue state

---

## Step 3: Mitigation Bias

Prefer the smallest safe mitigation that reduces impact:

- disable or isolate the failing path
- revert a narrow change if the evidence is strong
- add or restore a missing migration or config
- patch one integration boundary rather than refactoring the whole subsystem

Do not claim a root cause until the evidence supports it.

---

## Step 4: Closeout Expectations

When reporting back, make clear:

- symptom confirmed
- strongest hypothesis
- evidence checked
- mitigation applied or recommended
- verification run
- remaining unknowns

If the system is safer but the root cause is still incomplete, say so explicitly.
