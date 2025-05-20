import time
import cmath  

def f(x):
    return x**2 + x - 6

raiz = 2

def proxima_aproximacao_muller(f, x0, x1, x2):
    f0, f1, f2 = f(x0), f(x1), f(x2)
    h0 = x1 - x0
    h1 = x2 - x1
    delta0 = (f1 - f0) / h0
    delta1 = (f2 - f1) / h1
    a = (delta1 - delta0) / (h1 + h0)
    b = a * h1 + delta1
    c = f2
    discriminant = cmath.sqrt(b**2 - 4*a*c)

    if abs(b + discriminant) > abs(b - discriminant):
        denominator = b + discriminant
    else:
        denominator = b - discriminant

    x3 = x2 + (-2 * c) / denominator
    return x3

def mtd_muller(f, a, b):
    e = 1e-8
    num_iter = 0
    start_time = time.time()

    x0 = a
    x1 = (a + b) / 2
    x2 = b

    x3 = proxima_aproximacao_muller(f, x0, x1, x2)

    while abs(f(x3)) > e and num_iter < 100:
        num_iter += 1
        x0, x1, x2 = x1, x2, x3
        x3 = proxima_aproximacao_muller(f, x0, x1, x2)

    end_time = time.time()
    seconds = end_time - start_time

    print(f"Raiz encontrada: {x3.real:.9f}")  # Considera parte real
    print(f"Número de iterações: {num_iter}")
    print(f"Tempo gasto (s): {seconds:.9f}")
    print(f"Erro relativo: {abs(raiz - x3.real)/raiz:.9f}")
    print(f"Erro absoluto: {abs(raiz - x3.real):.9f}")

mtd_muller(f, 0, 3)
