---
name: anti-slop-design
description: Category-aware design skill that builds distinctive, production-grade UIs. Palettes, font pairings, UX patterns, shadcn/token integration, empty-error-loading copy, secondary slop signals, multimodal design parity from mocks, and a pre-ship second pass. Framework-agnostic.
license: MIT
metadata:
  version: "1.1.0"
  category: design
  sources:
    - Project design systems and token files
    - Platform accessibility guidance
    - Established product and editorial design patterns
  model_assumptions:
    - multimodal-input: recommended
---

# Anti-Slop Design Skill ("Taste Layer")

Build UIs that look like a senior designer made them, not a language model. This skill enforces category-aware design thinking, concrete palettes, and a pre-delivery quality gate.

## When to Use

- Building any UI: landing page, dashboard, app screen, marketing site
- User asks to "design", "build a page", "create a component", or "make it look good"
- User asks to "create a design system" or "set up design tokens"
- Reviewing or improving existing UI code

**For full pages or multi-section layouts**, also read `reference.md` in this skill directory. It contains section anatomy patterns, extended slop catalog, microcopy examples, stack-specific notes, common mistakes per category, CSS token starters, and a mobile-first checklist. Skip it for single-component work.

---

## Step 0: Read Design Context

Before designing anything, inspect the project:

1. Check the package manifest for styling approach (Tailwind, CSS Modules, styled-components, vanilla CSS).
2. Check for existing design tokens: `tailwind.config.*`, `theme.ts`, CSS variable files, `globals.css`.
3. Check for existing font imports (Google Fonts `@import`, `next/font`, `@font-face`).
4. Check for an existing icon library (lucide-react, heroicons, phosphor, etc.).
5. If a design system already exists, respect it. Extend, do not replace.

Skip this step only for standalone demos or canvases with no project context.

---

## Step 1: Design Thinking

Before writing any UI code, commit to a direction. Never skip this.

1. **Identify the category.** Match the project to a row in the Category Design Guide below.
2. **Pick the tone.** Use the category's recommended tone or choose a bold alternative -- never "modern and clean" (that is generic).
3. **State the memorable thing.** What is the ONE element someone will remember? Commit to it.
4. **Vary across generations.** If your last output was dark editorial, the next must differ -- unless the user explicitly requests consistency.

---

## Banned Patterns ("AI Slop")

These are the statistical median of AI training data. Never generate them:

- Three-column card grids with centered icons and centered text
- Indigo/purple gradients on buttons or text (unless explicitly requested)
- Thick gray borders and over-boxed layouts
- Emoji as UI icons
- Inter, Roboto, Arial, system-ui, Space Grotesk as default fonts
- Empty hero sections with no imagery or decorative elements
- Generic "Lorem ipsum" placeholder text
- Colored-circle-initial avatars
- 5-star yellow rating widgets
- Cookie-cutter components with no context-specific character

### Secondary slop signals (also avoid)

These patterns are nearly as common as the list above; treat them as soft bans unless the user explicitly wants them.

- **Glass stacks**: multiple nested `backdrop-blur` panels filling the page — reads as template UI; use glass for one focal layer only.
- **Blob clusters**: three overlapping blurred circles (purple/pink/cyan) behind every hero — substitute category-specific texture, photography, or one intentional mesh.
- **Fake social proof**: "Trusted by" with placeholder logos, repeated generic company names, or SVG boxes labeled "Logo".
- **Abstract 3D illustration overload**: same glossy shapes on every SaaS landing — prefer product screenshots, UI chrome, or category-appropriate photography.
- **Identical section rhythm**: every block is `py-24` + headline + subtitle + grid — vary vertical rhythm, full-bleed breaks, or editorial pulls.
- **Motion soup**: everything fades in on scroll with the same delay — stagger meaningfully or reserve motion for one hero moment.
- **Generic microcopy**: "Welcome!", "No data available", "Something went wrong" with no next step — write voice-specific, actionable copy (see reference.md).

---

## Multimodal Design Parity (M3)

When the user provides a design mock, screenshot, or reference image, treat the image as the contract for the build. On M3 the runtime can read the image directly; do not paraphrase from a guessed description.

