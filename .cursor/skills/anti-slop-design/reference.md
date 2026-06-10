# Anti-Slop Design Reference

Structural patterns, common mistakes, and starter tokens for the anti-slop-design skill. Read this file when building full pages, multi-section layouts, or design systems -- not for single-component work.

---

## Section Anatomy

These are structural skeletons, not templates. Adapt to the project's framework and styling approach. The point is the *structure and decisions*, not the exact code.

### Hero Section

A hero that avoids slop has these properties:

```
Structure:
  - Full viewport height (100svh or 100dvh), NOT min-height
  - Symmetric vertical padding for true optical centering
  - Content constrained to max-width container with consistent horizontal padding
  - ONE primary CTA + optional secondary CTA (not three buttons)
  - Visual fill: real photography, product screenshot, or decorative SVG/gradient -- never empty

Layout options (pick ONE per project, not the same every time):
  A. Split: text left, image/visual right (classic but effective)
  B. Centered: headline + CTA centered, background visual behind
  C. Asymmetric: text offset to one side, oversized image bleeding off-edge
  D. Editorial: massive typography IS the visual, minimal imagery
  E. Immersive: full-bleed image/video with text overlay

Common mistakes:
  - Using min-height instead of height (content not truly centered)
  - Forgetting pt-[header-height] when header is fixed/sticky
  - Hero padding different from other sections (edges don't align)
  - Decorative blurs/gradients that look identical across every generation
  - Stats row that's just three centered numbers (becomes a banned 3-col pattern)
```

### Product Grid (E-commerce)

```
Structure:
  - Category filter: horizontal scroll on mobile, wrapped on desktop
  - Grid: 1 col mobile, 2 col tablet, 3-4 col desktop
  - Cards: image-dominant (4:5 or 3:4 aspect ratio), info below
  - Quick-add visible on mobile without hover (touch has no hover state)
  - Stock/urgency signals near the product, not as a banner

Common mistakes:
  - Quick-add only appears on hover (invisible on mobile/touch)
  - Product images too small or square when portrait would sell better
  - Category filters that don't scroll on mobile (overflow hidden)
  - Repeating the same image for gallery thumbnails (lazy shortcut)
  - Missing cursor-pointer on clickable cards
```

### Features / Trust Banner

This is the single most common slop pattern. Three centered columns with icons and text.

```
WRONG (banned pattern):
  Three equal columns, centered icons, centered text, all same size.
  This is the #1 AI-generated layout. Avoid it.

BETTER alternatives:
  A. Inline strip: features as a horizontal row of icon+text pairs, no cards
  B. Asymmetric: one large feature left, two stacked right
  C. Integrated: features woven into the product section as small callouts
  D. Marquee: scrolling ticker of trust signals (logos, certifications)
  E. Contextual: shipping info near the cart, returns info near checkout
     (put trust signals WHERE they matter, not in a generic banner)

If you MUST use three columns:
  - Make them visually distinct (different sizes, colors, or weights)
  - Left-align the text
  - Use the category accent color for icons, not generic gray
  - Add a subtle background texture or gradient, not a flat color block
```

### Newsletter / CTA Section

```
Structure:
  - Short headline (not "Subscribe to our newsletter" -- that's generic)
  - One sentence of value proposition
  - Email input + submit button, inline on desktop, stacked on mobile
  - Constrained width (max-w-md or max-w-lg), not full-width

Common mistakes:
  - Generic "Subscribe" headline with no personality
  - Full-width input that looks like a search bar
  - No visual distinction from surrounding sections
  - Missing form label for accessibility (use sr-only label)
```

### Footer

```
Structure:
  - Same max-width container as all other sections
  - Logo + tagline, link columns, social icons, legal row
  - Dark background (primary color or near-black) for visual grounding

Common mistakes:
  - Different max-width than the rest of the page
  - Social icons as emoji instead of SVG
  - Too many link columns on mobile (should collapse or stack)
  - Missing aria-labels on icon-only social links
```

### Checkout Flow

