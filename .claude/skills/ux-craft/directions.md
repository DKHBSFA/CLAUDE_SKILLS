# Design Directions

Six distinct visual personalities. Choose one as your foundation.

---

## 1. Precision & Density

**Personality**: Technical, monochrome, information-dense
**Best For**: Developer dashboards, admin panels, data tables, IDE-style interfaces

### Visual Signature
- Tight spacing (4px base grid)
- Borders over shadows
- Monochrome with single accent
- Small, dense typography
- Maximum information per viewport

### Token Preset
```css
/* Precision & Density */
--space-base: 4px;
--radius: 2px;
--shadow: none;
--border: 1px solid var(--color-border);

/* Typography */
--font-display: "JetBrains Mono", "Fira Code", monospace;
--font-body: "IBM Plex Sans", system-ui;
--text-base: 0.8125rem; /* 13px - dense */

/* Colors */
--color-bg: hsl(220 15% 8%);
--color-surface: hsl(220 15% 12%);
--color-border: hsl(220 10% 25%);
--color-text: hsl(220 10% 85%);
--color-accent: hsl(200 80% 55%); /* Cyan accent */
```

### Example Elements
```css
.data-cell {
  padding: var(--space-1) var(--space-2); /* 4px 8px */
  border-bottom: var(--border);
  font-size: var(--text-base);
  font-family: var(--font-body);
  font-variant-numeric: tabular-nums;
}

.status-badge {
  padding: 2px 6px;
  border-radius: var(--radius);
  font-size: 0.6875rem;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
```

---

## 2. Warmth & Approachability

**Personality**: Soft, generous, friendly, inviting
**Best For**: Consumer apps, onboarding flows, marketing sites, community platforms

### Visual Signature
- Generous spacing (8px base, scale up quickly)
- Soft shadows, no hard edges
- Warm color palette
- Large, friendly typography
- Rounded corners, organic shapes

### Token Preset
```css
/* Warmth & Approachability */
--space-base: 8px;
--radius: 12px;
--radius-full: 9999px;

/* Shadows - soft and diffuse */
--shadow-sm: 0 1px 3px hsl(var(--shadow-color) / 0.08);
--shadow-md: 0 4px 12px hsl(var(--shadow-color) / 0.1);
--shadow-lg: 0 12px 32px hsl(var(--shadow-color) / 0.12);

/* Typography */
--font-display: "Bricolage Grotesque", "DM Sans", sans-serif;
--font-body: "Source Sans 3", "Inter", sans-serif;
--text-base: 1rem;
--line-height: 1.6;

/* Colors - warm foundation */
--color-bg: hsl(30 20% 98%);
--color-surface: hsl(0 0% 100%);
--color-text: hsl(20 15% 20%);
--color-accent: hsl(25 90% 55%); /* Warm orange */
--color-success: hsl(145 60% 42%);
--shadow-color: 20 30% 20%;
```

### Example Elements
```css
.card-friendly {
  padding: var(--space-5); /* 40px */
  background: var(--color-surface);
  border-radius: var(--radius);
  box-shadow: var(--shadow-md);
}

.button-primary {
  padding: var(--space-2) var(--space-4); /* 16px 32px */
  background: var(--color-accent);
  border-radius: var(--radius-full);
  font-weight: 600;
  font-size: 1rem;
  transition: transform 150ms ease, box-shadow 150ms ease;
}

.button-primary:hover {
  transform: translateY(-1px);
  box-shadow: var(--shadow-lg);
}
```

---

## 3. Sophistication & Trust

**Personality**: Cool, layered, premium, institutional
**Best For**: Finance apps, enterprise SaaS, legal/healthcare, luxury brands

### Visual Signature
- Balanced spacing (8px base)
- Layered depth with subtle gradients
- Cool, muted color palette
- Formal typography hierarchy
- Subtle backgrounds, glass effects

### Token Preset
```css
/* Sophistication & Trust */
--space-base: 8px;
--radius: 8px;

/* Shadows - crisp and layered */
--shadow-sm: 0 1px 2px hsl(220 30% 10% / 0.05);
--shadow-md: 0 2px 8px hsl(220 30% 10% / 0.08),
             0 1px 2px hsl(220 30% 10% / 0.04);
--shadow-lg: 0 8px 24px hsl(220 30% 10% / 0.12),
             0 2px 8px hsl(220 30% 10% / 0.06);

/* Typography */
--font-display: "Playfair Display", "Libre Baskerville", serif;
--font-body: "Source Sans 3", "Lato", sans-serif;
--text-base: 0.9375rem; /* 15px */
--letter-spacing-display: -0.02em;

/* Colors - cool foundation */
--color-bg: hsl(220 20% 97%);
--color-surface: hsl(0 0% 100%);
--color-surface-elevated: hsl(220 30% 99%);
--color-text: hsl(220 20% 15%);
--color-text-muted: hsl(220 15% 45%);
--color-accent: hsl(220 70% 50%); /* Trust blue */
--color-accent-subtle: hsl(220 70% 96%);
```

