# Validation Rules

Measurable, objective criteria for validating SEO-GEO-Copy content.

---

## How to Use

Each rule has:
- **Rule ID**: For reference
- **Check**: What to verify
- **Pass condition**: Objective criteria
- **Fail action**: What to do if it fails

Apply relevant rules after generation. Report pass/fail for each.

---

## SEO Rules

### SEO-001: Title Tag Length
- **Check**: Count characters in title tag
- **Pass**: 30-60 characters
- **Fail**: Truncate or expand to fit range

### SEO-002: Title Keyword Position
- **Check**: Position of primary keyword in title
- **Pass**: Keyword starts within first 30 characters
- **Fail**: Rewrite to front-load keyword

### SEO-003: Meta Description Length
- **Check**: Count characters in meta description
- **Pass**: 120-160 characters
- **Fail**: Adjust length to range

### SEO-004: Meta Description Keyword
- **Check**: Primary keyword present in meta description
- **Pass**: Keyword appears at least once
- **Fail**: Rewrite to include keyword naturally

### SEO-005: H1 Presence
- **Check**: Page has exactly one H1
- **Pass**: Exactly 1 H1 tag
- **Fail**: Add H1 or remove duplicates

### SEO-006: H1 Keyword
- **Check**: Primary keyword in H1
- **Pass**: Keyword appears in H1
- **Fail**: Rewrite H1 to include keyword

### SEO-007: Keyword in First 100 Words
- **Check**: Primary keyword in first 100 words of body content
- **Pass**: Keyword appears in first 100 words
- **Fail**: Rewrite opening to include keyword

### SEO-008: Header Hierarchy
- **Check**: H2s follow H1, H3s follow H2s
- **Pass**: No skipped levels (H1→H3 without H2)
- **Fail**: Fix hierarchy

### SEO-009: Internal Links
- **Check**: Content has internal links to related pages
- **Pass**: At least 2 internal links per 1000 words
- **Fail**: Add relevant internal links

### SEO-010: URL Slug
- **Check**: URL contains primary keyword, no stop words
- **Pass**: Keyword present, lowercase, hyphens, under 60 chars
- **Fail**: Suggest corrected slug

---

## GEO Rules

### GEO-001: Answer-First Opening
- **Check**: First paragraph directly answers the main query
- **Pass**: Opening paragraph can stand alone as complete answer
- **Fail**: Rewrite opening with direct answer

### GEO-002: Self-Contained Paragraphs
- **Check**: Each paragraph is semantically complete
- **Pass**: No paragraph requires previous paragraph to make sense
- **Fail**: Rewrite to add necessary context within paragraph

### GEO-003: No Fluffy Intros
- **Check**: Content starts with substance
- **Pass**: No "In today's world...", "Have you ever wondered..."
- **Fail**: Delete fluff, start with answer

### GEO-004: Specific Claims
- **Check**: Claims include specifics
- **Pass**: Numbers, percentages, dates, or named sources present
- **Fail**: Add specific data or remove vague claim

### GEO-005: Source Attribution
- **Check**: Statistics and facts have sources
- **Pass**: Each statistic cites a source
- **Fail**: Add source or mark as "based on [qualifier]"

### GEO-006: Entity Clarity
- **Check**: Key entities are explicitly named
- **Pass**: Products, people, companies named (not just "it" or "they")
- **Fail**: Replace pronouns with explicit names on first use per section

### GEO-007: FAQ Answer Completeness
- **Check**: FAQ answers are self-contained
- **Pass**: Answers don't say "click here", "see above", "learn more"
- **Fail**: Rewrite answer to be complete

### GEO-008: Definition Presence
- **Check**: Key terms are defined
- **Pass**: Technical terms defined on first use
- **Fail**: Add inline definition or definition callout

### GEO-009: No Clickbait
- **Check**: Headlines match content
- **Pass**: Content delivers what headline promises
- **Fail**: Rewrite headline or add missing content

### GEO-010: Chunk Length
- **Check**: Paragraphs are appropriate length for extraction
- **Pass**: Most paragraphs 40-150 words
- **Fail**: Split long paragraphs or combine very short ones

---

## Copywriting Rules

### COPY-001: Value Proposition Clarity
- **Check**: Clear value proposition within first scroll
- **Pass**: Reader knows "what's in it for me" in first 150 words
- **Fail**: Add explicit benefit statement

### COPY-002: You vs We Ratio
- **Check**: Ratio of "you/your" to "we/our/I" words
- **Pass**: "You" language used 2x more than "we" language
- **Fail**: Rewrite to focus on reader

### COPY-003: CTA Presence
- **Check**: Call to action present
- **Pass**: Clear next step for reader (per business intent)
- **Fail**: Add appropriate CTA