- `Read` the image file in the current session and reference the exact path in your closeout.
- Cite the **region** you are matching (hero block, top-right nav, footer) when reviewing deviations — generic "looks right" is not a citation.
- After the build, re-read the resulting state (post-change screenshot/frame) and compare against the reference; state "visually matched" only when you actually opened both.
- If the reference is a low-fidelity wireframe, design for the wireframe's intent, not its pixel values; if the reference is a high-fidelity mock, match the values.
- For multi-image sets (desktop, tablet, mobile mockups), re-read each before claiming a responsive match.

## Stack And Kit Integration

When the project already uses **shadcn/ui**, **Radix**, **MUI**, or similar:

1. **Do not replace** the component library for marketing polish — map the Category Design Guide to **semantic tokens** (`--primary`, `--background`, `--muted`, radius) so primitives stay accessible.
2. Override at **theme / CSS variable** layer first; only fork components when layout truly demands it.
3. For Tailwind v4, prefer `@theme` or token files that align with existing `globals.css` — avoid parallel conflicting palettes.

---

## Copy, Empty, And Error States

- Headlines and CTAs should sound like **this product**, not any SaaS: ban "Empower your workflow", "Unlock potential", "Streamline operations" unless ironic.
- **Empty states**: explain what will appear, one primary action, optional illustration that matches category — not a gray box and "Nothing here".
- **Errors**: what failed, what the user can do, support or retry — not only red text "Error".
- **Loading**: prefer skeleton shapes that match final layout; avoid infinite shimmer on unrelated blocks.

---

## Category Design Guide

Match the project to a category. Use the palette, fonts, and patterns as your starting point -- then push further.

### SaaS / Developer Tools

| Aspect | Guidance |
|--------|----------|
| **Palette** | Slate base (`#0f172a`, `#1e293b`), brand accent (teal `#14b8a6`, blue `#3b82f6`, or lime `#84cc16`), surface `#f8fafc` |
| **Fonts** | Display: Plus Jakarta Sans, Geist, Satoshi. Body: DM Sans, Source Sans 3 |
| **Tone** | Precise, confident, developer-friendly. Dense information without clutter |
| **UX patterns** | Product screenshot above fold, feature comparison grids, code snippets, transparent pricing, trust badges (SOC 2, uptime), developer docs link in nav |
| **Atmosphere** | Subtle dot-grid or noise backgrounds, monospace accents for technical credibility, dark mode as primary |
| **Avoid** | Marketing fluff, stock photography of people pointing at screens, excessive whitespace that wastes developer attention |

### E-commerce / Retail

| Aspect | Guidance |
|--------|----------|
| **Palette** | Warm neutrals (`#faf9f6`, `#292524`), accent for CTAs (coral `#f97316`, rose `#e11d48`), gold for premium (`#d4a574`) |
| **Fonts** | Display: Playfair Display, Fraunces (luxury), Bricolage Grotesque (casual). Body: DM Sans, Outfit |
| **Tone** | Product-led. The merchandise is the hero, not the UI chrome |
| **UX patterns** | Large product imagery, quick-add-to-cart, persistent cart indicator, urgency signals (stock count, not fake timers), filters/sort, social proof near buy button |
| **Atmosphere** | Clean product photography on neutral backgrounds, lifestyle imagery for context, subtle hover zoom on products |
| **Avoid** | Cluttered sidebars, aggressive pop-ups, fake urgency countdown timers, tiny product images |

### Fintech / Banking

| Aspect | Guidance |
|--------|----------|
| **Palette** | Deep navy (`#0b1f33`, `#1e3a5f`), trust teal (`#0d9488`), muted gold (`#b8860b`), surface `#f0f4f8` |
| **Fonts** | Display: Newsreader, Instrument Serif. Body: Geist, DM Sans |
| **Tone** | Authoritative, calm, trustworthy. Every pixel communicates stability |
| **UX patterns** | Compliance badges above fold, transparent fee structures, account dashboards with clear hierarchy, monospace for financial figures, security indicators |
| **Atmosphere** | Subtle gradients (navy-to-dark), fine-line geometric patterns, minimal motion (stability over playfulness) |
| **Avoid** | Flashy animations, crypto-bro neon aesthetics (unless explicitly a crypto project), hiding fees, cluttered dashboards |