### Example Elements
```css
.card-elevated {
  padding: var(--space-5);
  background: linear-gradient(
    135deg,
    var(--color-surface) 0%,
    var(--color-surface-elevated) 100%
  );
  border: 1px solid hsl(220 20% 92%);
  border-radius: var(--radius);
  box-shadow: var(--shadow-md);
}

.heading-display {
  font-family: var(--font-display);
  font-weight: 600;
  letter-spacing: var(--letter-spacing-display);
  color: var(--color-text);
}

.stat-value {
  font-family: var(--font-display);
  font-size: 2.5rem;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.03em;
}
```

---

## 4. Data & Analysis

**Personality**: Chart-optimized, numbers-first, analytical
**Best For**: Analytics dashboards, BI tools, scientific applications, trading platforms

### Visual Signature
- Dense but readable (4px base)
- High contrast for data clarity
- Color-coded semantic meaning
- Tabular typography
- Grid-aligned layouts

### Token Preset
```css
/* Data & Analysis */
--space-base: 4px;
--radius: 4px;

/* Typography - optimized for numbers */
--font-display: "Inter", "SF Pro Display", sans-serif;
--font-body: "Inter", "SF Pro Text", sans-serif;
--font-mono: "JetBrains Mono", "SF Mono", monospace;
--text-base: 0.875rem;

/* Data colors - semantic and distinguishable */
--color-positive: hsl(145 70% 42%);
--color-negative: hsl(0 75% 55%);
--color-neutral: hsl(220 10% 50%);
--color-warning: hsl(35 90% 50%);

/* Chart palette - colorblind safe */
--chart-1: hsl(220 70% 55%);
--chart-2: hsl(160 60% 45%);
--chart-3: hsl(35 90% 55%);
--chart-4: hsl(280 60% 55%);
--chart-5: hsl(0 70% 55%);
--chart-6: hsl(180 50% 45%);

/* Background */
--color-bg: hsl(220 15% 10%);
--color-surface: hsl(220 15% 14%);
--color-surface-elevated: hsl(220 15% 18%);
--color-border: hsl(220 10% 25%);
--color-text: hsl(220 10% 90%);
```

### Example Elements
```css
.metric-card {
  padding: var(--space-3);
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
}

.metric-value {
  font-family: var(--font-mono);
  font-size: 1.75rem;
  font-weight: 600;
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.02em;
}

.metric-change-positive {
  color: var(--color-positive);
}

.metric-change-negative {
  color: var(--color-negative);
}

.data-table {
  font-variant-numeric: tabular-nums;
  border-collapse: collapse;
}

.data-table td {
  padding: var(--space-2);
  border-bottom: 1px solid var(--color-border);
  text-align: right; /* Numbers align right */
}
```

---

## 5. Utility & Function

**Personality**: Muted, functional, no-nonsense
**Best For**: GitHub-style tools, documentation, CLIs with web UI, developer utilities

### Visual Signature
- Minimal decoration
- Functional color only
- Dense, scannable layouts
- Monospace where appropriate
- No shadows, minimal radius

### Token Preset
```css
/* Utility & Function */
--space-base: 4px;
--radius: 6px;
--border: 1px solid var(--color-border);

/* Typography */
--font-display: "Inter", system-ui;
--font-body: "Inter", system-ui;
--font-mono: "JetBrains Mono", "Consolas", monospace;
--text-base: 0.875rem;
--line-height: 1.5;

/* Colors - muted and functional */
--color-bg: hsl(210 20% 98%);
--color-surface: hsl(0 0% 100%);
--color-border: hsl(210 15% 85%);
--color-text: hsl(210 10% 20%);
--color-text-muted: hsl(210 10% 50%);
--color-accent: hsl(210 100% 45%);

/* Semantic only */
--color-success: hsl(140 60% 35%);
--color-warning: hsl(40 90% 45%);
--color-error: hsl(0 70% 50%);
--color-info: hsl(200 80% 45%);
```

