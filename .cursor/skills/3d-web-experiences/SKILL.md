---
name: 3d-web-experiences
description: >
  Build distinctive, performant, production-grade 3D on the web with Three.js, React Three Fiber, and WebGL. Use when the user asks to "build a 3D scene", "add a 3D hero/landing", "make a product viewer/configurator", mentions three.js / react-three-fiber / r3f / drei / webgl / shaders, or asks to make an existing 3D scene "look good", run smoothly, or work on mobile. Covers aesthetic direction (anti-slop for 3D), lighting/material/post-processing, performance budgets, responsive WebGL, graceful degradation, accessibility, and M3 multimodal parity from reference video/frames.
license: MIT
metadata:
  version: "1.1.0"
  category: design
  sources:
    - Three.js official documentation (threejs.org/docs)
    - React Three Fiber docs (r3f.docs.pmnd.rs)
    - drei docs (drei.docs.pmnd.rs)
    - react-postprocessing docs (react-postprocessing.docs.pmnd.rs)
  model_assumptions:
    - multimodal-input: recommended
---

# 3D Web Experiences ("3D Taste + Production Layer")

Build 3D on the web that looks intentional and runs at frame rate on real devices, not a default gray model spinning on a purple gradient. This skill is the 3D counterpart to `anti-slop-design`: it enforces aesthetic direction, a performance budget, responsive behavior, and graceful degradation.

This skill teaches the *decisions and quality bar*. For mechanical Three.js / R3F syntax, see the `3d-graphics` rule. For deep recipes (lighting/material/post-fx, performance playbook, bug catalog, asset pipeline), read [reference.md](reference.md).

## When to Use

- Building any 3D web visual: hero scene, product viewer/configurator, data viz, immersive scroll.
- User mentions three.js, React Three Fiber (r3f), drei, WebGL, GLSL/shaders, or a `.glb`/`.gltf` model.
- User asks to make an existing 3D scene "look better", "run faster", or "work on mobile".

Read [reference.md](reference.md) for full scenes, multi-effect pipelines, or when debugging performance/visual issues. Skip it for a single mesh or a trivial tweak.

---

## Step 0: Read 3D Context

Before writing 3D code, inspect the project:

1. Stack: vanilla Three.js or React Three Fiber? Check `package.json` for `three`, `@react-three/fiber`, `@react-three/drei`, `@react-three/postprocessing`, `@react-three/rapier`.
2. Existing canvas/scene setup, renderer config (color space, tone mapping), and the container the canvas mounts into.
3. Asset pipeline: are models Draco/Meshopt compressed? Are textures KTX2/Basis? Where do assets live?
4. Target: is this a decorative hero, an interactive tool, or a full game-like loop? This sets the performance budget.
5. If a scene already exists, respect its conventions and extend; do not rebuild from scratch.

---

## Step 0.5: Multimodal Reference Parity (M3)

When the user attaches a reference video, a recorded interaction, or a sequence of frames showing the look they want:

- Read the actual file/frame, not a guessed description of it. On M3 the runtime can ingest video natively; treat the attachment as ground truth.
- For "make it look like this" requests, the reference is the contract. State the path in your closeout.
- For reference clips with motion, pick a small number of representative frames (start, mid, end) and reason about the in-between motion explicitly — do not invent the motion.
- After the build, re-read the rendered state (post-change frame) and compare against the reference; do not claim parity from memory.

## Step 1: Commit to a 3D Direction

Never ship the default look. Before coding, decide:

1. **Intent**: decorative background, hero focal object, interactive product, or data-driven. This dictates how much GPU budget the 3D earns.
2. **Mood + lighting model**: studio/three-point (product), HDRI environment (realistic), or stylized/toon (playful). Pick one; do not leave it ambient-only.
3. **Material direction**: realistic PBR, glass/transmission, stylized/toon, or gradient. Match the 2D brand palette (coordinate with `anti-slop-design`).
4. **The memorable moment**: the ONE thing a viewer remembers (a material, a reveal, a camera move, a light). Commit to it.
5. **Tone mapping + color space are not optional**: set `ACESFilmic` (or `AgX` on recent three) tone mapping and correct output color space, or the scene reads flat and washed.
6. **Damp all continuous motion**: camera moves, pointer-follow, and scroll-tied animation go through `MathUtils.damp`/lerp — never bind raw scroll or pointer values directly. Undamped motion is the 3D equivalent of no easing; it reads as cheap immediately.

