# Page Taxonomy

Archetypal page types decomposed into sections. Each section links to visual references.

---

## Homepage / Landing Page

The entry point. Must communicate value proposition immediately.

### Sections

| Section | Purpose | References |
|---------|---------|------------|
| Navigation | Primary wayfinding | [nav-desktop-minimal-01.png](../references/nav-desktop-minimal-01.png) |
| Hero | Value proposition, primary CTA | [hero-saas-01.png](../references/hero-saas-01.png) |
| Social Proof | Trust signals (logos, testimonials) | *add references* |
| Features | Product capabilities | *add references* |
| How It Works | Process explanation | *add references* |
| Pricing | Plan comparison | *add references* |
| CTA Section | Conversion push | *add references* |
| Footer | Secondary navigation, legal | *add references* |

### Layout Patterns

- **F-pattern**: Logo top-left, nav top-right, content flows left-to-right
- **Z-pattern**: Hero headline → image → features → CTA
- **Single column**: Mobile-first, stacked sections

---

## Product Listing / Catalog

Browse and filter collections of items.

### Sections

| Section | Purpose | References |
|---------|---------|------------|
| Filter Bar | Narrow results | *add references* |
| Sort Controls | Order results | *add references* |
| Product Grid | Display items | *add references* |
| Pagination | Navigate pages | *add references* |
| Empty State | No results | *add references* |

### Layout Patterns

- **Grid**: 3-4 columns desktop, 2 columns tablet, 1 column mobile
- **List**: Full-width cards with horizontal layout
- **Masonry**: Pinterest-style variable heights

---

## Product Detail

Single item focus with purchase intent.

### Sections

| Section | Purpose | References |
|---------|---------|------------|
| Image Gallery | Product visuals | *add references* |
| Product Info | Title, price, description | *add references* |
| Variant Selector | Size, color, options | *add references* |
| Add to Cart | Primary action | *add references* |
| Product Tabs | Details, specs, reviews | *add references* |
| Related Products | Cross-sell | *add references* |

---

## Dashboard

Data overview and quick actions.

### Sections

| Section | Purpose | References |
|---------|---------|------------|
| Sidebar | Navigation | *add references* |
| Header | Search, user, notifications | *add references* |
| Metrics Row | KPIs at a glance | *add references* |
| Charts | Data visualization | *add references* |
| Activity Feed | Recent events | *add references* |
| Quick Actions | Common tasks | *add references* |

---

## Settings / Profile

User preferences and account management.

### Sections

| Section | Purpose | References |
|---------|---------|------------|
| Settings Nav | Category navigation | *add references* |
| Form Sections | Input groups | *add references* |
| Avatar Upload | Profile image | *add references* |
| Danger Zone | Destructive actions | *add references* |

---

## Authentication

Login, signup, password flows.

### Sections

| Section | Purpose | References |
|---------|---------|------------|
| Auth Card | Centered form container | *add references* |
| Social Login | OAuth buttons | *add references* |
| Divider | "or" separator | *add references* |
| Form Fields | Email, password inputs | *add references* |
| Submit Button | Primary action | *add references* |
| Links | Forgot password, signup | *add references* |

---

## Checkout

Multi-step purchase flow.

### Sections

| Section | Purpose | References |
|---------|---------|------------|
| Progress Bar | Step indicator | *add references* |
| Cart Summary | Order review | *add references* |
| Shipping Form | Address input | *add references* |
| Payment Form | Card details | *add references* |
| Order Confirmation | Success state | *add references* |

---

## Documentation

Technical content and guides.

### Sections

| Section | Purpose | References |
|---------|---------|------------|
| Doc Sidebar | Navigation tree | *add references* |
| Breadcrumbs | Location context | *add references* |
| Content Area | Markdown/prose | *add references* |
| Table of Contents | In-page nav | *add references* |
| Code Blocks | Syntax highlighted | *add references* |
| Callouts | Warnings, tips, notes | *add references* |

---

## Error States

404, 500, maintenance pages.

### Sections

| Section | Purpose | References |
|---------|---------|------------|
| Error Illustration | Visual indicator | *add references* |
| Error Message | What happened | *add references* |
| Recovery Actions | How to proceed | *add references* |

---

## Adding References

To add a reference:

1. Take/find a screenshot of the section
2. Name it: `[section]-[context]-[number].png`
3. Place in `references/` folder
4. Update this file with the path

Example:
```markdown
| Hero | Value proposition | [hero-saas-01.png](../references/hero-saas-01.png) |
```
