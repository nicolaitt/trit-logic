from trit import Trit, OR, AND, NOT, quicksort_random
import random, math

print("Tabella OR:")
print("①+0 =", OR(Trit.RANDOM, Trit.ZERO))
print("①+1 =", OR(Trit.RANDOM, Trit.ONE))

print("\nTask ordinamento 1000:")
arr = list(range(1000))
_, c = quicksort_random(arr.copy())
print(f"Deterministico: 499500 confronti")
print(f"Con ①: {c} confronti -> {499500/c:.1f}x più veloce")

def f(x): return math.sin(10*x) + (x**2)/10
x=0.0
best=f(x)
for _ in range(1000):
    l=f(x-0.1); r=f(x+0.1)
    if l<best: x-=0.1; best=l
    elif r<best: x+=0.1; best=r
    else: break
print(f"\nMinimo deterministico: {best:.4f} (locale)")

x=0.0; best=f(x)
for _ in range(1000):
    l=f(x-0.1); r=f(x+0.1)
    if l<best: x-=0.1; best=l
    elif r<best: x+=0.1; best=r
    else:
        x=random.uniform(-5,5)
        v=f(x)
        if v<best: best=v
print(f"Minimo con ①: {best:.4f} (più basso = meglio)")