### Healthcare / Medical

| Aspect | Guidance |
|--------|----------|
| **Palette** | Clinical blue (`#1e40af`, `#3b82f6`), calming teal (`#0d9488`), soft green (`#86efac`), warm surface `#f0fdf4` or `#f8fafc` |
| **Fonts** | Display: Source Serif 4, Fraunces. Body: Source Sans 3, DM Sans |
| **Tone** | Calm, trustworthy, accessible. Patients are anxious -- reduce cognitive load |
| **UX patterns** | Clear appointment CTAs, provider credentials visible, HIPAA/certification badges, large touch targets, high contrast for aging users, simple forms |
| **Atmosphere** | Soft gradients, organic rounded shapes, generous whitespace, calming imagery (nature, not sterile stock photos) |
| **Avoid** | Red as primary (triggers alarm), dense data tables for patients, small text, complex navigation, clinical coldness |

### Portfolio / Personal

| Aspect | Guidance |
|--------|----------|
| **Palette** | Achromatic base (`#0a0a0a`, `#fafafa`) with one signature accent that reflects personality |
| **Fonts** | Display: Cormorant Garamond, Instrument Serif, Bricolage Grotesque. Body: Satoshi, DM Sans |
| **Tone** | The work speaks. Minimal chrome, maximum project visibility |
| **UX patterns** | Project grid or scroll-based case studies, hover reveals, smooth page transitions, concise bio, contact CTA |
| **Atmosphere** | Dramatic whitespace or dramatic darkness, project imagery as the primary texture, subtle cursor effects |
| **Avoid** | Walls of text about yourself before showing work, generic "About Me" sections with stock icons, skill-bar charts |

### Blog / Editorial / Media

| Aspect | Guidance |
|--------|----------|
| **Palette** | Rich ink (`#1a1a2e`, `#0f172a`), warm paper (`#fefce8`, `#faf5ee`), accent for links/highlights |
| **Fonts** | Display: Lora, Libre Baskerville, Newsreader. Body: Source Serif 4, Merriweather, Charter |
| **Tone** | Typographic excellence. The reading experience is the product |
| **UX patterns** | 65-75 character line length, generous line-height (1.6-1.8), clear article hierarchy, pull quotes, related articles, reading time estimate |
| **Atmosphere** | Paper-like textures, drop caps, editorial grid with asymmetric image placement, subtle serif elegance |
| **Avoid** | Sidebar clutter, auto-playing media, pop-ups that interrupt reading, tiny body text, infinite scroll without pagination option |

### Restaurant / Food & Beverage

| Aspect | Guidance |
|--------|----------|
| **Palette** | Warm earth tones (terracotta `#c2703e`, olive `#606c38`, cream `#fefae0`) or moody dark (charcoal `#1a1a1a`, burgundy `#722f37`) |
| **Fonts** | Display: Cormorant Garamond, Playfair Display (upscale), Bricolage Grotesque (casual). Body: DM Sans, Outfit |
| **Tone** | Appetizing. The food and atmosphere are the stars |
| **UX patterns** | Menu with prices (not PDF), reservation CTA always visible, hours + location prominent, food photography hero, online ordering link |
| **Atmosphere** | Full-bleed food photography, warm lighting in imagery, textured backgrounds (linen, wood grain), subtle parallax |
| **Avoid** | PDF-only menus, tiny text, auto-playing background music, Flash-era animations, hiding the phone number |

### Real Estate / Property

| Aspect | Guidance |
|--------|----------|
| **Palette** | Sophisticated neutrals (`#1c1917`, `#44403c`), forest green (`#166534`), warm gold (`#b45309`), surface `#fafaf9` |
| **Fonts** | Display: Instrument Serif, Newsreader. Body: DM Sans, Geist |
| **Tone** | Aspirational but trustworthy. Properties sell on emotion and credibility |
| **UX patterns** | Search/filter as hero, large property photos with gallery, map integration, agent contact prominent, virtual tour links, neighborhood info |
| **Atmosphere** | Full-bleed property photography, clean card layouts for listings, map-based browsing, subtle hover transitions |
| **Avoid** | Tiny listing thumbnails, cluttered search forms, hiding agent contact info, auto-rotating carousels |

