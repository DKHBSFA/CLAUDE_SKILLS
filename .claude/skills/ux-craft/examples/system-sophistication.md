# Design System - Finance Platform

## Direction
**Personality**: Sophistication & Trust
**Foundation**: Cool (slate/blue)
**Depth**: Layered surfaces with subtle gradients

---

## Tokens

### Spacing (8px base)
```css
--space-1: 8px;
--space-2: 16px;
--space-3: 24px;
--space-4: 32px;
--space-5: 48px;
--space-6: 64px;
--space-7: 96px;
--space-8: 128px;
```

### Typography
```css
/* Fonts */
--font-display: "Playfair Display", "Libre Baskerville", serif;
--font-body: "Source Sans 3", "Lato", sans-serif;
--font-mono: "JetBrains Mono", monospace;

/* Scale */
--text-sm: 0.875rem;
--text-base: 0.9375rem;
--text-lg: 1.0625rem;
--text-xl: 1.25rem;
--text-2xl: 1.5rem;
--text-3xl: 2rem;
--text-4xl: 2.5rem;
--text-5xl: 3.5rem;

/* Weights */
--font-normal: 400;
--font-medium: 500;
--font-semibold: 600;
--font-bold: 700;
```

### Colors
```css
/* Background */
--color-bg: hsl(220 20% 96%);
--color-surface: hsl(0 0% 100%);
--color-surface-elevated: hsl(220 30% 99%);

/* Text */
--color-text: hsl(220 25% 12%);
--color-text-muted: hsl(220 15% 45%);
--color-text-subtle: hsl(220 10% 60%);

/* Accent - Trust blue */
--color-accent: hsl(220 70% 50%);
--color-accent-light: hsl(220 70% 60%);
--color-accent-subtle: hsl(220 60% 96%);
--color-accent-dark: hsl(220 70% 40%);

/* Semantic */
--color-success: hsl(160 60% 38%);
--color-warning: hsl(40 90% 48%);
--color-error: hsl(0 65% 48%);

/* Shadow */
--shadow-color: 220 30% 10%;
```

### Shadows
```css
--shadow-sm:
  0 1px 2px hsl(var(--shadow-color) / 0.04);
--shadow-md:
  0 2px 4px hsl(var(--shadow-color) / 0.03),
  0 4px 8px hsl(var(--shadow-color) / 0.06);
--shadow-lg:
  0 4px 8px hsl(var(--shadow-color) / 0.03),
  0 8px 16px hsl(var(--shadow-color) / 0.06),
  0 16px 32px hsl(var(--shadow-color) / 0.06);
```

### Borders
```css
--border: 1px solid hsl(220 20% 90%);
--radius: 8px;
--radius-lg: 12px;
```

---

## Component Patterns

### Card Elevated
```css
.card {
  padding: var(--space-4);
  background: linear-gradient(
    135deg,
    var(--color-surface) 0%,
    var(--color-surface-elevated) 100%
  );
  border: var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow-md);
}
```

### Stat Display
```css
.stat-value {
  font-family: var(--font-display);
  font-size: var(--text-4xl);
  font-weight: var(--font-bold);
  letter-spacing: -0.02em;
  font-variant-numeric: tabular-nums;
  color: var(--color-text);
}

.stat-label {
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--color-text-muted);
}
```

### Button
```css
.btn-primary {
  padding: var(--space-2) var(--space-4);
  font-size: var(--text-base);
  font-weight: var(--font-semibold);
  background: var(--color-accent);
  color: white;
  border: none;
  border-radius: var(--radius);
  min-height: 44px;
  transition: background 150ms ease;
}

.btn-primary:hover {
  background: var(--color-accent-dark);
}

.btn-primary:focus-visible {
  outline: 2px solid var(--color-accent);
  outline-offset: 2px;
}

.btn-secondary {
  padding: var(--space-2) var(--space-4);
  font-size: var(--text-base);
  font-weight: var(--font-medium);
  background: transparent;
  color: var(--color-accent);
  border: 1px solid var(--color-accent);
  border-radius: var(--radius);
  min-height: 44px;
}
```

---

## Notes
- Serif for display, sans for body
- Layered depth creates trust
- Muted, professional palette
- Formal spacing and typography
