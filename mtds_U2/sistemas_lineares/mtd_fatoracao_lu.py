from .utils import resolve_inferior, resolve_superior
import numpy as np
def fatoracao_lu(A, b):
    '''
    Resolve um sistema de equações lineares Ax = b pelo método da FATORAÇÃO LU.
    Este método assume que A tem tamanho N x N e b tem tamanho N x 1

    Entrada: Matrizes A e b
    Retorno: Um vetor de tamanho N x 1. A solução do sistema
    '''

    N = len(A)
    L = np.zeros((N, N), dtype=float);
    U = np.copy(A)
    bb = np.copy(b)
    
    # print(U, bb)
    for i in range(0, N):
        linha_pivo_atual = i
        for j in range(i+1, N):
            if(abs(U[j, i]) > abs(U[linha_pivo_atual, i])):
                linha_pivo_atual = j

        if linha_pivo_atual != i:
            temp1 = np.copy(U[i, :])
            U[i, :]= U[linha_pivo_atual, :]
            U[linha_pivo_atual, :] = temp1

            temp2 = np.copy(b[i, :])
            bb[i, :]= bb[linha_pivo_atual, :]
            bb[linha_pivo_atual, :] = temp2

        if U[i, i] == 0.0:
            raise ValueError("Erro: Pivô é 0 mesmo após pivotiamento")
        
        L[i, i] = 1.0

        for j in range(i+1, N):
            mult = U[j, i] / U[i, i]
            L[j, i] = mult
            for k in range(0, N):
                U[j, k] -= U[i, k] * mult

    y = resolve_inferior(L, bb)
    x = resolve_superior(U, y)
    residuo = b - (A @ x)
    print(b)
    print(A)
    print(x)
    return x, residuo, 0