```
Structure:
  - Progress indicator (step 1/2/3 or breadcrumb-style)
  - Form on left (60-70%), order summary on right (30-40%)
  - Summary sticky on desktop, collapsible on mobile
  - Clear total with shipping + tax breakdown
  - Security indicators near payment fields

Common mistakes:
  - No progress indication (user doesn't know how many steps remain)
  - Order summary hidden or at the bottom on mobile
  - Payment form without security/lock indicators
  - Submit button that doesn't disable during processing
  - Success state that's just text with no visual confirmation
```

---

## Common Mistakes by Category

These are the patterns models get wrong most often, even when following the skill.

### E-commerce

| Mistake | Why it happens | Fix |
|---------|---------------|-----|
| Three-column features banner | Models default to the most common layout in training data | Use inline strip, contextual placement, or asymmetric layout |
| Star ratings with yellow fill | Skill bans "5-star yellow rating widgets" but models generate them anyway | Use text reviews, review count badge, or a single aggregate score |
| Same image repeated as thumbnails | Lazy generation when only one product image exists | Skip the gallery entirely if there's only one image, or use different crop/angle |
| Mobile quick-add hidden behind hover | Hover doesn't exist on touch devices | Always show the add button on mobile; use hover reveal only on desktop |
| Generic "Shop Now" hero with no product | Hero should be product-led for e-commerce | Show an actual product image or collection in the hero |

### SaaS

| Mistake | Why it happens | Fix |
|---------|---------------|-----|
| Marketing-speak hero with no product screenshot | Models generate text-heavy heroes | Put a real product screenshot or demo above the fold |
| Pricing cards as three equal columns | Same banned pattern, different context | Use a comparison table, or highlight one plan with visual emphasis |
| Generic testimonial section | Stock avatar + quote in a card | Use real company logos, named individuals, specific metrics |
| Light mode default | Developer tools often work better in dark mode | Consider dark mode as primary, or offer both |

### Healthcare

| Mistake | Why it happens | Fix |
|---------|---------------|-----|
| Red as a primary or accent color | Models don't internalize that red triggers alarm in medical context | Use blue, teal, or green as primary; reserve red for errors only |
| Dense data tables for patient-facing pages | Models treat all healthcare as clinical dashboards | Simplify: cards, clear CTAs, large text, generous spacing |
| Stock photos of doctors with stethoscopes | Generic medical imagery | Use nature imagery, abstract organic shapes, or real facility photos |

### Agency / Creative

| Mistake | Why it happens | Fix |
|---------|---------------|-----|
| Template-looking grid layout | Models default to safe, predictable grids | Use experimental layouts: overlapping elements, scroll-driven animations, oversized typography |
| Listing services as bullet points | Text-heavy instead of visual | Show the work first; let case studies demonstrate capabilities |
| Conservative color palette | Models play it safe | Push hard: electric accents, dramatic contrast, bold typography at scale |

---

## CSS Token Starter

Use this as the foundation when generating a design system. Adapt the palette values from the Category Design Guide in SKILL.md.

### Tailwind v4 (`@theme` block)

```css
@import "tailwindcss";

@theme {
  /* Palette -- replace with category-specific values */
  --color-primary: #292524;
  --color-primary-light: #44403c;
  --color-surface: #faf9f6;
  --color-surface-alt: #f5f5f4;
  --color-surface-elevated: #ffffff;
  --color-accent: #f97316;
  --color-accent-hover: #ea580c;
  --color-accent-soft: #fff7ed;
  --color-text: #1c1917;
  --color-text-muted: #78716c;
  --color-text-inverse: #fafaf9;
  --color-border: #e7e5e4;
  --color-border-light: #f5f5f4;
  --color-success: #16a34a;
  --color-warning: #d97706;
  --color-error: #dc2626;

  /* Typography -- replace with category-specific fonts */
  --font-display: "Playfair Display", Georgia, serif;
  --font-body: "DM Sans", system-ui, sans-serif;
  --font-mono: "DM Mono", ui-monospace, monospace;

  /* Spacing (4px base) */
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
  --spacing-xl: 32px;
  --spacing-2xl: 48px;
  --spacing-3xl: 64px;
  --spacing-4xl: 96px;

  /* Border Radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;
  --radius-full: 9999px;

  /* Shadows */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.08);
  --shadow-lg: 0 8px 24px rgba(0, 0, 0, 0.12);
  --shadow-xl: 0 16px 48px rgba(0, 0, 0, 0.16);

  /* Motion */
  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
  --duration-fast: 150ms;
  --duration-normal: 300ms;
  --duration-slow: 500ms;
}
```

