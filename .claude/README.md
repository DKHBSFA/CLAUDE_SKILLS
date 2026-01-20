# Claude Development Framework

Un framework operativo per lavorare con Claude su progetti software, con skill specializzate integrate.

---

## Cos'è

Due componenti che lavorano insieme:

1. **Framework operativo** (`CLAUDE.md` + `.claude/docs/`) — Regole di processo: investigare prima di implementare, tracciare decisioni, verificare prima di affermare.

2. **Skill specializzate** (`.claude/skills/`) — Conoscenza di dominio:
   - **ux-craft** — UI/UX: design direction, accessibilità WCAG, tipografia
   - **dev-patterns** — Development: principi SOLID, API design, testing, security (agnostico + stack-specific)
   - **security-guardian** — Sicurezza AI-specific: OWASP, credential detection, BaaS audit

Il framework definisce *come* Claude lavora. Le skill definiscono *cosa* sa fare in ambiti specifici.

---

## Struttura

```
progetto/
├── CLAUDE.md                 # Regole operative (il "sistema operativo")
└── .claude/
    ├── README.md             # Questo file (documentazione del framework)
    ├── docs/
    │   ├── registry.md       # Memoria: cosa Claude sa del codebase
    │   ├── decisions.md      # Decisioni architetturali e perché
    │   ├── checklist.md      # Verifica pre-commit
    │   ├── workflows.md      # Diagrammi di flusso decisionali (Mermaid)
    │   └── specs/            # Specifiche feature (prima di implementare)
    └── skills/
        ├── ux-craft/         # Skill UI/UX
        │   ├── SKILL.md      # Definizione skill e comandi
        │   ├── directions.md # 6 direzioni di design
        │   ├── references.md # Guida al sistema visual references
        │   ├── taxonomy/     # Tassonomia pagine ed elementi
        │   │   ├── pages.md
        │   │   └── elements.md
        │   └── references/   # Screenshot di riferimento (da popolare)
        ├── dev-patterns/     # Skill development patterns
        │   ├── SKILL.md      # Entry point + /adapt-framework
        │   ├── core/         # Pattern agnostici (sempre presenti)
        │   │   ├── principles.md
        │   │   ├── api-design.md
        │   │   ├── testing.md
        │   │   ├── security.md
        │   │   ├── error-handling.md
        │   │   └── caching.md
        │   ├── checklists/   # Checklist universali
        │   │   ├── code-review.md
        │   │   ├── pre-deploy.md
        │   │   └── refactoring.md
        │   ├── templates/    # Template per generazione
        │   │   └── stack-template.md
        │   └── stacks/       # Pattern stack-specific (generati)
        │       └── typescript-react-nextjs/  # Esempio pre-generato
        └── security-guardian/# Skill sicurezza AI-specific
```

---

## Setup

### Nuovo progetto (senza codice esistente)

1. Copia nella root del progetto:
   - `CLAUDE.md`
   - `.claude/` (intera cartella)

2. Inizia a lavorare. Claude popolerà il registry man mano che sviluppa.

### Progetto esistente (con codice già scritto)

1. Copia nella root del progetto:
   - `CLAUDE.md`
   - `.claude/` (intera cartella)

2. **Obbligatorio:** Fai popolare il registry con questo prompt:

```
Analizza questo codebase e popola .claude/docs/registry.md con:
- Components e services
- Key functions
- API endpoints
- Database schema
- Environment variables
Salta le sezioni che non si applicano.
```

3. **Se ci sono pattern architetturali già stabiliti**, documentali:

```
Analizza il codebase e identifica le convenzioni architetturali (patterns, naming, struttura).
Aggiungi le decisioni rilevanti a .claude/docs/decisions.md.
```

4. **Se il progetto ha check specifici** (linter, i18n, etc.), aggiungi a `.claude/docs/checklist.md`.

### Cosa va popolato per-progetto

| File | Popolamento | Quando |
|------|-------------|--------|
| `registry.md` | **Obbligatorio** | Subito dopo aver copiato il framework |
| `decisions.md` | Consigliato | Se ci sono pattern già stabiliti |
| `checklist.md` | Opzionale | Se ci sono check specifici del progetto |
| `workflows.md` | No | Diagrammi universali, non modificare |
| `specs/*.md` | Automatico | Claude li crea durante lo sviluppo |

### Cosa NON va modificato

| File | Perché |
|------|--------|
| `CLAUDE.md` | È il "sistema operativo" — uguale per tutti i progetti |
| `workflows.md` | Diagrammi di flusso universali — uguale per tutti i progetti |
| `skills/*` | Le skill sono generiche, non dipendono dal progetto |

---

## Come funziona

### Flusso di lavoro standard

1. **Claude legge `CLAUDE.md`** all'inizio della sessione (automatico).

2. **Prima di lavorare**, Claude consulta:
   - `.claude/docs/registry.md` — Cosa esiste già?
   - `.claude/docs/decisions.md` — Decisioni passate da rispettare?
   - `.claude/docs/workflows.md` — Diagrammi di flusso per decisioni complesse

