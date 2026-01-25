# Interactive Workflow

Step-by-step guide for running SEO-GEO-Copy skill interactively.

---

## Command: `/seo-geo-copy write`

### Phase 0: Reference Discovery (Automatic)

Before asking questions, check for reference materials:

```
1. Check if reference/ directory exists
2. If exists:
   - Read reference/brand.md (voice, tone, terminology)
   - Read reference/context.md (business goals, constraints)
   - List reference/products/ contents
3. Use this context to:
   - Pre-fill tone/audience questions if specified
   - Offer product selection if products exist
   - Apply brand rules during generation
```

**If reference materials found, inform user:**
```
Found reference materials:
- Brand guidelines: [loaded/not found]
- Project context: [loaded/not found]
- Products: [X files found]

Using these to inform content generation.
```

### Phase 1: Intake Questions

**Ask in sequence:**

```
1. What type of content?
   [ ] Article / Blog Post
   [ ] Landing Page
   [ ] Product Description
   [ ] FAQ Section
   [ ] Homepage
   [ ] Category Page
   [ ] About Page
   [ ] Other: ___

2. What is the topic or subject?
   [Free text]

3. Who is the target audience?
   - Demographics: ___
   - Expertise level: [ ] Beginner [ ] Intermediate [ ] Expert
   - Primary pain point: ___

4. What is the primary keyword?
   [Free text]
   (I'll suggest if blank based on topic)

5. What action should readers take?
   [ ] Learn / Understand
   [ ] Compare options
   [ ] Sign up / Subscribe
   [ ] Purchase / Buy
   [ ] Contact / Inquire
   [ ] Download / Get
   [ ] Other: ___

6. Any specific requirements?
   - Word count: [ ] Short (<500) [ ] Medium (500-1500) [ ] Long (1500+)
   - Tone: [ ] Formal [ ] Conversational [ ] Technical [ ] Friendly
   - Must include: ___
   - Must avoid: ___
```

### Phase 2: Research & Planning

**I do this automatically:**

1. Analyze keyword intent
2. Draft content structure
3. Identify related keywords
4. Plan internal linking opportunities
5. Select appropriate schema type

**Show user:**
```
## Content Plan

**Target keyword:** [keyword]
**Search intent:** [informational/commercial/transactional]
**Recommended word count:** [range]
**Content structure:**
1. [H2 section 1]
2. [H2 section 2]
3. [H2 section 3]
...

**Schema type:** [Article/Product/FAQ/etc.]

Proceed with this plan? [Yes / Adjust]
```

### Phase 3: Generation

**Generate content following:**
1. Load appropriate generation prompt from `/generation/[type].md`
2. Apply all output checklist items
3. Generate full content
4. Generate SEO metadata
5. Generate Schema.org JSON-LD

### Phase 4: Validation

**Run validation automatically:**
1. Load rules from `/validation/rules.md`
2. Apply all relevant rules
3. Generate validation report
4. If score < 90%, fix issues automatically
5. Re-validate after fixes

### Phase 5: Delivery

**Present to user:**
```
## Generated Content

[Full content]

---

## SEO Metadata

[Title, description, URL slug]

---

## Schema.org JSON-LD

[JSON-LD code block]

---

## Validation Report

[Summary scores and any remaining issues]

---

## Next Steps

- [ ] Review and approve content
- [ ] Add to CMS
- [ ] Add internal links from existing pages
- [ ] Schedule publication
```

---

## Command: `/seo-geo-copy audit`

### Phase 1: Input Collection

```
1. What should I audit?
   [ ] Single page (provide URL or paste content)
   [ ] Multiple pages (provide URLs)
   [ ] Full site (provide sitemap or domain)

2. [If single page] Paste the content or provide URL:
   [Free text / URL]

3. What is the primary keyword for this page?
   [Free text]

4. What type of content is this?
   [ ] Article
   [ ] Landing page
   [ ] Product page
   [ ] Category page
   [ ] Homepage
   [ ] Other
```

### Phase 2: Analysis