### Vanilla CSS (no Tailwind)

```css
:root {
  /* Same token names, works without Tailwind */
  --color-primary: #292524;
  --color-surface: #faf9f6;
  --color-accent: #f97316;
  --color-text: #1c1917;
  --color-text-muted: #78716c;
  --color-border: #e7e5e4;
  --color-success: #16a34a;
  --color-warning: #d97706;
  --color-error: #dc2626;

  --font-display: "Playfair Display", Georgia, serif;
  --font-body: "DM Sans", system-ui, sans-serif;

  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;

  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.08);
  --shadow-lg: 0 8px 24px rgba(0, 0, 0, 0.12);
}
```

### Google Fonts Import Pattern

```html
<!-- Preconnect for performance -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

<!-- Load display + body fonts -->
<link href="https://fonts.googleapis.com/css2?family=DISPLAY_FONT:wght@400;500;600;700&family=BODY_FONT:wght@400;500;600&display=swap" rel="stylesheet">
```

Replace `DISPLAY_FONT` and `BODY_FONT` with the category-specific fonts from the Category Design Guide.

---

## Base Component Patterns

These are structural patterns, not copy-paste code. Adapt to the project's framework.

### Container

Every section uses the same container for consistent edge alignment:

```css
.container-main {
  width: 100%;
  max-width: 1400px;    /* or 1200px for editorial/blog */
  margin: 0 auto;
  padding: 0 24px;      /* matches --spacing-lg */
}
```

### Button System

Minimum viable button set for most projects:

```
Variants needed:
  - primary:  solid background, inverse text (main CTA)
  - accent:   category accent color (secondary CTA)
  - outline:  transparent with border (tertiary action)
  - ghost:    transparent, no border (nav items, minor actions)

Every button must have:
  - cursor: pointer
  - transition on background/color/shadow (200-300ms)
  - hover state that changes more than just opacity
  - disabled state with reduced opacity and cursor: not-allowed
  - min-height 40px for touch targets (44px on mobile)
```

### Animation Utilities

Reusable entrance animations:

