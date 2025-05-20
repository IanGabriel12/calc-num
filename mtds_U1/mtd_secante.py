def proxima_raiz(f, xk, xkmenos1):
    return xk - f(xk)*(xk - xkmenos1)/(f(xk) - f(xkmenos1))

def mtd_secante(f, a, b, e):
    xkmenos1 = a
    xk = b
    cnt_iteracoes = 0

    while abs(f(xk)) > e:
        cnt_iteracoes += 1
        auxiliar = xk
        xk = proxima_raiz(f, xk, xkmenos1)
        xkmenos1 = auxiliar


    return (xk, cnt_iteracoes)

