# Design System - Consumer App

## Direction
**Personality**: Warmth & Approachability
**Foundation**: Warm (sand/peach)
**Depth**: Soft shadows

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
--font-display: "Bricolage Grotesque", "DM Sans", sans-serif;
--font-body: "Source Sans 3", system-ui, sans-serif;
--font-mono: "JetBrains Mono", monospace;

/* Scale */
--text-sm: 0.875rem;
--text-base: 1rem;
--text-lg: 1.125rem;
--text-xl: 1.25rem;
--text-2xl: 1.5rem;
--text-3xl: 2rem;
--text-4xl: 2.5rem;

/* Weights */
--font-normal: 400;
--font-medium: 500;
--font-semibold: 600;
--font-bold: 700;
--font-extrabold: 800;
```

### Colors
```css
/* Background */
--color-bg: hsl(30 20% 97%);
--color-surface: hsl(0 0% 100%);
--color-surface-elevated: hsl(30 30% 99%);

/* Text */
--color-text: hsl(25 20% 15%);
--color-text-muted: hsl(25 10% 40%);

/* Accent */
--color-accent: hsl(25 90% 55%);
--color-accent-light: hsl(25 90% 65%);
--color-accent-subtle: hsl(25 50% 95%);

/* Semantic */
--color-success: hsl(145 55% 42%);
--color-warning: hsl(40 90% 50%);
--color-error: hsl(0 65% 50%);

/* Shadow tint */
--shadow-color: 25 30% 20%;
```

### Shadows
```css
--shadow-sm: 0 1px 3px hsl(var(--shadow-color) / 0.06);
--shadow-md:
  0 2px 4px hsl(var(--shadow-color) / 0.04),
  0 4px 12px hsl(var(--shadow-color) / 0.08);
--shadow-lg:
  0 4px 8px hsl(var(--shadow-color) / 0.04),
  0 12px 32px hsl(var(--shadow-color) / 0.1);
```

### Borders
```css
--radius: 12px;
--radius-lg: 16px;
--radius-full: 9999px;
```

---

## Component Patterns

### Card
```css
.card {
  padding: var(--space-4);
  background: var(--color-surface);
  border-radius: var(--radius);
  box-shadow: var(--shadow-md);
}
```

### Button Primary
```css
.btn-primary {
  padding: var(--space-2) var(--space-4);
  font-size: var(--text-base);
  font-weight: var(--font-semibold);
  background: var(--color-accent);
  color: white;
  border: none;
  border-radius: var(--radius-full);
  min-height: 48px;
  transition: transform 150ms ease, box-shadow 150ms ease;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}

.btn-primary:focus-visible {
  outline: 3px solid var(--color-accent-light);
  outline-offset: 2px;
}
```

### Input
```css
.input {
  padding: var(--space-2);
  font-size: var(--text-base);
  background: var(--color-bg);
  border: 2px solid transparent;
  border-radius: var(--radius);
  min-height: 48px;
  transition: border-color 150ms ease;
}

.input:focus {
  border-color: var(--color-accent);
  outline: none;
}
```

---

## Notes
- Generous whitespace
- Rounded, soft shapes
- Warm, inviting colors
- Smooth, friendly interactions