### Education / EdTech

| Aspect | Guidance |
|--------|----------|
| **Palette** | Friendly blue (`#2563eb`, `#60a5fa`), warm yellow (`#fbbf24`), green for progress (`#22c55e`), light surface `#f8fafc` |
| **Fonts** | Display: Plus Jakarta Sans, Bricolage Grotesque. Body: DM Sans, Nunito |
| **Tone** | Encouraging, clear, structured. Reduce anxiety about learning |
| **UX patterns** | Progress indicators, clear course structure, achievement badges, readable content areas, accessible navigation, search |
| **Atmosphere** | Friendly illustrations (not stock photos), subtle gradients, rounded shapes, generous spacing |
| **Avoid** | Overwhelming dashboards, tiny text, complex navigation trees, gamification that distracts from learning |

### Agency / Creative Studio

| Aspect | Guidance |
|--------|----------|
| **Palette** | Bold and opinionated -- this is where you push hardest. Achromatic with one electric accent, or full maximalist color |
| **Fonts** | Display: Oversized sans (Neue Montreal, Satoshi at 80px+), or dramatic serif (Cormorant at scale). Body: matching sans |
| **Tone** | The website IS the portfolio. Every interaction demonstrates capability |
| **UX patterns** | Case study scroll, dramatic transitions, cursor effects, work grid with hover reveals, minimal nav, bold typography as layout |
| **Atmosphere** | Custom effects (not templates), smooth scroll, video backgrounds, experimental layouts, grain/noise textures |
| **Avoid** | Template-looking layouts, generic stock imagery, conservative corporate feel, listing services without showing work |

### Legal / Corporate / Professional Services

| Aspect | Guidance |
|--------|----------|
| **Palette** | Warm charcoal (`#1c1917`, `#292524`), muted gold (`#b8860b`, `#d4a574`), deep navy (`#1e3a5f`), cream surface `#fffbeb` |
| **Fonts** | Display: Newsreader, Instrument Serif, Cormorant Garamond. Body: Source Sans 3, DM Sans |
| **Tone** | Authoritative, established, trustworthy. Quiet confidence, not flashy |
| **UX patterns** | Attorney/team bios with credentials, practice area navigation, consultation CTA always visible, testimonials, case results |
| **Atmosphere** | Editorial whitespace, subtle serif elegance, muted photography, fine horizontal rules as dividers |
| **Avoid** | Gavel/scales-of-justice stock photos, aggressive CTAs, flashy animations, hiding contact information |

### Entertainment / Gaming

| Aspect | Guidance |
|--------|----------|
| **Palette** | Deep dark (`#0f0f1a`, `#1a1a2e`), neon accents (cyan `#06b6d4`, magenta `#ec4899`, electric purple `#8b5cf6`) |
| **Fonts** | Display: Bold geometric sans (Satoshi, Outfit at heavy weights), or custom display faces. Body: DM Sans, Geist |
| **Tone** | High energy, immersive, community-driven |
| **UX patterns** | Hero with video/animation, game/content cards with hover effects, leaderboards, community features, trailer embeds, release countdowns |
| **Atmosphere** | Particle effects, glow/bloom on accents, dark mode primary, animated backgrounds, sound design cues |
| **Avoid** | Flat corporate layouts, excessive text blocks, slow page loads from unoptimized assets, inaccessible color contrast on neon |

### Non-profit / Charity

| Aspect | Guidance |
|--------|----------|
| **Palette** | Warm and human -- earth tones (`#92400e`, `#166534`), warm blue (`#1d4ed8`), hopeful accents (amber `#f59e0b`), light surface |
| **Fonts** | Display: Fraunces, Source Serif 4. Body: DM Sans, Source Sans 3 |
| **Tone** | Emotionally honest without manipulation. Impact-focused, transparent |
| **UX patterns** | Impact metrics above fold, donation CTA persistent but not aggressive, story-driven sections, transparency (where money goes), volunteer/event CTAs |
| **Atmosphere** | Real photography of people and communities (not stock), warm color grading, generous whitespace, human-scale typography |
| **Avoid** | Guilt-driven dark patterns, hiding financial information, stock photos of sad children, aggressive pop-up donation asks |

