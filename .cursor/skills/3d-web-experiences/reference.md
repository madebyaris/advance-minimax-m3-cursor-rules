# 3D Web Experiences Reference

Deep recipes for the `3d-web-experiences` skill: lighting, materials, post-processing, a performance playbook, a common-bug catalog, the asset pipeline, and degradation/accessibility patterns. Read this when building full scenes, multi-effect pipelines, or debugging performance/visual issues. Examples use React Three Fiber unless noted; the principles apply to vanilla Three.js too.

API note: package APIs move. The patterns below were aligned with current `three` / `@react-three/fiber` / `@react-three/drei` / `@react-three/postprocessing` docs, but re-verify exact prop names against the installed version before relying on them.

---

## Renderer Baseline (do this first)

A flat-looking scene is usually a renderer-config problem, not a lighting one.

```jsx
import { Canvas } from '@react-three/fiber'
import * as THREE from 'three'

<Canvas
  dpr={[1, 2]}                 // clamp device pixel ratio
  shadows                      // enable shadow maps
  gl={{ antialias: true, powerPreference: 'high-performance' }}
  camera={{ fov: 45, position: [0, 0, 6] }}
  onCreated={({ gl }) => {
    gl.toneMapping = THREE.ACESFilmicToneMapping  // or THREE.AgXToneMapping on recent three
    gl.toneMappingExposure = 1.0
    // Output color space is sRGB by default on modern three; set explicitly if unsure:
    gl.outputColorSpace = THREE.SRGBColorSpace
  }}
>
  {/* scene */}
</Canvas>
```

Vanilla Three.js equivalent: set `renderer.toneMapping`, `renderer.toneMappingExposure`, and `renderer.outputColorSpace` right after creating the `WebGLRenderer`, and size it to the container (see the `3d-graphics` rule).

---

## Lighting Recipes

### Environment-based (fastest path to "good")

The single highest-leverage move: image-based lighting via an HDRI environment. It lights and reflects in one step.

```jsx
import { Environment } from '@react-three/drei'

<Environment preset="city" />        {/* lights the scene; reflections on PBR materials */}
{/* presets: city, studio, sunset, dawn, night, warehouse, forest, apartment, park, lobby */}
{/* background={false} keeps the env for lighting only, not as the visible backdrop */}
```

Add one shaping light on top for direction and shadows:

```jsx
<directionalLight
  position={[5, 8, 5]}
  intensity={2}
  castShadow
  shadow-mapSize={[2048, 2048]}
  shadow-bias={-0.0001}            // reduces shadow acne
/>
```

### Three-point studio rig (product / portrait)

```jsx
<>
  {/* Key: brightest, off-axis */}
  <directionalLight position={[5, 5, 5]} intensity={2.5} castShadow />
  {/* Fill: softer, opposite side, no shadow */}
  <directionalLight position={[-5, 2, 5]} intensity={0.8} />
  {/* Rim / back: separates subject from background */}
  <directionalLight position={[0, 4, -6]} intensity={1.5} />
  <ambientLight intensity={0.15} />   {/* tiny floor, not the whole look */}
</>
```

### Soft contact shadows (cheap realism, no shadow-casting lights needed)

```jsx
import { ContactShadows } from '@react-three/drei'
<ContactShadows position={[0, -1, 0]} opacity={0.5} scale={10} blur={2.5} far={4} />
```

Lighting anti-patterns: ambient-only (no form), a single hard point light (harsh black shadows), or env map with zero directional shaping (no highlights).

---

## Material Recipes

### PBR (realistic)

```jsx
<meshStandardMaterial color="#b08d57" metalness={0.9} roughness={0.35} envMapIntensity={1} />
```

Metalness is near 0 or near 1 in reality; avoid 0.5 unless intentional. Roughness drives the look more than color. Needs an environment map to show reflections.

### Glass / transmission

```jsx
<meshPhysicalMaterial
  transmission={1}        // glass-like; needs the object to be non-opaque
  thickness={0.5}
  roughness={0.1}
  ior={1.5}
  envMapIntensity={1}
/>
```
Transmission is expensive — use sparingly and keep geometry simple. Requires an environment to refract.

### Stylized / toon

```jsx
import { useTexture } from '@react-three/drei'
const gradient = useTexture('/gradients/threeTone.jpg')  // small N-step gradient
<meshToonMaterial color="#6c5ce7" gradientMap={gradient} />
```

### Gradient / shader hero

