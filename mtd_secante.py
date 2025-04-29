import time
def proxima_raiz(f, xk, xkmenos1):
    return xk - f(xk)*(xk - xkmenos1)/(f(xk) - f(xkmenos1))

raiz_vdd = 2
def mtd_secante(f, a, b):
    e = 10**(-10)
    xkmenos1 = a
    xk = b
    cnt_iteracoes = 1
    start_time = time.time();

    while abs(f(xk)) > e:
        cnt_iteracoes += 1
        auxiliar = xk
        xk = proxima_raiz(f, xk, xkmenos1)
        xkmenos1 = auxiliar

    end_time = time.time();
    seconds = end_time - start_time
    
    print(f"Raíz encontrada: {xk:.8f}")
    print(f"Número de iterações: {cnt_iteracoes}")
    print(f"Tempo gasto (s): {seconds:.8f}")
    print(f"Erro relativo: {(raiz_vdd - xk)/raiz_vdd:.8f}")
    print(f"Erro absoluto: {(raiz_vdd - xk):.8f}")

f = lambda x : x*x + x - 6
mtd_secante(f, 1.8, 2.2)
