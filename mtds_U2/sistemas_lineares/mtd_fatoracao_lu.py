from .utils import resolve_inferior, resolve_superior

def fatoracao_lu(A, b):
    '''
    Resolve um sistema de equações lineares Ax = b pelo método da FATORAÇÃO LU.
    Este método assume que A tem tamanho N x N e b tem tamanho N x 1

    Entrada: Matrizes A e b
    Retorno: Um vetor de tamanho N x 1. A solução do sistema
    '''

    N = len(A)
    L = [[0 for _ in range(N)] for _ in range(N)]
    U = A.copy()
    bb = b.copy()
    
    for i in range(0, N):
        if U[i][i] == 0:
            melhor_linha = i+1
            maior_valor = U[i+1][i]
            for j in range(i+2, N):
                if maior_valor < U[j][i]:
                    melhor_linha = j
                    maior_valor = U[j][i]
            bb[i], bb[melhor_linha] = bb[melhor_linha], bb[i]
            U[i], U[melhor_linha] = U[melhor_linha], U[i]
            L[i], L[melhor_linha] = L[melhor_linha], L[i]
        
        L[i][i] = 1

        for j in range(i+1, N):
            mult = U[j][i] / U[i][i]
            L[j][i] = mult
            for k in range(0, N):
                U[j][k] -= U[i][k] * mult

    y = resolve_inferior(L, bb)
    x = resolve_superior(U, y)
    residuo = b - (A @ x)
    return x, residuo, 0