### Example Elements
```css
.toolbar {
  display: flex;
  gap: var(--space-2);
  padding: var(--space-2) var(--space-3);
  background: var(--color-surface);
  border-bottom: var(--border);
}

.button-utility {
  padding: var(--space-1) var(--space-2);
  background: transparent;
  border: var(--border);
  border-radius: var(--radius);
  font-size: var(--text-sm);
  color: var(--color-text);
  cursor: pointer;
}

.button-utility:hover {
  background: var(--color-bg);
}

.code-block {
  padding: var(--space-3);
  background: hsl(210 20% 96%);
  border-radius: var(--radius);
  font-family: var(--font-mono);
  font-size: 0.8125rem;
  overflow-x: auto;
}
```

---

## 6. Expressive & Bold

**Personality**: Vibrant, dynamic, personality-driven
**Best For**: Creative apps, portfolios, entertainment, marketing campaigns

### Visual Signature
- Bold color choices
- Dynamic motion and interaction
- Asymmetric layouts
- Display typography as hero
- Playful shadows and effects

### Token Preset
```css
/* Expressive & Bold */
--space-base: 8px;
--radius: 16px;
--radius-blob: 40% 60% 70% 30% / 40% 50% 60% 50%;

/* Shadows - dramatic */
--shadow-glow: 0 0 40px hsl(var(--accent-hue) 80% 50% / 0.3);
--shadow-dramatic:
  0 4px 6px hsl(0 0% 0% / 0.1),
  0 12px 24px hsl(0 0% 0% / 0.15),
  0 24px 48px hsl(0 0% 0% / 0.1);

/* Typography */
--font-display: "Bricolage Grotesque", "Syne", sans-serif;
--font-body: "DM Sans", "Inter", sans-serif;
--text-display: clamp(2.5rem, 8vw, 6rem);
--letter-spacing-display: -0.04em;

/* Colors - vibrant */
--accent-hue: 280; /* Purple base, easily changeable */
--color-accent: hsl(var(--accent-hue) 80% 60%);
--color-accent-light: hsl(var(--accent-hue) 80% 75%);
--color-accent-dark: hsl(var(--accent-hue) 80% 45%);

--color-bg: hsl(260 30% 8%);
--color-surface: hsl(260 25% 12%);
--color-text: hsl(0 0% 98%);

/* Gradients */
--gradient-hero: linear-gradient(
  135deg,
  hsl(280 80% 60%) 0%,
  hsl(320 80% 55%) 50%,
  hsl(30 90% 60%) 100%
);
```

### Example Elements
```css
.hero-heading {
  font-family: var(--font-display);
  font-size: var(--text-display);
  font-weight: 800;
  letter-spacing: var(--letter-spacing-display);
  line-height: 0.95;
  background: var(--gradient-hero);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.card-expressive {
  padding: var(--space-6);
  background: var(--color-surface);
  border-radius: var(--radius);
  box-shadow: var(--shadow-dramatic);
  transition: transform 300ms cubic-bezier(0.34, 1.56, 0.64, 1);
}

.card-expressive:hover {
  transform: translateY(-8px) scale(1.02);
}

.button-bold {
  padding: var(--space-3) var(--space-5);
  background: var(--gradient-hero);
  border: none;
  border-radius: var(--radius);
  font-weight: 700;
  font-size: 1.125rem;
  color: white;
  cursor: pointer;
  box-shadow: var(--shadow-glow);
  transition: transform 200ms ease, box-shadow 200ms ease;
}

.button-bold:hover {
  transform: scale(1.05);
  box-shadow: 0 0 60px hsl(var(--accent-hue) 80% 50% / 0.5);
}

/* Staggered reveal animation */
@keyframes reveal {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.reveal-item {
  animation: reveal 600ms cubic-bezier(0.22, 1, 0.36, 1) forwards;
  animation-delay: calc(var(--index, 0) * 100ms);
  opacity: 0;
}
```

---

## Direction Selection Guide

| If your project needs... | Choose |
|--------------------------|--------|
| Maximum data density | **Precision & Density** |
| User trust and comfort | **Warmth & Approachability** |
| Professional credibility | **Sophistication & Trust** |
| Data visualization focus | **Data & Analysis** |
| Developer tool aesthetic | **Utility & Function** |
| Brand personality | **Expressive & Bold** |

---

## Combining Directions

You can blend directions for specific contexts:

**Dashboard with friendly onboarding:**
- Main: Data & Analysis
- Onboarding modals: Warmth & Approachability

**Enterprise app with data views:**
- Chrome/navigation: Sophistication & Trust
- Data tables: Precision & Density

**Developer tool with marketing:**
- App: Utility & Function
- Landing page: Expressive & Bold
