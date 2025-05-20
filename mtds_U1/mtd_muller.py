import cmath

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

def mtd_muller(f, a, b, eps):
    num_iter = 0

    x0 = a
    x1 = (a + b) / 2
    x2 = b

    x3 = proxima_aproximacao_muller(f, x0, x1, x2)

    while abs(f(x3)) > eps and num_iter < 100:
        num_iter += 1
        x0, x1, x2 = x1, x2, x3
        x3 = proxima_aproximacao_muller(f, x0, x1, x2)

    return(x3.real, num_iter)