### Travel / Hospitality

| Aspect | Guidance |
|--------|----------|
| **Palette** | Sky and earth (ocean blue `#0369a1`, sand `#d4a574`, sunset coral `#fb923c`), warm surface `#fffbeb` |
| **Fonts** | Display: Cormorant Garamond, Playfair Display (luxury), Bricolage Grotesque (adventure). Body: DM Sans, Outfit |
| **Tone** | Aspirational. The user should feel the destination before booking |
| **UX patterns** | Full-bleed destination photography, search/date picker as hero, itinerary builders, reviews near booking CTA, map integration |
| **Atmosphere** | Cinematic imagery, parallax scrolling on landscapes, warm color grading, immersive full-width sections |
| **Avoid** | Tiny thumbnails, complex multi-step booking without progress indication, hiding total prices, generic city stock photos |

### Fitness / Wellness / Beauty

| Aspect | Guidance |
|--------|----------|
| **Palette** | Split by sub-tone. Fitness: bold (charcoal `#171717`, electric orange `#f97316`, lime `#84cc16`). Wellness: soft (sage `#a3b18a`, cream `#fefae0`, blush `#fecdd3`). Beauty: luxe (rose gold `#b76e79`, deep plum `#581c87`, pearl `#f5f5f4`) |
| **Fonts** | Fitness: Satoshi, Outfit (bold weights). Wellness: Fraunces, Cormorant Garamond. Beauty: Instrument Serif, DM Sans |
| **Tone** | Fitness: energizing, bold. Wellness: calming, nurturing. Beauty: luxurious, aspirational |
| **UX patterns** | Transformation stories, booking/scheduling CTA, class/service listings, trainer/practitioner bios, before/after (tastefully), membership pricing |
| **Atmosphere** | Fitness: high-contrast, dynamic angles, action photography. Wellness: soft gradients, organic shapes, nature imagery. Beauty: clean product shots, soft lighting, editorial layouts |
| **Avoid** | Unrealistic body imagery, aggressive "transform yourself" language for wellness, cluttered service menus, hiding prices |

---

## The Taste Layer Principles

These apply universally across all categories.

### Typography
- Distinctive font pairings mandatory -- use the category guide as starting point.
- Hierarchy through weight and color, not just size. De-emphasize secondary text with tinted muted colors, not smaller-and-black.
- Left-align body text. Center-align only for short hero headlines.

### Color
- Cohesive palette via CSS variables. One dominant + one sharp accent beats an evenly-distributed rainbow.
- Tinted grays (slate, zinc, stone) that complement the primary. Never pure neutral gray.
- Dark mode: rich deep colors (`#0A0A0B`, `#0f172a`), not `#000`. Light mode: warm/cool off-whites, not `#FFF`.

### Spacing and Layout
- Start with too much whitespace, then tighten. Strict 4px-based spacing scale.
- Integrated over boxed: elements breathe on the canvas, not everything in cards.
- All sections share the same `max-width` and horizontal padding -- edges align hero to footer.
- Hero: `height: 100svh` with symmetric vertical padding for true optical centering.

### Motion
- Orchestrated page entrance with staggered `animation-delay` reveals.
- `IntersectionObserver` for scroll-triggered fade-up/slide-in below the fold.
- Hover states that surprise: scale, color shift, shadow, underline. Not just opacity.
- Always respect `prefers-reduced-motion`.

### Backgrounds and Atmosphere
- Match to category: gradient meshes for luxury, noise/grain for tactile premium, dot-grids for technical, organic shapes for wellness.
- Glassmorphism only when it serves the design, not as a default.

### Borders and Depth
- Separate with whitespace or subtle background shifts. Use `ring-1 ring-black/5` for subtle edges.
- Shadows only for true elevation (dropdowns, floating nav). No decorative drop shadows.

### Icons
- Real SVG only: Lucide, Heroicons, Phosphor, Hugeicons. Never emoji.
- Style matches tone: stroke for minimal, filled for bold, duotone for marketing.
- Sizes: 16-20px inline, 24px nav, 32-48px feature callouts.