**I do this automatically:**

1. Parse content structure
2. Extract current title/meta
3. Identify keywords used
4. Analyze headers and hierarchy
5. Check for schema
6. Evaluate content quality

### Phase 3: Validation

**Run full validation:**
1. Apply all rules from `/validation/rules.md`
2. Generate detailed report

### Phase 4: Recommendations

**Present prioritized fixes:**

```
## Audit Report: [Page Title]

### Score: X/40 (X%)

### Critical Issues (Fix First)
1. [Issue] - [Specific fix]
2. [Issue] - [Specific fix]

### High Priority
3. [Issue] - [Specific fix]
4. [Issue] - [Specific fix]

### Medium Priority
5. [Issue] - [Specific fix]

### Low Priority / Enhancements
6. [Issue] - [Specific fix]

---

### Rewritten Content (if requested)

[Provide fixed version]
```

---

## Command: `/seo-geo-copy schema`

### Phase 1: Input

```
1. What type of schema do you need?
   [ ] Article
   [ ] FAQ
   [ ] Product
   [ ] LocalBusiness
   [ ] Person
   [ ] HowTo
   [ ] Organization
   [ ] Event
   [ ] Other: ___

2. I'll need the following information:
   [Dynamic questions based on schema type selected]
```

### Phase 2: Schema-Specific Questions

**Article:**
- Headline?
- Author name?
- Publication date?
- Publisher name?
- Featured image URL?
- Article body summary?

**FAQ:**
- List your questions and answers:
  Q1: ___ A1: ___
  Q2: ___ A2: ___
  (continue as needed)

**Product:**
- Product name?
- Description?
- Brand?
- Price?
- Currency?
- Availability?
- SKU?
- Image URLs?
- Rating (if any)?

**LocalBusiness:**
- Business name?
- Address?
- Phone?
- Hours?
- Price range?
- Business type?

**Person:**
- Full name?
- Job title?
- Employer?
- Bio?
- Image URL?
- Social profiles?

**HowTo:**
- Title?
- Steps (name + description each)?
- Tools needed?
- Supplies needed?
- Total time?

### Phase 3: Generation

1. Load template from `/templates/schemas/[type].json`
2. Fill in user-provided values
3. Validate JSON syntax
4. Present completed schema

---

## Command: `/seo-geo-copy pillar-cluster`

### Phase 1: Topic Discovery

```
1. What is the core topic you want to own?
   [Free text]

2. What is your business/site about?
   [Free text - helps contextualize]

3. How much content can you realistically produce?
   [ ] 5-10 articles
   [ ] 10-20 articles
   [ ] 20+ articles

4. Any existing content to incorporate?
   [URLs or page names]
```

### Phase 2: Architecture Generation

1. Generate pillar page concept
2. Generate 8-15 cluster topics
3. Map relationships
4. Create internal linking plan

### Phase 3: Deliverable

```
## Pillar-Cluster Architecture: [Topic]

### Pillar Page
[Title and structure]

### Cluster Articles (Prioritized)
1. [Cluster] - [Why prioritized]
2. [Cluster]
...

### Implementation Roadmap
1. Create pillar page first
2. Then clusters in priority order
3. Add links as each piece publishes

### Content Briefs
[Brief for each piece]
```

---

## Error Handling

### If User Provides Incomplete Info

```
I need a bit more information to create [high-quality content type]:

Missing: [specific field]
Why it matters: [brief explanation]

Please provide: ___
```

### If Validation Fails Repeatedly

```
I'm having trouble getting this above 90% quality. The main issues are:

1. [Persistent issue]
2. [Persistent issue]

Options:
[ ] Accept current version (X% score)
[ ] Provide additional information about: [what's needed]
[ ] Adjust requirements to: [suggestion]
```

### If Content Type Not Supported

```
I don't have a specific generation prompt for [type], but I can:

[ ] Adapt the Article template
[ ] Adapt the Landing Page template
[ ] Create custom structure based on your needs

Which approach would you prefer?
```