For the memorable moment, a custom shader or a gradient material (e.g. via drei `MeshDistortMaterial`, `MeshWobbleMaterial`, or a `shaderMaterial`) beats another glossy PBR blob. Keep it to the one focal object.

---

## Post-Processing Stack

Use `@react-three/postprocessing`. Effects live inside `<EffectComposer>`, after scene content, inside the `Canvas`.

```jsx
import { EffectComposer, Bloom, Vignette, DepthOfField, Noise } from '@react-three/postprocessing'

<EffectComposer>
  <Bloom mipmapBlur luminanceThreshold={1} intensity={1.2} />
  <Vignette offset={0.3} darkness={0.6} />
</EffectComposer>
```

### Selective bloom (the correct way to glow)

Bloom is selective by default: only materials whose color/emissive exceed the `luminanceThreshold` glow. Set `luminanceThreshold={1}` and make the chosen object emit above 1 with tone mapping disabled:

```jsx
<meshStandardMaterial emissive="#ff5ea2" emissiveIntensity={3} toneMapped={false} />
```

Without `toneMapped={false}`, tone mapping clamps the color back into range and nothing glows. Whole-scene bloom (low threshold + everything bright) is slop — make the glow intentional.

### Effect costs (budget guidance)

| Effect | Cost | Use when |
|--------|------|----------|
| `Vignette`, `Noise` | cheap | almost always fine |
| `Bloom` (mipmapBlur) | moderate | selective glow, neon, emissive |
| `DepthOfField` | moderate-high | product focus, cinematic |
| `SSAO`/`N8AO` | high | grounded contact shadows, desktop only |

On mobile, disable or drop to the cheapest effects. Conditionally render the `<EffectComposer>` based on a device/performance check.

---

## Performance Playbook

### Instancing

For many copies of the same geometry, one `InstancedMesh` is one draw call instead of N.

```jsx
import { Instances, Instance } from '@react-three/drei'

<Instances limit={1000}>
  <boxGeometry args={[0.2, 0.2, 0.2]} />
  <meshStandardMaterial />
  {positions.map((p, i) => <Instance key={i} position={p} />)}
</Instances>
```

Vanilla / imperative: use `THREE.InstancedMesh`, set per-instance matrices with a reusable `THREE.Object3D` dummy, then `instanceMatrix.needsUpdate = true`.

### LOD (level of detail)

Swap detail by camera distance with drei `<Detailed>`. `distances` indices correspond to children in order (high → low detail).

```jsx
import { Detailed } from '@react-three/drei'

<Detailed distances={[0, 10, 25]}>
  <HighPolyModel />
  <MediumPolyModel />
  <LowPolyModel />
</Detailed>
```

### On-demand rendering (static scenes)

If the scene only changes on interaction, do not render 60fps forever:

```jsx
import { useThree } from '@react-three/fiber'
<Canvas frameloop="demand"> ... </Canvas>
// call invalidate() (from useThree) whenever something changes to request a frame
```

### Adaptive quality

```jsx
import { AdaptiveDpr, PerformanceMonitor } from '@react-three/drei'

<PerformanceMonitor onDecline={() => {/* drop effects, lower dpr */}} />
<AdaptiveDpr pixelated />
```

### Dispose on unmount (prevent GPU memory leaks)

R3F auto-disposes objects it created. For anything you build/load manually, dispose explicitly:

```js
geometry.dispose()
material.dispose()
texture.dispose()
// for a loaded scene: scene.traverse(o => { o.geometry?.dispose(); /* dispose materials/maps */ })
```

### Shadow cost

Shadows are expensive. Cap `shadow-mapSize` (1024 on mobile, 2048 desktop), shrink the shadow camera frustum to the scene, or replace dynamic shadows with `ContactShadows` / baked shadows.

---

## Responsive 3D Matrix

| Concern | Desktop | Tablet | Phone |
|--------|---------|--------|-------|
| DPR | `[1, 2]` | `[1, 1.75]` | `[1, 1.5]` |
| Post-fx | full (budgeted) | reduced | off or Vignette only |
| Shadow map | 2048 | 1024 | 1024 or ContactShadows |
| Particles / instances | full | ~60% | ~30% |
| Camera motion | full | full | reduce; respect reduced-motion |

Always size the renderer to the **container**, and update on resize. In R3F this is automatic when the parent has an explicit height; in vanilla Three.js, observe the container (e.g. `ResizeObserver`) and call `camera.updateProjectionMatrix()` + `renderer.setSize(w, h)`.