### Imagery
- Hero sections never visually empty: real photography (Unsplash, Pexels), product screenshots, or decorative SVG.
- Real headshots for testimonials, not colored-circle initials.
- When photography unavailable: animated SVG shapes, gradient blobs, or geometric patterns.

---

## Design System Generation

When asked to create a design system or set up tokens, output this structure:

### Master Tokens

```
Category: [matched from Category Design Guide]
Tone: [one sentence]

Palette (CSS variables):
  --color-primary:    [hex]
  --color-secondary:  [hex]
  --color-accent:     [hex]
  --color-surface:    [hex]
  --color-surface-alt:[hex]
  --color-text:       [hex]
  --color-text-muted: [hex]
  --color-success:    [hex]
  --color-warning:    [hex]
  --color-error:      [hex]

Typography:
  --font-display: '[Display Font]', [fallback]
  --font-body:    '[Body Font]', [fallback]
  --font-mono:    '[Mono Font]', monospace  (if needed)

  Scale: 12 / 14 / 16 / 18 / 20 / 24 / 30 / 36 / 48 / 60 / 72

Spacing (4px base):
  4 / 8 / 12 / 16 / 20 / 24 / 32 / 40 / 48 / 64 / 80 / 96

Border radius:
  --radius-sm: 4px
  --radius-md: 8px
  --radius-lg: 16px
  --radius-full: 9999px

Shadows:
  --shadow-sm:  0 1px 2px rgba(0,0,0,0.05)
  --shadow-md:  0 4px 12px rgba(0,0,0,0.08)
  --shadow-lg:  0 8px 24px rgba(0,0,0,0.12)
```

### Page Overrides (Optional)

When a specific page deviates from the master (e.g., a marketing landing page within a SaaS dashboard), document the override:

```
Page: [name]
Overrides:
  --color-surface: [different hex]
  Tone shift: [e.g., "more playful than the dashboard default"]
  Additional font: [if needed]
```

---

## Domain-Specific Patterns

| Domain | Key rules |
|--------|-----------|
| **Landing pages** | Hero with 100svh centering, consistent max-width across sections, real imagery or decorative SVG fills, single primary CTA per section |
| **Dashboards** | Dense but hierarchical, semantic status colors, real chart libraries (Recharts, Chart.js with fixed-height containers), data tables with proper alignment |
| **Forms** | Accessible labels on every input, clear error states with color + icon + text, logical tab order, generous touch targets (44px min) |
| **Marketing sites** | Story-driven scroll, social proof near CTAs, distinctive hero that is not a three-column card grid, real testimonial photos |
| **Mobile / responsive** | 44px minimum touch targets, fluid typography (`clamp()`), thumb-zone navigation, no horizontal scroll, test at 375px and 768px |

---

## Workflow

```
1. READ    -> Inspect project: styling approach, existing tokens, fonts, icons
2. MATCH   -> Identify category from the Category Design Guide
3. COMMIT  -> State tone + memorable element in one sentence
4. BUILD   -> Apply category palette, fonts, and patterns + Taste Layer principles
5. CHECK   -> Run Pre-Delivery Checklist + Slop second pass before presenting
```

---

## Slop Second Pass (before ship)

After the main checklist, scan once for:

1. **Sameness**: If two sections could swap places with no loss of meaning, differentiate structure or merge them.
2. **Proof**: At least one place shows **real product, real data shape, or real imagery** — not only abstract shapes and lorem.
3. **One accent rule**: Count accent-color uses; if more than three competing "look at me" elements per viewport, demote some to neutral.
4. **Touch**: Every primary action on mobile is reachable and ≥44px; no hover-only affordances.
5. **Voice**: Read headings aloud — if they could apply to any competitor, rewrite.

---

## Pre-Delivery Checklist

Before presenting any UI code, verify every item:

