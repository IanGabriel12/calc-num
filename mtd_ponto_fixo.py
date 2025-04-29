import math
import time

precision = 1e-8

def f(x):
    return x ** 2 + x - 6

def phi(x):
    return math.sqrt(6 - x)

def fixed_point(a, b):
    iterations = 0
    max_iterations = 1000

    x = (a + b) / 2
    prev = None

    while iterations < max_iterations:
        prev = x
        x = phi(x)
        error = abs(x - prev)

        if error < precision:
            print(f"Número de iterações: {iterations}")
            print(f"Convergiu em {x}")
            return x

        iterations += 1

    print(f"Número máximo de iterações atingido sem convergir, valor mais próximo: {x}")
    return x

def main():
    a = 1.0
    b = 3.0
    h = 0.4
    exact_root = 2.0

    for start in frange(a, b, h):
        end = start + h
        if end > b:
            end = b

        print(f"\nIntervalo [{start}, {end}]")

        start_time = time.perf_counter()

        root = fixed_point(start, end)

        end_time = time.perf_counter()

        abs_error = abs(root - exact_root)
        rel_error = abs_error / abs(exact_root)

        print(f"Raiz aproximada: {root:.15f}")
        print(f"f(raiz) = {f(root):.15f}")
        print(f"Erro absoluto: {abs_error:.15f}")
        print(f"Erro relativo: {rel_error:.15f}")
        print(f"Tempo de execução: {end_time - start_time:.15f} segundos")

def frange(start, stop, step):
    while start < stop:
        yield start
        start += step

if __name__ == "__main__":
    main()