---

## Graceful Degradation

### WebGL detection + fallback

```js
import WebGL from 'three/examples/jsm/capabilities/WebGL.js'

if (WebGL.isWebGLAvailable()) {
  // mount the 3D canvas
} else {
  // render meaningful 2D content: poster image, static hero, or a message
}
```

### Suspense loader for async assets

```jsx
import { Suspense } from 'react'
import { useProgress, Html } from '@react-three/drei'

function Loader() {
  const { progress } = useProgress()
  return <Html center>{progress.toFixed(0)}%</Html>
}

<Canvas>
  <Suspense fallback={<Loader />}>
    <Model />
    <Environment preset="studio" />
  </Suspense>
</Canvas>
```

### Context loss

```js
gl.domElement.addEventListener('webglcontextlost', (e) => {
  e.preventDefault()    // allow restore
  // show fallback UI until 'webglcontextrestored'
})
```

---

## Accessibility Patterns

- Decorative canvas: wrap so the canvas is `aria-hidden` and the real content stays in the DOM and readable.
- Interactive 3D (configurator, viewer): provide real DOM controls (buttons, sliders) that drive the scene, so it is keyboard- and screen-reader-operable — do not rely on drag-only interaction.
- Provide a visible pause/play control for continuous animation.
- Honor `window.matchMedia('(prefers-reduced-motion: reduce)')`: stop auto-rotate and large camera moves; present a static framed composition.
- Never trap keyboard focus inside the canvas; users must be able to tab past it.

---

## Asset Pipeline

Optimize models and textures before shipping — this is usually the biggest perf and load-time win.

| Step | Tool | Why |
|------|------|-----|
| Compress geometry | Draco or Meshopt (via `gltf-transform` or `gltfpack`) | 5-10x smaller `.glb` |
| Compress textures | KTX2 / Basis (`gltf-transform` / `toktx`) | GPU-native, lower VRAM |
| Generate React component | `gltfjsx` (`npx gltfjsx model.glb`) | typed, declarative scene graph |
| Inspect / prune | `gltf-transform inspect` / `prune` | drop unused nodes, dedupe |

Loading compressed assets in R3F:

```jsx
import { useGLTF } from '@react-three/drei'
// useGLTF wires Draco + Meshopt decoders automatically in current drei
const { scene } = useGLTF('/models/product.glb')
useGLTF.preload('/models/product.glb')   // preload for snappier first paint
```

For KTX2 textures, use drei's `useKTX2` (or a configured `KTX2Loader`). Verify decoder/transcoder paths against the installed drei version.

---

## Common 3D Bug Catalog

These are the bugs models generate most often (including the ones removed from the `3d-graphics` rule).

| Symptom | Cause | Fix |
|---------|-------|-----|
| `useFrame is not a function` / undefined | Imported `useFrame` from `react` | `import { useFrame } from '@react-three/fiber'` (only `useRef`, `useState`, etc. come from `react`) |
| `<Detail>` / LOD JSX errors | Used a non-existent `Detail` from `three` | Use drei `<Detailed distances={[...]}>` with mesh children |
| Instancing example won't compile | `InstancedMesh`/`Object3D` imported from fiber | Use the `<instancedMesh>` JSX element (or `THREE.InstancedMesh`); import `Object3D` from `three` |
| Canvas has zero height / invisible | Parent container has no height | Give the container an explicit height; canvas fills its parent |
| Scene looks flat / milky | No tone mapping or wrong color space | Set `ACESFilmic`/`AgX` tone mapping + sRGB output color space |
| Nothing glows with Bloom | Material tone-mapped, color in 0-1 | `toneMapped={false}` + emissive/color above the `luminanceThreshold` |
| FPS tanks over time | Geometry/material/texture not disposed | Dispose on unmount; reuse geometries/materials |
| Jagged shadows / acne | No shadow bias, tiny map | Set `shadow-bias`, raise `shadow-mapSize`, tighten shadow camera |
| Blurry or slow on retina | Uncapped DPR | Clamp `dpr={[1, 2]}` |
| Blank canvas on some devices | No WebGL / context lost | Detect WebGL, provide 2D fallback, handle context-lost |

---

## When NOT to Read This File

- A single mesh or a one-line tweak — `SKILL.md` plus the `3d-graphics` rule is enough.
- No 3D in the project yet and the user only wants 2D UI — use `anti-slop-design` instead.