---

## Banned Patterns ("3D Slop")

These are the statistical-median 3D outputs. Do not ship them as the final look:

- A lone glossy `TorusKnot`/`Icosahedron`/blob slowly auto-rotating on a purple→blue gradient background.
- Default gray `meshStandardMaterial` with no metalness/roughness intent and no environment map.
- Ambient-light-only scenes (flat, no form, no shadows) — or the opposite: a single point light with everyone's favorite hard black shadows.
- No tone mapping / wrong color space, so PBR materials look milky and lifeless.
- `OrbitControls` with infinite auto-rotate as the *only* "interactivity."
- Bloom cranked on the whole scene so everything glows (bloom should be selective).
- Particle fields of 10k points as a stand-in for an idea.
- Ignoring mobile: shipping full DPR + heavy post-fx that melts phones, or a blank canvas where WebGL is unavailable.
- The pasted-rectangle canvas: scene background mismatched with the page, hard edges, no compositional tie to the surrounding 2D layout. Blend with a matching clear color or transparent canvas, and let 2D content overlap the 3D so they read as one composition.

Pivot each to something category-appropriate: real product geometry, an HDRI-lit material study, a purposeful camera move, selective emissive glow, or a restrained, readable composition.

---

## Core Decisions

| Decision | Default that works | Push further |
|----------|-------------------|--------------|
| Lighting | `Environment` (HDRI) + one key `directionalLight` with soft shadows | Three-point studio rig; stylized rim light; baked lighting |
| Material | PBR `meshStandardMaterial` with an env map | `transmission` glass, toon/gradient, custom shader for the hero |
| Camera | Framed composition, slight FOV (35-50), not centered-and-static | Subtle parallax/scroll-tied move; `prefers-reduced-motion` respected |
| Color | `ACESFilmicToneMapping` + correct color space | Graded HDRI + matched `Vignette`/`Bloom` |
| Post-fx | None, or selective `Bloom` + light `Vignette` | DOF for product focus, SSAO for contact realism (budget permitting) |

See [reference.md](reference.md) for concrete, verified recipes for each.

---

## Performance Budget (decide before building)

Pick a target and hold to it. Frame budget is ~16.6ms for 60fps.

| Tier | Target | Draw calls | Triangles | Post-fx |
|------|--------|-----------|-----------|---------|
| Decorative / background | 60fps desktop, 30fps+ mobile | < 50 | < 150k | minimal |
| Hero / product | 60fps desktop, 30fps mobile | < 100 | < 500k | selective bloom/DOF |
| Interactive tool | 60fps desktop | < 200 | < 1M | as budget allows |

Core levers (full playbook in [reference.md](reference.md)):
- Clamp DPR: `dpr={[1, 2]}` in R3F (or `Math.min(devicePixelRatio, 2)`). Never render at uncapped retina DPR.
- Instance repeated geometry (`InstancedMesh` / drei `<Instances>`); merge static geometry.
- LOD with drei `<Detailed distances={[...]}>` for distant detail.
- Static scene? Use `frameloop="demand"` and `invalidate()` on change instead of rendering every frame.
- Compress assets: Draco/Meshopt for geometry, KTX2/Basis for textures.
- Dispose geometries, materials, and textures on unmount to avoid GPU memory leaks.

---

## Responsive & Mobile WebGL

3D must adapt across desktop, laptop, tablet, and phone — not just resize.

