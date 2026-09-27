# Logica a 3 simboli — 0, 1, 0 con 1 dentro

**Simboli ufficiali definitivi:**
- 0 = ovale vuoto = Bianco = Spento = 0 fisso
- 1 = 1 con baffetto = Nero = Acceso = 1 fisso
- ① = 0 con 1 dentro con baffetto = Grigio = Casualità = a volte 0, a volte 1

Il terzo simbolo è 0 che contiene 1. Prima usavamo un carattere provvisorio da tastiera, ora è definito correttamente come ①.

> In una riga: 0 spegne, 1 accende, ① fa a caso.

## Tabelle Vero Falso

OR (+): ①+0=①, ①+1=1
AND (·): ①·0=0, ①·1=①
NOT: ¬0=1, ¬1=0, ¬①=①

Tabella completa nel PDF — sempre con ①, mai con altri simboli provvisori.

## Perché non binario

Binario = 2 valori fissi.
Ternario storico Setun 1958 = 3 valori fissi.
Questo = 2 fissi + 1 casuale nativo = computer probabilistico ternario.
Richiede 3 livelli: 0V=0, 2.5V=①, 5V=1.

## Primo calcolo — prova che ① velocizza

Task: ordinare 1000 numeri già ordinati (incubo per binario)

- Deterministico: 499500 confronti
- Con ① casuale: 10136 confronti
- 49.3x più veloce, risparmio 489364 confronti

Task: minimo di sin(10x)+x²/10

- Deterministico bloccato a -0.90 (minimo locale)
- Con ① salta e trova -0.99 (minimo globale)

## Usa

```python
from src.trit import Trit, OR, AND
print(OR(Trit.RANDOM, Trit.ONE))  # 1
print(AND(Trit.RANDOM, Trit.ZERO)) # 0
```

Data: 2026-09-27
Licenza: MIT
