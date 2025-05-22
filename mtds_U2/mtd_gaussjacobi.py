import numpy as np

def criterio_lc(A):
    n = len(A)

    ctr_colunas = 1
    ctr_linhas = 1
    for i in range(0, n):
        val_ctrl = 0
        val_ctrc = 0
        for j in range(0, n):
            val_ctrl += A[i][j]
            val_ctrc += A[j][i]
        if (A[j][j] < val_ctrc - A[j][j]):
            ctr_colunas = -1
        if (A[i][i] < val_ctrl - A[i][i]):
            ctr_linhas = -1
    
    if ctr_linhas == -1 and ctr_colunas == -1:
        return 0
    else:
        return 1

def metodo_gaussjacobi(A, X, B, eps):
    n = len(A)
    criterio = criterio_lc(A)
    if criterio == 0:
        return "O método não converge"

    v_aux = np.zeros(n)
    x = 0 # iterador
    while(x < 10000): # número limite de iterações
        val_max = 0 # valor máximo da diferença x(k) - x(k-1)
        val_max_X = 0 # valor máximo do vetor X 
        for i in range(0, n):
            aux = 0 # variável auxiliar para calcular o somatório dos elementos da linha
            val_aux = 0 # variável auxiliar com um valor para determinar o valor atual da diferença x(k) - x(k-1)
            for j in range(0, n):
                if i != j: aux += A[i][j]*X[j] 
            X[i] = (1/A[i][i])*(B[i] - aux)
            val_aux = abs(X[i] - v_aux[i])
            v_aux[i] = X[i]
            if val_aux > val_max:
                val_max = val_aux
            if abs(X[i]) > val_max_X:
                val_max_X = abs(X[i])

        if val_max < eps and val_max/val_max_X < eps:
            return X 
        
        x+=1

    print("Número máximo de iterações")

        