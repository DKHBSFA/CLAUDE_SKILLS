# Visual References System

Curated screenshot collection for UI pattern research.

---

## Purpose

Instead of searching online, Claude consults your curated screenshots. This ensures:
- Consistent visual language across the project
- Faster research phase (no web search needed)
- Your taste, not generic examples

---

## How to Use

### Adding References

1. **Capture** a screenshot of UI you like
2. **Name** it following the convention:
   ```
   [element]-[context]-[number].png

   Examples:
   hero-saas-dark-01.png
   nav-mobile-overlay-01.png
   card-product-minimal-01.png
   button-primary-hover-01.png
   ```
3. **Place** in `references/` folder
4. **Link** in the taxonomy file ([pages.md](taxonomy/pages.md) or [elements.md](taxonomy/elements.md))

### Invoking References

```
/ux-craft reference hero
/ux-craft reference navigation mobile
/ux-craft reference card product
```

Claude will:
1. Search taxonomy files for matching patterns
2. Display linked screenshots
3. Extract visual characteristics
4. Apply to subsequent generation

---

## Naming Convention

```
[elemento]-[contesto]-[variante]-[numero].png
```

| Part | Description | Examples |
|------|-------------|----------|
| elemento | UI element type | `hero`, `nav`, `card`, `button`, `form` |
| contesto | Use case or platform | `saas`, `ecommerce`, `mobile`, `desktop` |
| variante | Style variation (optional) | `dark`, `minimal`, `overlay`, `hover` |
| numero | Sequential number | `01`, `02`, `03` |

### Good Names

```
hero-saas-centered-01.png
nav-desktop-mega-01.png
card-product-hover-01.png
form-login-floating-01.png
modal-confirmation-01.png
```

### Bad Names

```
screenshot.png           # No context
hero.png                 # Missing specifics
New Screenshot 2024.png  # Spaces, no convention
IMG_1234.png            # Camera default
```

---

## Folder Structure

```
.claude/skills/ux-craft/
├── references.md           # This file
├── taxonomy/
│   ├── pages.md            # Page types → sections
│   └── elements.md         # Atomic elements → variants
└── references/
    ├── hero-saas-01.png
    ├── hero-ecommerce-01.png
    ├── nav-desktop-minimal-01.png
    ├── nav-mobile-overlay-01.png
    ├── card-product-01.png
    └── ...
```

---

## What Claude Can Extract

From a screenshot, Claude can identify:

| Extractable | Example |
|-------------|---------|
| Layout structure | "Split layout: text left, image right" |
| Visual hierarchy | "Large headline, smaller subhead, prominent CTA" |
| Spacing rhythm | "Generous whitespace, vertical rhythm" |
| Color relationships | "Dark background, light text, accent CTA" |
| Typography style | "Serif headlines, sans-serif body" |
| Component patterns | "Card grid with hover states" |

## What Claude Cannot Extract

| Not Extractable | Why |
|-----------------|-----|
| Exact hex codes | Vision approximates colors |
| Pixel measurements | Cannot measure precisely |
| Font names | Can describe style, not identify font |
| CSS values | Cannot reverse-engineer code |

**For exact values:** Use `system.md` tokens or export from Figma.

---

## Integration with Workflow

```
1. /ux-craft establish
   └── Creates system.md with exact tokens

2. /ux-craft reference [pattern]  ← NEW
   └── Shows visual inspiration

3. BUILD
   └── Generates code using:
       • Exact values from system.md
       • Visual style from references

4. /ux-craft audit
   └── Verifies consistency
```

---

## Best Practices

### Curating References

- **Quality over quantity**: 2-3 excellent examples beat 20 mediocre ones
- **Diverse contexts**: Include light/dark, desktop/mobile variants
- **Annotate**: Add notes in taxonomy about what makes each example good
- **Update**: Remove outdated references, add new inspiration

### Organizing

- Keep `references/` flat (no subfolders) for simplicity
- Use consistent naming so Claude can find patterns
- Link every reference in taxonomy files

### Using with system.md

References show *style*. `system.md` provides *values*.

```
Reference shows: "Generous spacing, rounded corners"
system.md defines: --space-4: 32px, --radius: 12px
```

Claude combines both: applies the spacing value in the visual style.

---

## Quick Start

1. Find 3-5 screenshots of UI you like
2. Name them properly
3. Drop in `references/`
4. Add links in `taxonomy/elements.md`
5. Try `/ux-craft reference [element]`

---

## Reference Index

*Screenshots in `references/` folder:*

| File | Element | Context | Notes |
|------|---------|---------|-------|
| *empty* | - | - | Add your first reference! |

Update this table as you add screenshots.
