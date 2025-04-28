def proxima_raiz(f, xk, xkmenos1):
    return xk - f(xk)*(xk - xkmenos1)/(f(xk) - f(xkmenos1))

def mtd_newton(f, a, b):
    e = 10**-8
    xkmenos1 = a
    xk = b
    cnt_iteracoes = 0
    ms = 0

    while abs(f(xk)) > e:
        cnt_iteracoes += 1
        auxiliar = xk
        xk = proxima_raiz(f, xk, xkmenos1)
        xkmenos1 = auxiliar

    print(f"Raíz encontrada: {xk:.8f}")
    print(f"Número de iterações: {cnt_iteracoes}")
    print(f"Tempo gasto (ms): {ms:.8f}")
    print(f"Erro relativo: {0}")
    print(f"Erro absoluto: {0}")