3. **Per modifiche non banali**, Claude:
   - Crea una spec in `.claude/docs/specs/[nome].md`
   - Aspetta approvazione ("PROCEED")
   - Implementa

4. **Dopo aver implementato**, Claude:
   - Aggiorna il registry con nuovi componenti
   - Registra decisioni architetturali rilevanti
   - Esegue la checklist pre-commit

### Workflow Diagrams

Il file `.claude/docs/workflows.md` contiene diagrammi Mermaid che visualizzano i flussi decisionali del framework:

| Workflow | Quando consultare |
|----------|-------------------|
| Change Classification | Per decidere se serve una spec |
| Registry Verification | Prima di affermare che qualcosa esiste |
| Pre-Generation (UX) | Prima di generare codice UI |
| Severity Enforcement | Quando security-guardian trova vulnerabilità |
| Iteration Tracking | Quando modifico lo stesso file ripetutamente |
| Pre-Commit Checklist | Prima di ogni commit |

I diagrammi rendono esplicita la logica condizionale che altrimenti sarebbe sparsa nelle skill in forma testuale.

### Skills

Le skill sono moduli di conoscenza specializzata che Claude può attivare in base al contesto.

#### UX-Craft

Si attiva automaticamente quando il contesto riguarda UI/UX, oppure manualmente:

| Comando | Cosa fa |
|---------|---------|
| `/ux-craft establish` | Crea un design system (con fallback intelligente se nessuna reference) |
| `/ux-craft apply` | Applica il design system durante la generazione |
| `/ux-craft audit` | Verifica accessibilità e coerenza |
| `/ux-craft research [topic]` | Ricerca prima di progettare |
| `/ux-craft polish` | Rifinitura finale |
| `/ux-craft extract [name]` | Salva un pattern riutilizzabile |
| `/ux-craft reference [pattern]` | Consulta riferimenti visivi curati |
| `/ux-craft compliance` | Audit compliance design system su tutto il codebase |
| `/ux-craft migrate [pattern]` | Migrazione sistematica di un pattern |
| `/ux-craft test-system` | Genera pagine HTML statiche per testare il design system |
| `/ux-craft map-sitemap` | Mappa route progetto → archetipi pagina |
| `/ux-craft archetype [type]` | Genera template completo per un archetipo |

**Page Taxonomy System:** La skill include una tassonomia di 6 archetipi pagina (Entry, Discovery, Detail, Action, Management, System). Ogni archetipo definisce layout patterns, component slots, content patterns e interaction flows. Usa `/ux-craft map-sitemap` per mappare le route del tuo progetto agli archetipi.

**Design System Testing:** Prima di adottare un design system, usa `/ux-craft test-system` per generare pagine HTML statiche di test in `.ux-craft/test-pages/`. Questo permette di validare visivamente il sistema prima dell'integrazione.

**Visual References System:** La skill include un sistema di riferimenti visivi per mantenere consistenza nel design. Aggiungi screenshot in `.claude/skills/ux-craft/references/` e mappali nei file taxonomy per far consultare a Claude esempi visivi curati invece di cercare online. Se la cartella references è vuota, `/ux-craft establish` decide autonomamente in base al tipo di progetto.

**Attivazione:** UI, UX, component, interface, design system, accessibility, WCAG, frontend styling

#### Dev Patterns

Framework di sviluppo agnostico con pattern core universali e generazione dinamica di pattern stack-specific.

| Comando | Cosa fa |
|---------|---------|
| `/adapt-framework` | Analizza il progetto e genera pattern per lo stack rilevato |
| `/dev-patterns principles` | Consulta principi SOLID, DRY, KISS |
| `/dev-patterns api` | REST/GraphQL design patterns |
| `/dev-patterns testing` | TDD, coverage, mocking |
| `/dev-patterns security` | Checklist sicurezza |
| `/dev-patterns stack` | Pattern specifici del tuo stack |
| `/dev-patterns review` | Code review con checklist |
| `/dev-patterns checklist [type]` | Carica checklist (pre-deploy, refactoring) |

**Architettura a due livelli:**
1. **Core agnostico** — Principi universali sempre disponibili (SOLID, API design, testing, security, error handling, caching)
2. **Stack-specific** — Pattern generati dinamicamente per il tuo stack (TypeScript+React+Next.js, Python+FastAPI, etc.)

**Attivazione:**
- Automatica quando crei un nuovo progetto (Claude genera i pattern dopo aver scelto lo stack)
- Manuale con `/adapt-framework` su progetti esistenti

#### Security Guardian

Analisi di sicurezza specifica per codice AI-generated. Rileva vulnerabilità tipiche del vibe coding:

| Comando | Cosa fa |
|---------|---------|
| `/security-guardian scan [path]` | Scansiona file/directory per vulnerabilità |
| `/security-guardian audit` | Audit completo del progetto |
| `/security-guardian secrets` | Scansione credenziali e segreti |
| `/security-guardian baas [provider]` | Audit configurazione BaaS (Supabase/Firebase) |
| `/security-guardian status` | Stato sicurezza dei file tracciati |
| `/security-guardian report [format]` | Genera report (sarif/markdown/json) |
| `/security-guardian config` | Configura impostazioni |

