# Feature: UX-Craft Visual References System

**Status:** COMPLETE
**Created:** 2026-01-17
**Approved:** 2026-01-17
**Completed:** 2026-01-17

---

## 1. Overview

**What?** Sistema di riferimenti visivi strutturato che mappa screenshot a pattern UI, integrato nella skill ux-craft.

**Why?** Permette a Claude di consultare esempi visivi curati invece di basarsi solo su descrizioni testuali, migliorando la consistenza del design generato.

**For whom?** L'utente che vuole un design system coerente basato su riferimenti visivi reali.

**Success metric:** Claude può invocare `/ux-craft reference [pattern]` e vedere screenshot pertinenti prima di generare UI.

---

## 2. Technical Approach

**Pattern:** Estensione della skill esistente con nuova cartella `references/` e file di mapping `.md`

**Key decisions:**
- Cartella `references/` piatta (no sottocartelle) → semplicità di gestione
- Naming convention: `[elemento]-[contesto]-[numero].png`
- File `.md` per categoria contengono path + note contestuali
- Integrazione con workflow RESEARCH esistente

**Dependencies:** Nessuna nuova dipendenza

**Breaking changes:** None

---

## 3. Files to Modify

| File | Action | Changes |
|------|--------|---------|
| `.claude/skills/ux-craft/SKILL.md` | Modify | Aggiungere comando `/ux-craft reference` |
| `.claude/skills/ux-craft/references.md` | Create | Indice generale dei riferimenti |
| `.claude/skills/ux-craft/taxonomy/pages.md` | Create | Tassonomia tipologie di pagina |
| `.claude/skills/ux-craft/taxonomy/elements.md` | Create | Tassonomia elementi UI |
| `.claude/skills/ux-craft/references/` | Create | Cartella per screenshot |

---

## 4. Struttura Proposta

```
.claude/skills/ux-craft/
├── SKILL.md                    # Esistente, da modificare
├── references.md               # NEW: Indice e istruzioni d'uso
├── taxonomy/
│   ├── pages.md                # NEW: Tipi di pagina → sezioni
│   └── elements.md             # NEW: Elementi atomici
└── references/
    ├── hero-saas-01.png
    ├── hero-ecommerce-01.png
    ├── nav-desktop-minimal-01.png
    ├── nav-mobile-overlay-01.png
    ├── card-product-01.png
    ├── form-login-01.png
    └── ...
```

---

## 5. Formato File Taxonomy

### `taxonomy/pages.md`
```markdown
# Page Taxonomy

## Homepage
Sezioni tipiche:
- Hero → [hero-saas-01.png](../references/hero-saas-01.png)
- Navigation → [nav-desktop-minimal-01.png](../references/nav-desktop-minimal-01.png)
- Features grid → [features-grid-01.png](../references/features-grid-01.png)
- Social proof → [testimonials-carousel-01.png](../references/testimonials-carousel-01.png)
- CTA finale → [cta-section-01.png](../references/cta-section-01.png)
- Footer → [footer-multi-column-01.png](../references/footer-multi-column-01.png)

## Product Listing
...
```

### `taxonomy/elements.md`
```markdown
# Element Taxonomy

## Navigation
### Desktop
- Minimal: [nav-desktop-minimal-01.png](../references/nav-desktop-minimal-01.png)
- Mega menu: [nav-desktop-mega-01.png](../references/nav-desktop-mega-01.png)

### Mobile
- Hamburger overlay: [nav-mobile-overlay-01.png](../references/nav-mobile-overlay-01.png)
- Bottom tabs: [nav-mobile-tabs-01.png](../references/nav-mobile-tabs-01.png)

## Hero Sections
- SaaS landing: [hero-saas-01.png](../references/hero-saas-01.png)
- E-commerce: [hero-ecommerce-01.png](../references/hero-ecommerce-01.png)
- Editorial: [hero-editorial-01.png](../references/hero-editorial-01.png)

## Cards
...
```

---

## 6. Nuovo Comando

### `/ux-craft reference [pattern]`

**Workflow:**
1. Riceve richiesta (es. `/ux-craft reference hero`)
2. Legge `taxonomy/elements.md` o `taxonomy/pages.md`
3. Trova sezione corrispondente
4. Mostra immagini di riferimento con contesto
5. Tiene in memoria durante la generazione successiva

**Esempio output:**
```
## Hero Section References

Trovati 3 riferimenti per "hero":

1. **SaaS Landing** - hero-saas-01.png
   - Layout centrato
   - Headline + subhead + CTA
   - Immagine/mockup a destra o sotto

2. **E-commerce** - hero-ecommerce-01.png
   - Full-width image
   - Overlay text
   - CTA prominente

3. **Editorial** - hero-editorial-01.png
   - Typography-driven
   - Minimal imagery
   - Scroll indicator

Quale stile preferisci per il tuo progetto?
```

---

## 7. Naming Convention

```
[elemento]-[contesto]-[variante]-[numero].png

Esempi:
hero-saas-dark-01.png
nav-mobile-overlay-01.png
card-product-grid-01.png
form-checkout-multistep-01.png
footer-minimal-01.png
```

**Regole:**
- Tutto lowercase
- Separatori: trattini (-)
- Numero progressivo a 2 cifre (01, 02, ...)
- Niente spazi o caratteri speciali

---

## 8. Limitazioni Dichiarate

| Cosa Claude PUÒ fare | Cosa Claude NON può fare |
|---------------------|--------------------------|
| Vedere layout e proporzioni | Estrarre hex esatti |
| Capire stile visivo | Misurare spacing in px |
| Applicare principi simili | Replicare pixel-perfect |
| Confrontare con system.md | Processare batch automatici |

**Implicazione:** I references sono ispirazione guidata, non spec esatta. Per precisione pixel-perfect, esportare token da Figma.

---

## 9. Integrazione con Workflow Esistente

```
┌─────────────────────────────────────────────────────────┐
│                    WORKFLOW UX-CRAFT                     │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  1. /ux-craft establish                                 │
│     └── Crea system.md con token                        │
│                                                         │
│  2. /ux-craft reference [pattern]  ← NEW                │
│     └── Consulta screenshot di riferimento              │
│                                                         │
│  3. BUILD                                               │
│     └── Genera codice usando:                           │
│         • Token da system.md (valori esatti)            │
│         • Stile da references (ispirazione)             │
│                                                         │
│  4. /ux-craft audit                                     │
│     └── Verifica consistenza                            │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## 10. Verifica

Per verificare che funziona:
1. Aggiungo almeno 1 screenshot in `references/`
2. Creo entry in `taxonomy/elements.md`
3. Invoco `/ux-craft reference [nome]`
4. Claude mostra l'immagine e il contesto
5. Genero UI e verifico che lo stile sia coerente

---

**Attendo PROCEED per implementare.**
