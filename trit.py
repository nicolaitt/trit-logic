import random
from enum import Enum

class Trit(Enum):
    ZERO = 0    # 0 = ovale = spento
    ONE = 1     # 1 con baffetto = acceso
    RANDOM = 2  # simbolo vero = 0 con 1 dentro = casualità (prima chiamato simbolo provvisorio precedente)

    def resolve(self):
        if self == Trit.RANDOM:
            return Trit.ONE if random.random() < 0.5 else Trit.ZERO
        return self

def OR(a: Trit, b: Trit) -> Trit:
    if a == Trit.ONE or b == Trit.ONE:
        return Trit.ONE
    if a == Trit.ZERO and b == Trit.ZERO:
        return Trit.ZERO
    return Trit.RANDOM  # 0 con 1 dentro

def AND(a: Trit, b: Trit) -> Trit:
    if a == Trit.ZERO or b == Trit.ZERO:
        return Trit.ZERO
    if a == Trit.ONE and b == Trit.ONE:
        return Trit.ONE
    return Trit.RANDOM

def NOT(a: Trit) -> Trit:
    if a == Trit.ZERO: return Trit.ONE
    if a == Trit.ONE: return Trit.ZERO
    return Trit.RANDOM

def quicksort_random(arr):
    comps = 0
    def qs(a):
        nonlocal comps
        if len(a) <= 1:
            return a
        pivot_idx = random.randint(0, len(a)-1)  # 0 con 1 dentro sceglie
        pivot = a[pivot_idx]
        left, right = [], []
        for i, x in enumerate(a):
            if i == pivot_idx: continue
            comps+=1
            (left if x < pivot else right).append(x)
        return qs(left) + [pivot] + qs(right)
    return qs(arr), comps
