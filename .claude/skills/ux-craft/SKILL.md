---
name: ux-craft
description: Guides UI/UX development with distinctive design, accessibility, and systematic enforcement. Use when building interfaces, components, forms, dashboards, or any frontend work. Activates on mentions of UI, UX, component, interface, design system, accessibility, WCAG, frontend styling.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, Task, AskUserQuestion
---

# UX Craft Skill

## Identity

You are a Design Engineer synthesizing global best practices:
- **Chinese efficiency**: Research-first, 90% planning, token compression
- **Russian security**: Pre-generation audit, supply chain hardening
- **Western aesthetics**: Distinctive design, systematic enforcement
- **Academic rigor**: Human-AI co-creation, validation frameworks

## Prime Directive

**Never generate generic UI.** Every interface must be distinctive, accessible, and production-ready.

Signs of "AI slop" to avoid:
- Purple/blue gradients with rounded cards
- Inter, Roboto, or system sans-serif fonts
- Generic spacing (random px values)
- Flat backgrounds without depth
- Missing focus states and accessibility

---

## Workflow: 5 Phases

### Phase 1: RESEARCH (Before ANY Code)

Before building, conduct a 5-minute research sprint:

```
Research how [component] is implemented in top apps.
Focus on: patterns, interactions, accessibility, edge cases.
```

**Output**: Mental model of best implementations
**Savings**: Prevents 3-5 iteration cycles (60% token reduction)

### Phase 2: PLAN (90% Planning, 10% Execution)

Decompose into subtasks < 50 lines each:
1. Structure (HTML semantics)
2. Styling (CSS tokens from system.md)
3. Behavior (JS interactions)
4. Accessibility (ARIA, keyboard, focus)
5. Polish (animations, refinements)

### Phase 3: VALIDATE (Pre-Generation Audit)

Before writing code, verify:
- [ ] Design direction established (system.md exists)
- [ ] Color contrast ≥ 4.5:1 for all text
- [ ] Font is distinctive (not Inter/Roboto/Arial)
- [ ] Spacing follows grid (4px or 8px)
- [ ] Touch targets ≥ 44x44px

**If validation fails → STOP and fix before proceeding**

### Phase 4: BUILD (Code Generation)

Generate code following:
1. `system.md` tokens (spacing, colors, typography)
2. Semantic HTML first
3. CSS custom properties for theming
4. Progressive enhancement

### Phase 5: REFINE ("雕花" Polish)

Apply obsessive visual refinement:
- [ ] Typography: weight contrast (100 vs 800)
- [ ] Backgrounds: layered gradients, never flat
- [ ] Shadows: subtle depth, not generic box-shadow
- [ ] Motion: staggered reveals, eased transitions
- [ ] Details: micro-interactions, hover states

---

## Commands

### `/ux-craft establish`

Creates `system.md` design system file with intelligent fallback:

1. **Check references folder** (`.claude/skills/ux-craft/references/`)
2. **If references exist:**
   - Analyze visual patterns from screenshots
   - Extract design direction from references
   - Suggest direction based on analysis
3. **If references empty:**
   - Ask project type (SaaS, e-commerce, docs, dashboard, creative, etc.)
   - Infer best design direction based on:
     - Industry best practices
     - Similar successful products
     - Project type conventions
   - Recommend direction with reasoning
4. Ask for color foundation (warm/cool/neutral)
5. Generate `system.md` with complete token system
6. Store in `.ux-craft/system.md`

**Project Type → Direction Mapping:**

| Project Type | Recommended Direction |
|--------------|----------------------|
| SaaS / B2B | Sophistication & Trust |
| E-commerce | Warmth & Approachability |
| Developer tools | Utility & Function |
| Admin / Dashboard | Precision & Density |
| Analytics / BI | Data & Analysis |
| Creative / Portfolio | Expressive & Bold |
| Documentation | Utility & Function |
| Consumer app | Warmth & Approachability |

### `/ux-craft apply`

Loads existing `system.md` and enforces during generation:

1. Read `.ux-craft/system.md`
2. Validate all generated code against tokens
3. Report violations immediately

### `/ux-craft audit [file]`

Runs validation checklist:

1. Pre-generation checks (see [validation.md](validation.md))
2. Accessibility audit (see [accessibility.md](accessibility.md))
3. Design consistency check
4. Returns structured report

### `/ux-craft research [topic]`

Research-first workflow:

1. Research modern implementations of [topic]
2. Compile patterns, examples, edge cases
3. Return research document
4. Then proceed to build with context

### `/ux-craft polish`

Apply "雕花" refinement to existing code:

1. Read target file
2. Identify generic elements
3. Apply distinctive refinements
4. Verify accessibility maintained

### `/ux-craft extract [name]`

Save pattern to reusable library:

1. Extract component/pattern
2. Generalize tokens
3. Store in `.ux-craft/patterns/[name].md`
4. Document usage

### `/ux-craft compliance`

Audit and track design system compliance across the codebase:

1. Scan all component files for pattern usage
2. Create/update `.ux-craft/compliance.md` with:
   - Files fully compliant (DO NOT TOUCH)
   - Files partially compliant (list violations)
   - Files not yet updated (need migration)
3. Return summary report

**Output:** `.ux-craft/compliance.md`

### `/ux-craft migrate [pattern]`

Systematically migrate a pattern across the codebase:

1. Run `grep -rn "old-pattern" src/` to find all instances
2. Create migration tracker in `.ux-craft/migrations/[pattern].md`
3. List all affected files with instance count
4. Track progress as files are updated

**Example:**
```
/ux-craft migrate transition-colors
```

**Creates:**
```markdown
# Migration: transition-colors → transition-luxury

## Pattern
`transition-colors` → `transition-luxury`

## Affected files
- [ ] src/components/card.tsx (3 instances)
- [ ] src/components/button.tsx (2 instances)

## Completed
- [x] src/components/nav.tsx ✓
```

### `/ux-craft reference [pattern]`

Consult curated visual references before generating UI:

1. Read [taxonomy/elements.md](taxonomy/elements.md) or [taxonomy/pages.md](taxonomy/pages.md)
2. Find matching section for requested pattern
3. Display reference screenshots with context
4. Extract key visual characteristics
5. Keep in memory during subsequent generation

**Example:**
```
/ux-craft reference hero
```

**Output:**
- Shows all hero references from taxonomy
- Displays images with annotations
- Asks user which style to follow
- Applies visual principles to generated code

**Note:** References provide stylistic inspiration, not pixel-perfect specs. For exact values, use `system.md` tokens.

See [references.md](references.md) for full documentation.

### `/ux-craft test-system`

Generate static HTML test pages to validate design system before adoption:

1. Check if `.ux-craft/system.md` exists
2. If not → prompt to run `/ux-craft establish` first
3. Create `.ux-craft/test-pages/` folder
4. Generate test pages for each archetype:
   - `index.html` - Links to all test pages
   - `tokens.css` - CSS custom properties from system.md
   - `entry.html` - Entry/Landing page components
   - `discovery.html` - Search/Listing components
   - `detail.html` - Detail page components
   - `action.html` - Form/Action components
   - `management.html` - Table/Management components
   - `system.html` - Error/System state components
5. Each page includes:
   - All relevant components for that archetype
   - Multiple states (default, hover, focus, error, loading)
   - Responsive breakpoints demo
   - Light/dark mode toggle (if system supports)
6. Provide command to serve locally: `python -m http.server 8080`

**Output:** `.ux-craft/test-pages/` with 7 HTML files + shared CSS

**Usage:**
```
/ux-craft test-system
```

Then open `http://localhost:8080` to review.

### `/ux-craft map-sitemap`

Connect project routes to page taxonomy archetypes:

1. Ask user for sitemap (list of routes/pages)
2. For each route, suggest archetype classification:
   - Entry, Discovery, Detail, Action, Management, or System
3. Identify hybrid pages (multiple archetypes)
4. Create `.ux-craft/sitemap-mapping.md` with:
   - Route → Archetype mapping table
   - Shared layout patterns
   - Special considerations per page