**Funzionalità:**
- Pattern OWASP Top 10
- Rilevamento credenziali hardcoded
- Audit BaaS (Supabase, Firebase)
- Tracciamento iteration degradation (ricerca mostra +37.6% vulnerabilità dopo 5 iterazioni AI)
- Rilevamento logic inversion

**Attivazione:** Security review, code audit, credential check, configuration analysis

---

## Perché questo framework

Claude ha tendenze che causano errori:
- Affermare che qualcosa esiste senza verificare
- Iniziare a scrivere codice prima di capire
- Dimenticare decisioni prese in precedenza
- Aggiungere feature non richieste
- Perdere pattern ripetuti in file grandi
- Dichiarare "fatto" un refactoring incompleto

Il framework mitiga questi problemi con:
- **Registry** — Memoria esterna verificabile
- **Specs** — Pensare prima di implementare
- **Decisions** — Non contraddire scelte passate
- **Checklist** — Verifica finale sistematica
- **Migration tracker** — Traccia refactoring su più file
- **Compliance tracking** — Stato di conformità per-file

### Il problema dei file grandi

Quando Claude legge un file di 500+ righe:
1. Legge a chunk → perde pattern che si ripetono
2. Modifica un punto → dimentica gli altri
3. Dichiara "fatto" → l'utente trova errori

**Soluzione nel framework:**
```bash
# Prima di modificare, trova TUTTI i punti
grep -n "pattern" src/components/large-file.tsx
```

Poi Claude sa esattamente quali righe toccare.

---

## Aggiungere altre skill

Le skill sono modulari. Per aggiungerne una:

1. Crea `.claude/skills/[nome-skill]/SKILL.md`
2. Aggiungi file di supporto nella stessa cartella
3. Documenta la skill in `.claude/docs/registry.md`

La skill sarà disponibile automaticamente nelle sessioni future.

---

## Note

- Il framework è pensato per Claude Code (CLI/VSCode), ma i principi funzionano anche con altre interfacce.
- `CLAUDE.md` viene letto automaticamente se presente nella root del progetto.
- Le skill in `.claude/skills/` vengono rilevate automaticamente.

---

## FAQ

### Le skill vengono impattate dal registry?

**No, sono indipendenti.** Le skill (`ux-craft`, `security-guardian`) sono definite a livello di configurazione Claude Code, non nel registry.

Il registry è "memoria" di cosa esiste nel progetto. Le skill sono "capacità" che Claude può usare.

**Però c'è una relazione utile:**

```
Registry dice: "Abbiamo componente Button in src/components/ui/button.tsx"
     ↓
ux-craft può usare questa info per:
  - Sapere che esiste già un Button
  - Verificare che segua il design system
  - Non crearne uno nuovo duplicato
```

Il registry **informa** le skill, non le modifica.

### Devo popolare il registry ogni volta che copio il framework?

**Sì, se il progetto ha già codice.** Il registry è specifico per-progetto. Copiarlo da un altro progetto creerebbe confusione.

### Cosa succede se non popolo il registry?

Claude funziona lo stesso, ma:
- Potrebbe ri-scoprire componenti già esistenti
- Potrebbe creare duplicati
- Potrebbe fare assunzioni errate

### Posso modificare le skill?

Sì, ma con attenzione:
- **Modifiche sicure:** Aggiungere pattern, esempi, riferimenti
- **Modifiche rischiose:** Cambiare la logica core o i comandi

---

## Formato dei file .claude/docs/

### registry.md

Esempi di come popolare le varie sezioni:

```markdown
## Components
| Name | Type | Location | Purpose |
|------|------|----------|---------|
| UserService | service | src/auth/service.ts | Handles authentication |

## Key Functions
| Function | Location | Lines | What it does |
|----------|----------|-------|--------------|
| createUser | src/auth/service.ts | 45-78 | Creates user with hashed password |

## API Endpoints
| Method | Route | Handler | Auth required |
|--------|-------|---------|---------------|
| POST | /auth/login | AuthController.login | No |

## Database
### Tables
| Table | Key columns | Used by |
|-------|-------------|---------|
| users | id, email, password_hash | UserService |

### Important queries
| Name | Location | What it does |
|------|----------|--------------|
| getUserByEmail | src/repositories/user.ts:23 | Finds user for login |

## External Dependencies
| Package | Version | Used for |
|---------|---------|----------|
| bcrypt | ^5.1.0 | Password hashing |

## Environment Variables
| Variable | Required | Purpose |
|----------|----------|---------|
| DATABASE_URL | Yes | PostgreSQL connection |
```

### decisions.md

Esempio di decisione architetturale:

```markdown
### Repository pattern for data access
**Date:** 2026-01-09
**Decision:** All database operations go through repository classes
**Why:** Separates DB logic from business logic, enables easy mocking in tests
**Affects:** Every new data model needs a corresponding repository
```