### COPY-004: CTA Clarity
- **Check**: CTA uses action verb + benefit
- **Pass**: CTA is specific ("Start Free Trial" not "Submit")
- **Fail**: Rewrite CTA

### COPY-005: Benefit vs Feature Ratio
- **Check**: Benefits stated, not just features
- **Pass**: Each feature is paired with a benefit
- **Fail**: Add "so you can..." or "which means..." after features

### COPY-006: Scannable Structure
- **Check**: Content is scannable
- **Pass**: Headers every 300 words max, bullets/lists present
- **Fail**: Add subheadings or break into lists

### COPY-007: Social Proof
- **Check**: Social proof present (where applicable)
- **Pass**: Testimonials, logos, numbers, or reviews included
- **Fail**: Add social proof or note gap for client

### COPY-008: Objection Handling
- **Check**: Common objections addressed (where applicable)
- **Pass**: At least one objection answered (FAQ, guarantee, comparison)
- **Fail**: Identify likely objections, add responses

### COPY-009: No Jargon Without Explanation
- **Check**: Technical terms explained
- **Pass**: Jargon either avoided or explained
- **Fail**: Add explanation or use simpler term

### COPY-010: Active Voice
- **Check**: Active voice dominant
- **Pass**: Less than 20% passive constructions
- **Fail**: Rewrite passive sentences

---

## Schema Rules

### SCHEMA-001: Schema Present
- **Check**: JSON-LD schema exists
- **Pass**: At least one schema type present
- **Fail**: Add appropriate schema

### SCHEMA-002: Schema Type Match
- **Check**: Schema type matches content type
- **Pass**: Article for articles, Product for products, etc.
- **Fail**: Change to correct schema type

### SCHEMA-003: Required Properties
- **Check**: Schema has required properties
- **Pass**: All required properties for that type present
- **Fail**: Add missing required properties

### SCHEMA-004: Valid JSON
- **Check**: JSON-LD is syntactically valid
- **Pass**: JSON parses without errors
- **Fail**: Fix syntax errors

### SCHEMA-005: No Schema Spam
- **Check**: Schema reflects actual page content
- **Pass**: All schema values match visible content
- **Fail**: Remove/correct mismatched values

---

## Technical Rules

### TECH-001: Image Alt Text
- **Check**: Images have alt text
- **Pass**: All images have descriptive alt text
- **Fail**: Add alt text

### TECH-002: Alt Text Quality
- **Check**: Alt text is descriptive
- **Pass**: Alt text describes image, includes keyword if natural
- **Fail**: Rewrite alt text

### TECH-003: No Broken Internal Links
- **Check**: Internal links point to existing pages
- **Pass**: All internal links resolve
- **Fail**: Fix or remove broken links

### TECH-004: Canonical Tag
- **Check**: Canonical tag present
- **Pass**: Self-referencing canonical present
- **Fail**: Add canonical tag

### TECH-005: Open Graph Tags
- **Check**: OG tags present
- **Pass**: og:title, og:description, og:image present
- **Fail**: Add missing OG tags

---

## Validation Scoring

### Per-Rule Scoring
- Pass: 1 point
- Fail: 0 points

### Category Scores
- **SEO Score**: Points earned / 10
- **GEO Score**: Points earned / 10
- **Copy Score**: Points earned / 10
- **Schema Score**: Points earned / 5
- **Tech Score**: Points earned / 5

### Overall Score
Total points / 40 × 100 = Percentage

### Quality Thresholds
- **90-100%**: Production ready
- **80-89%**: Minor fixes needed
- **70-79%**: Significant issues, needs revision
- **Below 70%**: Major rewrite required

---

## Validation Report Template

```markdown
## Validation Report: [Page/Content Title]

**Date:** [Date]
**Content Type:** [Article/Landing Page/Product/etc.]
**Primary Keyword:** [Keyword]

### Scores

| Category | Score | Max | % |
|----------|-------|-----|---|
| SEO | X | 10 | X% |
| GEO | X | 10 | X% |
| Copy | X | 10 | X% |
| Schema | X | 5 | X% |
| Tech | X | 5 | X% |
| **Total** | **X** | **40** | **X%** |

### Failed Rules

| Rule ID | Issue | Fix Required |
|---------|-------|--------------|
| SEO-001 | Title 75 chars | Truncate to 60 |
| GEO-003 | Fluffy intro | Delete first paragraph |
| ... | ... | ... |

### Status
[ ] Production Ready
[ ] Minor Fixes Needed
[ ] Needs Revision
[ ] Major Rewrite Required

### Required Actions
1. [Action 1]
2. [Action 2]
...
```