```css
/* Fade up (primary entrance) */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(20px); }
  to   { opacity: 1; transform: translateY(0); }
}

/* Fade in (simple reveal) */
@keyframes fadeIn {
  from { opacity: 0; }
  to   { opacity: 1; }
}

/* Scale in (modals, popovers) */
@keyframes scaleIn {
  from { opacity: 0; transform: scale(0.95); }
  to   { opacity: 1; transform: scale(1); }
}

/* Stagger delays */
.delay-100 { animation-delay: 100ms; }
.delay-200 { animation-delay: 200ms; }
.delay-300 { animation-delay: 300ms; }

/* Respect user preference */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## Mobile Responsive Strategy

Design mobile-first, then enhance for larger screens. The key decisions are: what to **hide**, what to **reorder**, and what to **transform**.

### What to HIDE on Mobile

| Element | Mobile behavior | Show from |
|---------|----------------|-----------|
| Hero background image (split layout) | Hide; let text fill the viewport | `lg` (1024px) |
| Stats row in hero (e.g. "50+ partners, 12K customers") | Hide; not essential for conversion | `md` (768px) |
| Desktop navigation links | Replace with hamburger menu | `lg` (1024px) |
| Hover-only quick actions (wishlist, quick-view icons) | Hide; no hover on touch | `md` (768px) |
| Sidebar filters | Hide behind a "Filters" button/drawer | `lg` (1024px) |
| Sticky product info panel | Don't stick; let it flow naturally | `lg` (1024px) |
| Multi-column footer link groups | Collapse into accordion or single column | `md` (768px) |
| Image gallery thumbnails | Hide if fewer than 3 unique images | `md` (768px) |
| Decorative background blurs/shapes | Reduce size and opacity, or hide | `md` (768px) |

### What to REORDER on Mobile

| Element | Desktop order | Mobile order | Why |
|---------|--------------|--------------|-----|
| Product image vs. info | Side by side | Image first, info below | Users need to see the product before reading details |
| Checkout form vs. summary | Form left, summary right | Summary first (collapsible), form below | User needs to confirm what they're buying |
| Hero CTA buttons | Inline row | Stacked vertically, full-width | Thumb-friendly, no overflow |
| Category filters | Wrapped row | Horizontal scroll strip | Fits more options without wrapping to 3+ rows |
| Footer columns | 4-column grid | Single column, stacked | Readability on narrow screens |
| Cart drawer | Side panel from right | Full-screen overlay or bottom sheet | More room for cart items |

### What to TRANSFORM on Mobile

| Element | Desktop | Mobile | Implementation |
|---------|---------|--------|----------------|
| Quick-add button | Appears on card hover | Always visible at card bottom | Remove the hover condition; show by default |
| Navigation | Horizontal link row | Hamburger + slide-out menu | `hidden lg:flex` for nav links, show hamburger below `lg` |
| Product grid | 3-4 columns | 1-2 columns | `grid-cols-1 sm:grid-cols-2 lg:grid-cols-4` |
| Font sizes | Display: 48-72px, Body: 16-18px | Display: 32-40px, Body: 15-16px | Use `text-4xl md:text-5xl lg:text-7xl` scaling |
| Section padding | `py-20` to `py-32` | `py-10` to `py-16` | `py-10 md:py-16 lg:py-20` |
| Hero height | `height: 100svh` | `min-height: 100dvh` with `pt-20` for fixed header | `100dvh` handles mobile browser chrome better |
| Features banner | 3-column grid | Single column with dividers, or horizontal scroll | `grid-cols-1 md:grid-cols-3` |
| Checkout layout | 2-column (form + summary) | Single column, summary collapsible at top | `grid-cols-1 lg:grid-cols-[1fr_400px]` |

### Mobile-First Verification

```
At 375px (small phone):
  [ ] Fixed header: logo + hamburger + cart fit in one row
  [ ] Hero: text readable, no overflow, CTA buttons stacked full-width
  [ ] No desktop-only content visible (stats, hover actions, sidebar)
  [ ] Cards: single column, quick-add visible without hover
  [ ] Forms: full-width inputs, visible labels, 44px min touch targets
  [ ] Footer: single column, social icons in one row
  [ ] No horizontal scroll on any section
  [ ] Font sizes reduced but still readable (min 15px body)

At 768px (tablet):
  [ ] Grid shifts to 2 columns
  [ ] Stats row and secondary content can appear
  [ ] Hero image can show alongside text
  [ ] Category filters can wrap instead of scroll

At 1024px+ (desktop):
  [ ] Full navigation visible, hamburger hidden
  [ ] Grid at 3-4 columns
  [ ] Hover states and quick actions active
  [ ] Sticky elements (cart summary, product info) work correctly
  [ ] Split layouts (hero, checkout) use side-by-side columns