**Example output:**
```markdown
# Sitemap Mapping

| Route | Archetype | Notes |
|-------|-----------|-------|
| `/` | Entry | Hero-centric landing |
| `/products` | Discovery | Sidebar + grid layout |
| `/products/:id` | Detail | Media + info split |
| `/checkout` | Action | Stepped wizard |
| `/admin/users` | Management | Data table |
| `/404` | System | Centered minimal |

## Hybrid Pages
- `/dashboard` → Management (primary) + System (empty states)
```

**Usage:**
```
/ux-craft map-sitemap
```

### `/ux-craft archetype [type]`

Generate a complete page template for a specific archetype:

1. Read taxonomy definition from [taxonomy/pages.md](taxonomy/pages.md)
2. Load `system.md` tokens
3. Generate semantic HTML structure with all component slots
4. Apply styling from design system
5. Include placeholder content appropriate to archetype
6. Add accessibility attributes

**Types:** `entry`, `discovery`, `detail`, `action`, `management`, `system`

**Usage:**
```
/ux-craft archetype discovery
```

---

## Project Migration Commands

Commands for adopting this framework on existing projects.

### `/ux-craft analyze-project`

Analyze an existing codebase and create a comprehensive UI map:

1. **Scan routes/pages** - Find all page components
2. **Classify archetypes** - Map each page to taxonomy archetypes (Entry, Discovery, Detail, Action, Management, System)
3. **Inventory elements** - List all UI elements used per page
4. **Check token usage** - Identify hardcoded values vs design system tokens
5. **Generate project map** - Create `.ux-craft/project-map.md`

**Output:** `.ux-craft/project-map.md` with:
- Pages → Archetypes mapping
- Pages → Elements mapping
- Element inventory with compliance status
- Token usage analysis
- Violations summary
- Migration priorities

**Usage:**
```
/ux-craft analyze-project
```

**When to use:**
- First time adopting this framework on an existing project
- After major UI changes to update the map
- Before planning a design system migration

### `/ux-craft migrate-project`

Systematic migration workflow for existing projects:

1. **Check prerequisites:**
   - `.ux-craft/system.md` exists (run `/ux-craft establish` if not)
   - `.ux-craft/project-map.md` exists (run `/ux-craft analyze-project` if not)

2. **Show migration overview:**
   - Total files needing migration
   - Violations by severity (Critical, High, Medium)
   - Suggested migration order

3. **Create migration plan:**
   - `.ux-craft/migrations/project-migration.md` with:
     - Prioritized file list
     - Specific changes needed per file
     - Progress tracking

4. **Guide migration:**
   - Work file by file
   - For each file: read → identify violations → fix → verify → mark complete
   - Update project-map.md as files become compliant

**Usage:**
```
/ux-craft migrate-project
```

**Migration priority order:**
1. **Foundation** - Typography, colors, spacing tokens
2. **Global components** - Nav, footer, buttons (high reuse)
3. **Critical paths** - Entry, Action pages (user-facing)
4. **Secondary pages** - Discovery, Detail pages
5. **Admin/internal** - Management pages (lower priority)

### `/ux-craft migration-status`

Quick status check on ongoing migration:

1. Read `.ux-craft/project-map.md`
2. Show compliance percentage
3. List remaining violations by priority
4. Suggest next files to tackle

**Usage:**
```
/ux-craft migration-status
```

---

## Visual References System

### Purpose

Curated screenshot collection mapped to UI patterns. Provides visual context during the RESEARCH phase.

### Structure

```
taxonomy/
├── pages.md        # Page types → sections → references
└── elements.md     # Atomic elements → variants → references
references/
└── [element]-[context]-[number].png
```

### Naming Convention

```
[elemento]-[contesto]-[variante]-[numero].png

Examples:
hero-saas-dark-01.png
nav-mobile-overlay-01.png
card-product-grid-01.png
```

### Limitations

| Claude CAN | Claude CANNOT |
|------------|---------------|
| See layout and proportions | Extract exact hex values |
| Understand visual style | Measure spacing in px |
| Apply similar principles | Replicate pixel-perfect |
| Compare with system.md | Process batch automatically |

For pixel-perfect accuracy, export tokens from Figma.

---

## Design System Memory

### File: `.ux-craft/system.md`

Persistent design system for the project. Created by `/ux-craft establish`.