- Tie the renderer to its **container size**, not `window.innerWidth/Height`; the container must have an explicit height (see the `3d-graphics` rule's container guidance).
- Lower the effect tier on mobile: reduce/disable post-fx, cap DPR harder (`[1, 1.5]`), reduce shadow map size, drop particle counts.
- Use drei `<AdaptiveDpr pixelated />` and `<PerformanceMonitor>` to degrade quality under load automatically.
- Touch: ensure controls work with touch (pinch/drag); avoid hover-only affordances on touch devices.
- Respect `prefers-reduced-motion`: pause auto-rotation and large camera moves; offer a static framed view.

---

## Graceful Degradation & Loading

- Detect WebGL support; if unavailable, render a meaningful 2D fallback (poster image / static content), not a blank canvas.
- Wrap async 3D (models, HDRIs) in `Suspense` with a real loader (drei `useProgress` / `<Html>`), not a frozen white screen.
- Handle `webglcontextlost` (recover or show the fallback) — common on mobile after backgrounding.

---

## Accessibility

- A 3D canvas is not keyboard-operable by default. Provide an accessible alternative: descriptive text, a 2D version, or controls with real buttons.
- Do not trap focus or keyboard inside the canvas; ensure users can tab past it.
- Provide a visible pause/stop control for continuous motion (also satisfies `prefers-reduced-motion` users who toggle).
- Decorative canvases: mark `aria-hidden` and keep the real content in the DOM.

---

## Verification

3D is a UI/interaction change — static confidence is not proof. Before claiming done:

1. Load the scene in a browser (use the browser tools): confirm it renders, not a blank/black canvas.
2. Check the console for WebGL errors, shader compile errors, and `context lost` warnings.
3. Sanity-check frame rate (drei `<Stats>` or browser FPS) against the chosen budget tier.
4. Resize / emulate a phone viewport: confirm the canvas resizes with its container and the mobile effect tier kicks in.
5. Toggle `prefers-reduced-motion` and confirm motion is reduced.

Report what you verified and what remains unverified (e.g. "rendered and 60fps on desktop; mobile not device-tested").

---

## Pre-Delivery Checklist

```
[ ] Direction committed: intent, lighting model, material, memorable moment stated
[ ] No 3D slop (lone blob on purple gradient, default gray PBR, ambient-only, no tone mapping)
[ ] Tone mapping + correct output color space set on the renderer
[ ] Lighting has form: environment/HDRI or a real key/fill/rim, not ambient-only
[ ] Post-fx is selective and budget-justified, not whole-scene bloom
[ ] Performance budget chosen; DPR clamped; instancing/LOD used where relevant
[ ] Static scenes use frameloop="demand"; dispose on unmount
[ ] Canvas sized to its container (explicit height), resizes correctly
[ ] Mobile effect tier: reduced post-fx, capped DPR, adaptive DPR/perf monitor
[ ] WebGL-unavailable fallback renders meaningful 2D content
[ ] Suspense loader for async assets; context-lost handled
[ ] Accessible alternative + focus not trapped + pause control for motion
[ ] prefers-reduced-motion respected
[ ] Verified in browser: renders, no console errors, FPS within budget
```

---

## Quick Reference

```
READ    -> stack (vanilla vs R3F), renderer config, asset pipeline, container
COMMIT  -> intent + lighting model + material + memorable moment
BUDGET  -> pick tier (decorative/hero/interactive), clamp DPR, plan instancing/LOD
BUILD   -> lighting with form, tone mapping, selective post-fx, responsive sizing
DEGRADE -> WebGL fallback, Suspense loader, context-lost, reduced-motion, a11y
CHECK   -> browser render, console clean, FPS in budget, mobile + reduced-motion

BANNED  -> lone blob on purple gradient, default gray PBR, ambient-only lighting,
           no tone mapping, auto-rotate-only "interaction", whole-scene bloom,
           uncapped DPR, blank canvas with no fallback
ALWAYS  -> tone mapping + color space, lighting with form, clamped DPR,
           dispose on unmount, container-sized canvas, mobile tier, 2D fallback,
           accessible alternative, browser-verified
```