```
[ ] Design thinking completed (category identified, tone stated)
[ ] No banned patterns (Inter, purple gradients, emoji icons, empty heroes, 3-col card grids)
[ ] Font pairing is distinctive and matches category
[ ] Icons from real SVG library (Lucide, Heroicons, Phosphor)
[ ] Hero and feature areas have imagery or decorative fills
[ ] Color palette uses CSS variables, tinted grays, no pure #000/#FFF
[ ] Sections share consistent max-width and padding
[ ] Responsive: tested mentally at 375px, 768px, 1024px, 1440px
[ ] prefers-reduced-motion respected for all animations
[ ] Accessibility: 4.5:1 contrast, visible focus states, form labels
[ ] Cursor pointer on all clickable elements
[ ] Hover states provide clear visual feedback (not just opacity)
[ ] No secondary slop: blob trio hero, stacked glass panels, fake logo wall, motion soup
[ ] If shadcn/MUI/Radix: colors/radius mapped to tokens, components not rewritten unnecessarily
[ ] Empty / error / loading states are specific and actionable, not generic placeholders
[ ] Slop second pass completed (sameness, proof, accent discipline, touch, voice)
```

---

## Before / After Examples

### Before: "AI Slop"
```html
<div style="border: 1px solid #e5e7eb; border-radius: 8px; padding: 16px; font-family: Inter, sans-serif;">
  <h3 style="font-size: 20px; font-weight: bold; color: black;">Plan your project</h3>
  <p style="font-size: 14px; color: #374151; margin-top: 8px;">Use our tool to manage tasks.</p>
  <button style="margin-top: 16px; background: linear-gradient(to right, #8b5cf6, #6366f1); color: white; padding: 8px 16px; border-radius: 6px;">
    Get Started
  </button>
</div>
```

### After: Category-Aware (SaaS)
```html
<div style="position: relative; overflow: hidden; border-radius: 16px; background: #f8fafc;
  outline: 1px solid rgba(15,23,42,0.06); padding: 32px; transition: box-shadow 0.3s;">
  <!-- Subtle radial glow from category accent (teal) -->
  <div style="position: absolute; inset: 0;
    background: radial-gradient(circle at 70% 20%, rgba(20,184,166,0.06), transparent 60%);"></div>
  <div style="position: relative; display: flex; flex-direction: column; align-items: flex-start; gap: 16px;">
    <span style="display: inline-flex; align-items: center; gap: 6px; font-size: 12px;
      font-weight: 600; letter-spacing: 0.05em; text-transform: uppercase;
      color: #14b8a6; font-family: 'DM Sans', sans-serif;">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor"
        stroke-width="2"><rect x="3" y="3" width="7" height="7" rx="1"/>
        <rect x="14" y="3" width="7" height="7" rx="1"/>
        <rect x="3" y="14" width="7" height="7" rx="1"/>
        <rect x="14" y="14" width="7" height="7" rx="1"/></svg>
      Project Management
    </span>
    <h3 style="font-size: 20px; font-weight: 600; letter-spacing: -0.025em;
      color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif;">Plan your project</h3>
    <p style="font-size: 16px; line-height: 1.6; color: #64748b; font-family: 'DM Sans', sans-serif;">
      Bring tasks, docs, and team communication into one place.</p>
    <button style="display: inline-flex; height: 40px; align-items: center; border-radius: 8px;
      background: #0f172a; padding: 0 24px; font-size: 14px; font-weight: 500; color: #f8fafc;
      cursor: pointer; transition: background 0.2s; font-family: 'DM Sans', sans-serif;">
      Get Started</button>
  </div>
</div>
```

---

## Quick Reference

```
READ    -> package.json, tailwind.config, existing fonts/icons
MATCH   -> Category Design Guide table
COMMIT  -> Tone + memorable element in one sentence
BUILD   -> Category palette + fonts + Taste Layer principles
CHECK   -> Pre-Delivery Checklist (no slop, no banned patterns)

BANNED  -> Inter, Roboto, Arial, purple gradients, emoji icons,
           empty heroes, 3-col card grids, thick gray borders,
           colored-circle avatars, pure #000/#FFF,
           blob trio heroes, nested glass, fake logos, generic SaaS copy

ALWAYS  -> Real SVG icons, tinted grays, CSS variables, responsive,
           prefers-reduced-motion, 4.5:1 contrast, cursor pointer,
           consistent max-width, distinctive font pairing,
           tokens over ripping UI kits, second-pass slop scan
```