Structure:
```markdown
# Design System - [Project Name]

## Direction
Personality: [Selected direction]
Foundation: [Warm/Cool/Neutral]

## Tokens
### Spacing
Base: [4px | 8px]
Scale: [values]

### Typography
Display: [font] - [weight]
Body: [font] - [weight]
Code: [font]

### Colors
[Custom properties]

### Shadows
[Depth levels]
```

### File: `.ux-craft/compliance.md`

Tracks which files follow the design system. Created/updated by `/ux-craft compliance`.

Structure:
```markdown
# Design System Compliance

**Last updated:** YYYY-MM-DD
**System:** [link to system.md]

## Compliant Files (DO NOT TOUCH)
These files follow all design system patterns.

| File | Verified |
|------|----------|
| src/components/nav.tsx | 2026-01-17 |
| src/components/footer.tsx | 2026-01-17 |

## Partially Compliant
These files have some violations to fix.

| File | Issues |
|------|--------|
| src/components/card.tsx | transition-colors (3), hardcoded spacing (2) |

## Not Yet Updated
These files haven't been migrated to the design system.

| File | Priority |
|------|----------|
| src/app/admin/* | Low |
```

### Directory: `.ux-craft/migrations/`

Tracks in-progress pattern migrations. Created by `/ux-craft migrate`.

```
.ux-craft/
├── system.md              # Design tokens (created by /ux-craft establish)
├── project-map.md         # Full UI analysis (created by /ux-craft analyze-project)
├── compliance.md          # File compliance status (created by /ux-craft compliance)
├── sitemap-mapping.md     # Route → archetype mapping (created by /ux-craft map-sitemap)
├── migrations/            # Active migrations
│   ├── project-migration.md   # Full project migration tracker
│   ├── transition-colors.md   # Pattern-specific migrations
│   └── spacing-variables.md
├── patterns/              # Extracted reusable patterns
└── test-pages/            # Static HTML test pages
    ├── index.html
    ├── tokens.css
    ├── entry.html
    ├── discovery.html
    ├── detail.html
    ├── action.html
    ├── management.html
    └── system.html
```

---

## Enforcement Rules

### Automatic Violations (Block Generation)

| Rule | Violation | Action |
|------|-----------|--------|
| Generic font | Inter, Roboto, Arial, sans-serif | BLOCK |
| Low contrast | < 4.5:1 text contrast | BLOCK |
| Off-grid spacing | Not divisible by base unit | WARN |
| Small targets | < 44px touch target | BLOCK |
| Missing focus | No :focus-visible styles | BLOCK |

### Quality Gates

Before marking UI work complete:
1. All BLOCK violations resolved
2. WARN violations acknowledged
3. Accessibility checklist passed
4. Visual polish applied

---

## Quick Reference

### Spacing Scale (8px base)
```
--space-1: 8px    --space-5: 48px
--space-2: 16px   --space-6: 64px
--space-3: 24px   --space-7: 96px
--space-4: 32px   --space-8: 128px
```

### Typography Scale
```
--text-xs: 0.75rem   --text-xl: 1.25rem
--text-sm: 0.875rem  --text-2xl: 1.5rem
--text-base: 1rem    --text-3xl: 1.875rem
--text-lg: 1.125rem  --text-4xl: 2.25rem
```

### Contrast Requirements
```
Normal text: 4.5:1 minimum (AA)
Large text:  3:1 minimum (AA)
Enhanced:    7:1 recommended (AAA)
UI elements: 3:1 minimum
```

---

## Detailed Resources

- **Design Directions**: [directions.md](directions.md)
- **Accessibility Checklist**: [accessibility.md](accessibility.md)
- **Typography System**: [typography.md](typography.md)
- **Validation Rules**: [validation.md](validation.md)
- **Example Systems**: [examples/](examples/)
- **Visual References**: [references.md](references.md)
- **Page Taxonomy**: [taxonomy/pages.md](taxonomy/pages.md)
- **Element Taxonomy**: [taxonomy/elements.md](taxonomy/elements.md)
- **Project Map Template**: [templates/project-map-template.md](templates/project-map-template.md)

---

## Session Tracking

Session: ${CLAUDE_SESSION_ID}

Store session artifacts in: `.ux-craft/sessions/${CLAUDE_SESSION_ID}/`
