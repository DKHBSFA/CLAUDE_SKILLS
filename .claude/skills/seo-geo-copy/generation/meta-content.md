# Meta Content Generation Prompt

## Pre-Generation Questions

### Required
1. **Page URL**: What page is this for?
2. **Page type**: Article, product, landing page, homepage, category?
3. **Primary keyword**: What should this page rank for?
4. **Page content summary**: Brief description of what's on the page

### Optional
5. **Brand name**: For title tag suffix
6. **Secondary keywords**: To incorporate if space allows
7. **Unique value prop**: What makes this page special?
8. **Target action**: What should searchers do? (learn, buy, compare, etc.)

---

## Title Tag Generation

### Rules
- **Length**: 50-60 characters (Google truncates at ~60)
- **Structure**: Primary keyword + modifier + brand (if fits)
- **Front-load**: Put keyword as close to beginning as possible
- **Unique**: No two pages should have identical titles

### Formulas by Page Type

**Article:**
```
[Primary Keyword]: [Promise/Benefit] | [Brand]
How to [Primary Keyword] in [Timeframe/Steps] | [Brand]
[Number] [Primary Keyword] [Tips/Strategies/Examples] ([Year])
```

**Product:**
```
[Product Name] - [Key Benefit] | [Brand]
[Product Name] | [Differentiator] | [Brand]
Buy [Product Name] - [Feature] | [Brand]
```

**Landing Page:**
```
[Primary Keyword] [Solution Type] | [Brand]
[Benefit Statement] - [Primary Keyword] | [Brand]
[Primary Keyword] for [Audience] | [Brand]
```

**Category:**
```
[Category Name] - [Browse/Shop] [Product Type] | [Brand]
[Adjective] [Category] [Products/Services] | [Brand]
```

**Homepage:**
```
[Brand] - [Primary Value Proposition]
[Brand] | [Tagline or Core Offering]
```

### Title Tag Don'ts
- No keyword stuffing
- No ALL CAPS (except acronyms)
- No special characters for attention (★, →, etc.)
- No duplicate titles across pages
- No vague titles ("Welcome", "Home", "Untitled")

---

## Meta Description Generation

### Rules
- **Length**: 150-160 characters
- **Include**: Primary keyword naturally
- **Include**: Clear value proposition
- **Include**: Call to action or next step
- **Tone**: Active voice, speaks to searcher

### Structure

```
[What the page offers] + [Key benefit/differentiator] + [CTA or outcome]
```

### Formulas by Page Type

**Article:**
```
Learn [topic] with our [comprehensive/step-by-step] guide. Discover [specific benefit] and [outcome]. [CTA: Read now, Get started, etc.]
```

**Product:**
```
[Product name] delivers [key benefit]. [Feature highlight]. [Trust signal: Free shipping, warranty, reviews]. [CTA: Shop now, Order today]
```

**Landing Page:**
```
[Pain point solution] with [product/service]. [Key differentiator]. [Social proof or guarantee]. [CTA: Get started, Try free, Learn more]
```

**Category:**
```
Browse our [adjective] selection of [category]. [Variety/quality statement]. [Trust signal]. [CTA: Shop now, Find yours]
```

### Meta Description Don'ts
- No deceptive descriptions (must match page content)
- No truncated sentences (complete your thought)
- No generic phrases ("Welcome to our website")
- No quotes (Google may strip them)
- No keyword stuffing

---

## Canonical URL

### Rules
- Always lowercase
- No trailing slashes (unless site standard)
- No URL parameters (use clean version)
- Specify protocol (https://)
- One canonical per page

### Format
```
<link rel="canonical" href="https://example.com/page-slug" />
```

---

## Open Graph Tags

Generate for social sharing:

```html
<meta property="og:title" content="[Title - can be longer than title tag, up to 95 chars]">
<meta property="og:description" content="[Description - up to 200 chars, can differ from meta]">
<meta property="og:type" content="[website|article|product]">
<meta property="og:url" content="[canonical URL]">
<meta property="og:image" content="[Image URL - 1200x630px ideal]">
<meta property="og:site_name" content="[Brand Name]">
```

For articles, add:
```html
<meta property="article:published_time" content="[ISO 8601 date]">
<meta property="article:author" content="[Author name or URL]">
```

---

## Twitter Card Tags

```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="[Same as OG title]">
<meta name="twitter:description" content="[Same as OG description]">
<meta name="twitter:image" content="[Same as OG image]">
```

---

## Output Checklist

### Title Tag (5 checks)
- [ ] Under 60 characters
- [ ] Primary keyword within first 30 characters
- [ ] Readable (not keyword-stuffed)
- [ ] Unique to this page
- [ ] Accurately describes page content

### Meta Description (5 checks)
- [ ] 150-160 characters
- [ ] Includes primary keyword
- [ ] Contains value proposition
- [ ] Has call to action
- [ ] Matches page content (not deceptive)

### Technical (4 checks)
- [ ] Canonical URL specified
- [ ] OG tags complete
- [ ] Twitter cards complete
- [ ] No duplicate meta across pages

---

## Example Output Format

```
## Meta Content for: [Page URL]

### Title Tag
`[Title here]`
Character count: [X]/60

### Meta Description
`[Description here]`
Character count: [X]/160

### Canonical
`<link rel="canonical" href="[URL]" />`

### Open Graph
```html
<meta property="og:title" content="[title]">
<meta property="og:description" content="[description]">
<meta property="og:type" content="[type]">
<meta property="og:url" content="[url]">
<meta property="og:image" content="[image-url]">
<meta property="og:site_name" content="[brand]">
```

### Twitter Card
```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="[title]">
<meta name="twitter:description" content="[description]">
<meta name="twitter:image" content="[image-url]">
```

---

### Validation Score

Title: X/5
Description: X/5
Technical: X/4
Total: X/14

Issues found:
- [List any failures]

### Alternative Options

**Title variants:**
1. [Alternative 1]
2. [Alternative 2]

**Description variants:**
1. [Alternative 1]
2. [Alternative 2]
```
