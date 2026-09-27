# trit-logic

> 0 spegne, 1 accende, ①=0 con 1 dentro = casuale...

**Un computer ternario. Base ternaria. 3 numero perfetto.**

Il terzo stato, quello che manca alla logica binaria.

### L'idea - dal quaderno

![Quaderno originale](./quaderno.jpeg)

```
0 = SPENTO, NERO, FALSO
1 = ACCESO, BIANCO, VERO
① = CASUALE, GRIGIO, VERO e FALSO

TERZO FATTORE
① = un 1 dentro lo 0
```

**VERO & FALSO INSIEME**
↓
**GATTO DI SCHRÖDINGER**
↓
**LANCIO DELLA MONETA**
↓
**① PUO' ESSERE ENTRAMBI**

### Perché 3?

In teoria dell'informazione, la base più efficiente è `e = 2.718...`
L'intero più vicino è **3**. Non è 2.

- Binario: 2 stati -> 0, 1
- Ternario: 3 stati -> 0, 1, ①

Con 1 trit rappresenti 50% di informazione in più di 1 bit.

Storicamente: Setun (Mosca, 1958) di Brusentsov è stato il primo computer ternario moderno con logica bilanciata {-1, 0, +1}. Knuth lo definì "forse la base più bella".

### La logica

Non è solo -1, 0, +1. È uno stato di sovrapposizione.

| Simbolo | Valore | Significato | Colore |
| :--- | :--- | :--- | :--- |
| `0` | -1 / 0 | SPENTO / FALSO | Nero |
| `1` | +1 / 1 | ACCESO / VERO | Bianco |
| `①` | 0 con 1 dentro | CASUALE / ENTRAMBI | Grigio |

#### Tavole di verità (Strong Kleene - versione trit-logic)

**NOT**
```
NOT 0 = 1
NOT 1 = 0
NOT ① = ①  # il casuale resta casuale
```

**AND (min)**
```
0 AND x = 0
1 AND 1 = 1
1 AND ① = ①
① AND ① = ①
```

**OR (max)**
```
1 OR x = 1
0 OR 0 = 0
0 OR ① = ①
① AND ① = ①
```

### Implementazione Python (base)

```python
from enum import Enum
import random

class Trit(Enum):
    ZERO = 0  # SPENTO, NERO, FALSO
    ONE = 1   # ACCESO, BIANCO, VERO
    BOTH = 2  # ① CASUALE, GRIGIO, VERO e FALSO

    def __repr__(self):
        return {0: "0", 1: "1", 2: "①"}[self.value]

def trit_not(a: Trit) -> Trit:
    if a == Trit.ZERO: return Trit.ONE
    if a == Trit.ONE: return Trit.ZERO
    return Trit.BOTH  # NOT ① = ①

def trit_and(a: Trit, b: Trit) -> Trit:
    # 0 domina, 1 è neutro se l'altro è ①
    if a == Trit.ZERO or b == Trit.ZERO:
        return Trit.ZERO
    if a == Trit.ONE and b == Trit.ONE:
        return Trit.ONE
    return Trit.BOTH

def trit_or(a: Trit, b: Trit) -> Trit:
    # 1 domina
    if a == Trit.ONE or b == Trit.ONE:
        return Trit.ONE
    if a == Trit.ZERO and b == Trit.ZERO:
        return Trit.ZERO
    return Trit.BOTH

def collapse(trit: Trit) -> Trit:
    """Il lancio della moneta - collassa ① in 0 o 1"""
    if trit != Trit.BOTH:
        return trit
    return random.choice([Trit.ZERO, Trit.ONE])
```

### Roadmap

- [x] Definizione del terzo fattore
- [ ] Porte logiche complete
- [ ] Addizionatore ternario
- [ ] Simulatore Setun-like

---
*TERZO STATO QUELLO CHE MANCA ALLA LOGICA BINARIA*
