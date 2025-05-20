# utilização de método de newton para resolução das questões 3 e 4
import time

def f(x):
    return x**2 + x - 6

def der_f(x):
    return 2*x + 1

def proxima_aproximacao(f, der_f, xk):
    return xk - f(xk)/der_f(xk)

raiz = 2

def mtd_newton(f, der_f, a, b):
    e = 10**-8
    xk = (a + b) / 2  # Chute inicial: ponto médio do intervalo
    num_iter = 0
    start_time = time.time()

    while abs(f(xk)) > e:
        num_iter += 1
        xk = proxima_aproximacao(f, der_f, xk)

    end_time = time.time()
    seconds = end_time - start_time

    print(f"Raiz encontrada: {xk:.9f}")
    print(f"Número de iterações: {num_iter}")
    print(f"Tempo gasto (s): {seconds:.9f}")
    print(f"Erro relativo: {(raiz - xk)/raiz:.9f}")
    print(f"Erro absoluto: {(raiz - xk):.9f}")

# Chamando o método
mtd_newton(f, der_f, 1.8, 2.2)

