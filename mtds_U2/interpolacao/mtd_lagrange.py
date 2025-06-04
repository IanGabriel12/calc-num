def mtd_interp_lagrange(T, x):
    '''
        Interpolação via polinômios de lagrange
        Entrada: T -> Lista de pontos T[i] = (x_i, y_i)
                 x -> O valor que se quer interpolar
        Saída: O valor aproximado de f(x) após a interpolação
    '''
    c = len(T)
    P = 0
    for k in range(c):
        L = 1
        for j in range(c):
            if k != j:
                L *= (x - T[j][0])/(T[k][0] - T[j][0])

        P += T[k][1]*L

    return P

