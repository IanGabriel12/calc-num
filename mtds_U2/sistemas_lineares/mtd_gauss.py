import numpy as np

def resolve_superior(A, b):
    n, _ = np.shape(A)
    x = np.zeros((n, 1), dtype=float)
    for i in range(n-1, -1, -1):
        x[i,0] = (b[i,0] - A[i,i:n]@x[i:n, 0])/ A[i,i]
    return x

def elim_gauss(A, b):
    n, _ = np.shape(A)
    aumentada = np.concatenate((A, b), axis=1)

    for i in range(n-1):
        linha_pivo_atual = i
        for j in range(i+1, n):
            if(abs(aumentada[j, i]) > abs(aumentada[linha_pivo_atual, i])):
                linha_pivo_atual = j

        if linha_pivo_atual != i:
            temp = np.copy(aumentada[i, :])
            aumentada[i, :]= aumentada[linha_pivo_atual, :]
            aumentada[linha_pivo_atual, :] = temp

        pivo = aumentada[i,i]

        if pivo == 0.0:
            raise ValueError("Erro: Pivô é 0 mesmo após pivotiamento")


        for j in range(i+1, n):
            fator = aumentada[j, i] / pivo
            aumentada[j, :] = aumentada[j, :] - fator*aumentada[i, :]

        
    U = aumentada[:, 0:n]
    y = aumentada[:, n:]
    x = resolve_superior(U, y)
    residuo = b - (A @ x)
    return x, residuo, 0


if __name__ == '__main__':
    A = np.array([[3, 3, 4],
                       [1, 1, 2],
                       [4, 3, -2]], dtype=float)

    b = np.array([[1],
                       [2],
                       [3]], dtype=float)


    x = elim_gauss(A, b)
    print(f'Solucao x:  {x}')

    print("\nVerificação Ax =", A @ x)
    print("b =", b)

