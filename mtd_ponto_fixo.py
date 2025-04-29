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
    a = 1.8
    b = 2.2
    exact_root = 2.0

    start_time = time.perf_counter()

    root = fixed_point(a, b)

    end_time = time.perf_counter()

    abs_error = abs(root - exact_root)
    rel_error = abs_error / abs(exact_root)

    print(f"Raiz aproximada: {root:.9f}")
    print(f"f(raiz) = {f(root):.9f}")
    print(f"Erro absoluto: {abs_error:.9f}")
    print(f"Erro relativo: {rel_error:.9f}")
    print(f"Tempo de execução: {end_time - start_time:.9f} segundos")

if __name__ == "__main__":
    main()
