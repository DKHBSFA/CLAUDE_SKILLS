# Design System - Developer Dashboard

## Direction
**Personality**: Precision & Density
**Foundation**: Cool (slate)
**Depth**: Borders only (no shadows)

---

## Tokens

### Spacing (4px base)
```css
--space-1: 4px;
--space-2: 8px;
--space-3: 12px;
--space-4: 16px;
--space-5: 24px;
--space-6: 32px;
--space-7: 48px;
--space-8: 64px;
```

### Typography
```css
/* Fonts */
--font-display: "JetBrains Mono", "Fira Code", monospace;
--font-body: "IBM Plex Sans", system-ui, sans-serif;
--font-mono: "JetBrains Mono", monospace;

/* Scale */
--text-xs: 0.6875rem;   /* 11px */
--text-sm: 0.75rem;     /* 12px */
--text-base: 0.8125rem; /* 13px */
--text-lg: 0.875rem;    /* 14px */
--text-xl: 1rem;        /* 16px */
--text-2xl: 1.25rem;    /* 20px */

/* Weights */
--font-normal: 400;
--font-medium: 500;
--font-semibold: 600;
```

### Colors
```css
/* Background */
--color-bg: hsl(220 15% 8%);
--color-surface: hsl(220 15% 12%);
--color-surface-elevated: hsl(220 15% 16%);

/* Border */
--color-border: hsl(220 10% 22%);
--color-border-subtle: hsl(220 10% 18%);

/* Text */
--color-text: hsl(220 10% 85%);
--color-text-muted: hsl(220 10% 55%);
--color-text-subtle: hsl(220 10% 40%);

/* Accent */
--color-accent: hsl(200 80% 55%);
--color-accent-muted: hsl(200 60% 35%);

/* Semantic */
--color-success: hsl(145 60% 45%);
--color-warning: hsl(40 90% 50%);
--color-error: hsl(0 70% 55%);
--color-info: hsl(200 80% 55%);
```

### Borders
```css
--border: 1px solid var(--color-border);
--border-subtle: 1px solid var(--color-border-subtle);
--radius: 2px;
```

---

## Component Patterns

### Data Table Cell
```css
.cell {
  padding: var(--space-1) var(--space-2);
  font-size: var(--text-base);
  font-variant-numeric: tabular-nums;
  border-bottom: var(--border-subtle);
}
```

### Status Badge
```css
.badge {
  padding: 2px 6px;
  font-size: var(--text-xs);
  font-weight: var(--font-medium);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  border-radius: var(--radius);
  border: var(--border);
}
```

### Button
```css
.btn {
  padding: var(--space-1) var(--space-3);
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
  border: var(--border);
  border-radius: var(--radius);
  background: var(--color-surface);
  min-height: 28px;
}

.btn:hover {
  background: var(--color-surface-elevated);
}

.btn:focus-visible {
  outline: 2px solid var(--color-accent);
  outline-offset: 1px;
}
```

---

## Notes
- Maximize information density
- Tabular numbers everywhere
- Monospace for technical data
- Minimal visual noise