```

---

## Rating and Social Proof Alternatives

The skill bans "5-star yellow rating widgets." Use these instead:

| Pattern | When to use | Example |
|---------|-------------|---------|
| **Aggregate score badge** | Product pages | `4.9 (128 reviews)` as text, no stars |
| **Review count link** | Product cards | `128 reviews` as an underlined link |
| **Named testimonial** | Landing pages | Real name + photo + specific quote + company |
| **Logo wall** | B2B / SaaS | Row of client logos (real SVGs from Simple Icons) |
| **Metric callout** | Trust sections | `12,000+ customers` or `$2M+ processed` as large text |
| **Review excerpt** | Product detail | Pull one specific sentence from a review, with attribution |

---

## Extended Slop Catalog

Use when auditing a full page or comparing two layout directions.

| Pattern | Why it reads as AI | Pivot |
|---------|-------------------|--------|
| Purple/pink/cyan blurred orb trio | Default hero background for years | One mesh gradient in brand hues, noise texture, or photography |
| "Integrations" row of same-size squares | Filler grid | Real logos with consistent monochrome treatment, or fewer larger marks |
| Pricing: three tiers, middle "Popular" | Template | Four tiers, usage-based row, or single CTA + "Contact" for enterprise |
| Testimonial carousel of faceless quotes | No credibility | Named photo + role + one specific outcome number |
| Dashboard: sidebar + top bar + three KPI cards | Boilerplate | Lead with the user's task; KPIs only if they change behavior |
| Sticky "Book a demo" on every scroll | Aggressive B2B default | One clear nav CTA + contextual CTA in hero and footer |
| Dark theme + neon purple CTA only | Crypto/template | Category navy/teal/gold; neon only for entertainment/gaming |
| Identical `rounded-2xl` on every surface | Card soup | Mix: full-bleed sections, flush tables, one elevated panel |
| Chart with random upward curve | Misleading | Real axis labels, source, or remove chart |
| Colored `border-left` stripe on cards/alerts | The default "status accent" | Full border, background tint, or leading icon |
| Gradient `background-clip: text` headline | Decorative, never meaningful | Solid color; emphasis via weight or size |
| Big-number hero-metric card grid | SaaS dashboard cliché | Lead with the user's task; metrics inline with context and trend |
| Card nested inside a card | Double-boxed grouping | Flatten; separate with background shift or whitespace |
| Modal for every interaction | Laziness pattern | Inline editing, expandable rows, progressive disclosure first |

---

## Microcopy And State Patterns

Replace generic strings with **specific + actionable** lines. Adapt voice to category (SaaS: crisp; wellness: warm; legal: calm).

### Empty states

| Weak | Stronger |
|------|----------|
| No items | No projects yet — create one to see your timeline here. |
| No results | No matches for "[query]". Try fewer filters or a different keyword. |
| Nothing to show | Connect your calendar to surface upcoming meetings. |

### Errors

| Weak | Stronger |
|------|----------|
| Something went wrong | We couldn't save. Check your connection and try again. |
| Error 500 | This page failed to load. Refresh or return home. |
| Invalid input | Enter a date in the future. |

### Loading

- Skeleton **aspect ratio** should match the real card row or table row.
- Prefer **one** shimmer region per viewport focal area, not the entire page pulsing.

### Headline / CTA clichés to rewrite

| Generic | Direction |
|---------|-----------|
| Empower your team | State the outcome: "Ship releases on schedule" |
| The future of X | Name the problem: "Stop losing leads after the demo" |
| Get started today | Action + object: "Import your first spreadsheet" |
| All-in-one platform | One concrete capability per line instead |

---

## Theme Integration (shadcn / Tailwind v4)

When extending an existing kit:

1. Map category **primary** to `--primary` (or your project's brand token); keep destructive/success semantic.
2. **Radius**: pick one scale (`sm` / `md` / `lg`) and apply consistently — avoid mixing pill buttons with sharp tables unless intentional.
3. **Dark mode**: define `--background` and `--foreground` pairs that pass contrast; muted text should not dip below ~4.5:1 on body.
4. New marketing sections should **import** the same font variables the app shell uses unless the brief asks for a separate landing aesthetic.

---

## When NOT to Read This File

- Single-component work (a button, a card, a form field) -- SKILL.md is enough
- Canvas demos or standalone HTML -- no project context to match
- The user explicitly says "keep it simple" or "just the component"

Only read this reference when building full pages, multi-section layouts, or complete design systems.
