# Development Principles (Language-Agnostic)

## SOLID Principles

### Single Responsibility (SRP)
Ogni modulo/classe/funzione ha UNA sola ragione per cambiare.

**Segnali di violazione:**
- Funzione con "and" nel nome (es: `validateAndSave`)
- Classe con troppi metodi non correlati
- File che importa dipendenze di domini diversi

### Open/Closed (OCP)
Aperto per estensione, chiuso per modifica.

**Applicazione pratica:**
- Usa interfacce/protocolli per definire contratti
- Nuove funzionalita tramite nuove implementazioni
- Evita modifiche a codice funzionante

### Liskov Substitution (LSP)
I sottotipi devono essere sostituibili ai tipi base.

**Test mentale:** Se sostituisco `Parent` con `Child`, il programma funziona ancora correttamente?

### Interface Segregation (ISP)
Molte interfacce specifiche > una interfaccia generale.

**Applicazione:** Dividi interfacce grandi in ruoli specifici.

### Dependency Inversion (DIP)
Dipendi da astrazioni, non da implementazioni concrete.

**Esempio universale:**
```
# Invece di:
class OrderService:
    def __init__(self):
        self.db = PostgresDatabase()  # Dipendenza concreta

# Preferisci:
class OrderService:
    def __init__(self, db: Database):  # Dipendenza astratta
        self.db = db
```

---

## Principi di Organizzazione

### Separation of Concerns
- Data access separato da business logic
- Business logic separato da presentation
- Configuration separato da codice

### High Cohesion, Low Coupling
- ALTA coesione: elementi correlati stanno insieme
- BASSO accoppiamento: moduli indipendenti tra loro

### Principio della Minima Sorpresa
Il codice dovrebbe fare quello che il nome suggerisce, niente di piu.

---

## DRY, KISS, YAGNI

### DRY (Don't Repeat Yourself)
Ogni pezzo di conoscenza deve avere una rappresentazione unica nel sistema.

**Attenzione:** DRY riguarda la conoscenza, non il codice. Due pezzi di codice identici ma che rappresentano concetti diversi NON violano DRY.

### KISS (Keep It Simple, Stupid)
Preferisci soluzioni semplici. La complessita e un costo.

**Domanda:** C'e un modo piu semplice per ottenere lo stesso risultato?

### YAGNI (You Ain't Gonna Need It)
Non implementare funzionalita finche non sono necessarie.

**Attenzione:** Questo non significa ignorare l'architettura. Significa non aggiungere feature "perche potrebbero servire".

---

## Anti-Pattern Universali

| Anti-Pattern | Problema | Soluzione |
|--------------|----------|-----------|
| God Object | Una classe fa tutto | Dividi per responsabilita |
| Spaghetti Code | Flusso incomprensibile | Estrai funzioni, usa early return |
| Magic Numbers | Valori senza significato | Costanti nominate |
| Copy-Paste | Duplicazione | Estrai funzione comune |
| Premature Optimization | Complessita inutile | YAGNI - ottimizza quando serve |
| Feature Envy | Classe usa troppi dati di altra classe | Sposta metodo nella classe giusta |
| Shotgun Surgery | Un cambio richiede modifiche in molti posti | Centralizza la logica |
| Long Parameter List | Funzione con troppi parametri | Usa oggetti/struct |

---

## Code Smells Universali

### Funzione
- Troppo lunga (> 50 righe)
- Troppi parametri (> 5)
- Flag arguments (boolean che cambia comportamento)
- Output parameters

### Classe/Modulo
- Troppo grande (> 500 righe)
- Troppi metodi pubblici
- Nessuna coesione tra metodi
- Accoppiamento eccessivo

### Naming
- Nomi generici (data, info, handler, manager, processor)
- Nomi abbreviati non ovvi
- Nomi che non riflettono il comportamento

---

## Metriche di Qualita Universali

| Metrica | Soglia Consigliata | Perche |
|---------|-------------------|--------|
| Lunghezza funzione | < 50 righe | Leggibilita |
| Lunghezza file | < 500 righe | Manutenibilita |
| Profondita nesting | < 4 livelli | Complessita cognitiva |
| Parametri funzione | < 5 | Usabilita |
| Complessita ciclomatica | < 10 | Testabilita |
| Coupling | Basso | Modificabilita |
| Cohesion | Alto | Comprensibilita |

---

## Early Return Pattern

**Prima (nesting profondo):**
```
function process(user) {
    if (user != null) {
        if (user.isActive) {
            if (user.hasPermission) {
                // actual logic here
            }
        }
    }
}
```

**Dopo (early return):**
```
function process(user) {
    if (user == null) return
    if (!user.isActive) return
    if (!user.hasPermission) return

    // actual logic here
}
```

---

## Composizione vs Ereditarieta

**Preferisci composizione:**
- Piu flessibile
- Evita gerarchie profonde
- Facilita testing

**Usa ereditarieta solo quando:**
- C'e vera relazione "is-a"
- Vuoi polimorfismo
- La gerarchia e stabile e poco profonda

---

## Fail Fast

Verifica precondizioni all'inizio. Fallisci immediatamente se qualcosa non va.

```
function divide(a, b) {
    if (b == 0) {
        throw new Error("Cannot divide by zero")  // Fail fast
    }
    return a / b
}
```

---

## Defensive Programming vs Design by Contract

### Defensive Programming
Valida tutto, non fidarti di nessuno.
- Buono per: Input esterni, API pubbliche, boundaries

### Design by Contract
Definisci pre/post condizioni, il chiamante garantisce le pre.
- Buono per: Codice interno, API private

**Raccomandazione:** Difensivo ai boundaries, contratti internamente.
