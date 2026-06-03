---
name: minimax-multimodal-toolkit
description: >
  MiniMax-native multimodal workflow for image, video, voice, music, and media-processing tasks.
  Use when the user asks to generate image/video/audio assets, wants MiniMax-specific media APIs,
  needs TTS or voice workflows, wants reproducible local media outputs, or needs FFmpeg-style
  processing around generated media. M3's native multimodal input means image/video inputs can
  be fed directly to the model for grounded decisions in coding work.
license: MIT
metadata:
  version: "1.1.0"
  category: media-generation
  sources:
    - MiniMax platform media capabilities
    - Current runtime tool surface
    - FFmpeg documentation
  model_assumptions:
    - multimodal-input: required
---

# MiniMax Multimodal Toolkit

Use MiniMax-native media workflows without bloating the always-on prompt. Route the task to the smallest path that can honestly produce the requested artifact.

## When to Use

- The user asks for image, video, voice, speech, music, or multimodal asset generation
- The user explicitly mentions MiniMax media capabilities or wants MiniMax API integration
- The user wants reproducible local media outputs rather than only in-chat prose
- The task involves media conversion, trimming, concatenation, or extraction around generated assets

**For deeper routing notes, output conventions, and implementation details, also read `reference.md` in this skill directory.**

---

## Step 0: Determine the Real Goal

Classify the task before acting:

1. **Direct asset generation**: user wants an image, clip, narration, or music artifact
2. **Product integration**: user wants app code that calls MiniMax media APIs
3. **Media pipeline work**: user already has files and needs processing, conversion, or stitching
4. **Capability research**: user wants comparison, planning, or API guidance before building

Do not jump into API integration when a direct generation path is enough.

---

## Step 1: Route to the Right Path

| User need | Primary path | Notes |
|---|---|---|
| One-off image asset | Use the runtime's direct image-generation tool if available | Fastest path for explicit image requests |
| Video, TTS, voice, music, or MiniMax-specific generation | Use current MiniMax docs and the repo/runtime tool surface | Check auth and output path first |
| Existing media needs editing | Use local tooling such as FFmpeg when available | Avoid re-generation unless needed |
| App feature using MiniMax media APIs | Implement integration code and verify with a focused request or fixture | Prefer smallest vertical slice |
| Planning or research only | Gather current docs and synthesize | Do not implement prematurely |
| **M3 input path: read an attached image / video frame as ground truth** | Feed the file/frame into the model directly via the runtime's multimodal input — no separate "describe the image" step | Use for design parity, error UI triage, screenshot-driven dev. See the `minimax-m3-multimodal-input` skill for the full workflow. |

---

## Step 2: Inspect Before Generating

Before any implementation or generation:

1. Inspect the repo for existing media patterns, asset folders, env handling, and helper utilities
2. Check the current runtime for direct generation tools before inventing scripts
3. Check whether required MiniMax credentials or host configuration already exist
4. Clarify only if the missing answer changes the route:
   - output medium
   - target format
   - duration or size constraints
   - whether the user wants direct generation or product integration

---

## M3 Native Multimodal Input

On M3, image and video inputs can be fed to the model directly. This collapses the older "read the file, write a text description, then reason about the description" loop into a single grounded step:

- The user attaches an image, screenshot, mock, or short clip; the runtime passes it to M3 as native input.
- Ground decisions in what the image actually shows. Quote visible text, cite regions, name the file path.
- For the full input-handling workflow (region citations, before/after diffing, multi-frame video, design parity), load the `minimax-m3-multimodal-input` skill.

This skill (`minimax-multimodal-toolkit`) remains the source of truth for **generation** paths — calling MiniMax media APIs, FFmpeg pipelines, and reproducible local outputs. The two skills are complementary: this one for output, `minimax-m3-multimodal-input` for input.

## Core Rules

- Prefer the smallest path that produces the requested artifact honestly
- Use direct generation tools for explicit image requests when available
- Use MiniMax-specific API flows when the user asks for MiniMax integration, reproducibility, video, TTS, voice, or music
- Keep generated outputs in a predictable project-local folder rather than scattering temp files
- Never hardcode secrets; use environment variables and document the missing configuration
- Do not claim a generated asset exists until you have verified the file or response
- For integration work, verify one focused happy-path request before broadening the feature

---

## Verification Expectations

Match proof to the task:

- **Asset generation**: verify the output file exists or the tool returned a concrete artifact
- **API integration**: verify one focused request, script, or runtime flow
- **Media processing**: verify the output file was created and matches the requested format or duration
- **UI integration**: verify at the user surface, not only by build success

If the artifact was designed but not generated, report it as `changed` and `unverified`, not complete.

---

## Workflow

```text
1. CLASSIFY -> direct asset, integration, processing, or research
2. ROUTE -> choose direct tool, MiniMax API path, or local media tooling
3. INSPECT -> repo patterns, runtime surface, env/auth, output constraints
4. EXECUTE -> make the smallest honest slice
5. VERIFY -> prove the artifact or integration at the relevant surface
```

---

## Quick Reference

```text
IMAGE      -> direct image tool first when available
VIDEO/TTS  -> MiniMax-specific workflow or integration path
MUSIC      -> MiniMax-specific workflow or integration path
PROCESSING -> local media tooling, usually FFmpeg
INTEGRATE  -> smallest API slice + focused verification

ALWAYS     -> inspect runtime first, use env vars for secrets, verify outputs
NEVER      -> hardcode keys, promise files that were not produced, skip surface proof
```
