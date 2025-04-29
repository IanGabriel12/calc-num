import math
import time

precision = 10**-10

f = lambda x: x**2 + x - 6
phi = lambda x: math.sqrt(6-x)

f1 = lambda x: 2 * x**4 + 4 * x**3 + 3 * x**2 - 10 * x - 15
phi_f1 = lambda x: (2 * x**4 + 4 * x**3 + 3 * x**2 - 15) / 10

f2 = lambda x: x**5 - 2 * x**4 - 9 * x**3 + 22 * x**2 + 4 * x - 24
phi_f2 = lambda x: (24 - x**5 + 2 * x**4 + 9 * x**3 - 22 * x**2) / 4

# f3 = lambda x: math.log2(x + 1)
# phi_f3 = lambda x: math.log2(x + 1)

def fixed_point(a, b, phi):
    iterations = 0
    max_iterations = 500

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
    root = fixed_point(a, b, phi)
    end_time = time.perf_counter()

    abs_error = abs(root - exact_root)
    rel_error = abs_error / abs(exact_root)

    print(f"Raiz aproximada: {root:.9f}")
    print(f"f(raiz) = {f(root):.9f}")
    print(f"Erro absoluto: {abs_error:.9f}")
    print(f"Erro relativo: {rel_error:.9f}")
    print(f"Tempo de execução: {end_time - start_time:.9f} segundos")

    print("===========================")
    #
    # print("Método do ponto fixo para f1: f1(x) = 2x^4 + 4x^3 + 3x^2 - 10x - 15")
    # a1 = 0
    # b1 = 3
    # exact_root = 1.5
    #
    # start_time = time.perf_counter()
    # root = fixed_point(a1, b1, phi_f1)
    # end_time = time.perf_counter()
    #
    # abs_error = abs(root - exact_root)
    # rel_error = abs_error / abs(exact_root)
    #
    # print(f"Raiz aproximada: {root:.9f}")
    # print(f"f(raiz) = {f1(root):.9f}")
    # print(f"Erro absoluto: {abs_error:.9f}")
    # print(f"Erro relativo: {rel_error:.9f}")
    # print(f"Tempo de execução: {end_time - start_time:.9f} segundos")
    #
    # print("===========================")
    #
    # print("Método do ponto fixo para f2: f2(x) = x^5 - 2x^4 - 9x^3 + 22x^2 + 4x - 24")
    # a2 = 0
    # b2 = 5
    # exact_root = 2.0
    #
    # start_time = time.perf_counter()
    # root = fixed_point(a2, b2, phi_f2)
    # end_time = time.perf_counter()
    #
    # abs_error = abs(root - exact_root)
    # rel_error = abs_error / abs(exact_root)
    #
    # print(f"Raiz aproximada: {root:.9f}")
    # print(f"f(raiz) = {f2(root):.9f}")
    # print(f"Erro absoluto: {abs_error:.9f}")
    # print(f"Erro relativo: {rel_error:.9f}")
    # print(f"Tempo de execução: {end_time - start_time:.9f} segundos")
    #
    # print("===========================")
    #
    # print("Método do ponto fixo para f3: f3(x) = log2(x+1)")
    # a3 = -0.5
    # b3 = 0.5
    # exact_root = 0.0
    #
    # start_time = time.perf_counter()
    # root = fixed_point(a3, b3, phi_f3)
    # end_time = time.perf_counter()
    #
    # abs_error = abs(root - exact_root)
    # rel_error = abs_error / (abs(exact_root) + 1e-15)
    #
    # print(f"Raiz aproximada: {root:.9f}")
    # print(f"f(raiz) = {f3(root):.9f}")
    # print(f"Erro absoluto: {abs_error:.9f}")
    # print(f"Erro relativo: {rel_error:.9f}")
    # print(f"Tempo de execução: {end_time - start_time:.9f} segundos")
    #
if __name__ == "__main__":
    main()
