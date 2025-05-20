def proxima_aproximacao(f, der_f, xk):
    return xk - f(xk)/der_f(xk)

def mtd_newton(f, der_f, a, b, e):
    xk = (a + b) / 2  # Chute inicial: ponto médio do intervalo
    num_iter = 0

    while abs(f(xk)) > e:
        num_iter += 1
        xk = proxima_aproximacao(f, der_f, xk)

    return (xk, num_iter)

