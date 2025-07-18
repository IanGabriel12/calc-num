import numpy as np
import time

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

def metodo_gaussjacobi(A, B, eps=1e-6, MAX_ITERACOES=1000):
    inicio = time.perf_counter()
    n = len(A)
    criterio = criterio_lc(A)
    if criterio == 0:
        print("Aviso: O método não garante a convergencia para esta matriz")

    for i in range(n):
        if A[i][i] == 0:
            for k in range(i + 1, n):
                if A[k][i] != 0:
                    # Troca as linhas i e k em A e B
                    A[[i, k]] = A[[k, i]]
                    B[[i, k]] = B[[k, i]]
                    break
            if A[i][i] == 0:
                raise ValueError("Erro: Não foi possível evitar divisão por zero mesmo após troca de linhas.")
    
    X = np.array([B[i] / A[i][i] for i in range(n)])
    v_aux = np.zeros(n)
    x = 0 # iterador
    while(x < MAX_ITERACOES): # número limite de iterações
        val_max = 0 # valor máximo da diferença x(k) - x(k-1)
        val_max_X = 0 # valor máximo do vetor X 
        for i in range(0, n):
            aux = 0 # variável auxiliar para calcular o somatório dos elementos da linha
            val_aux = 0 # variável auxiliar com um valor para determinar o valor atual da diferença x(k) - x(k-1)
            for j in range(0, n):
                if i != j: aux += A[i][j]*X[j] 
            X[i] = (1/A[i][i])*(B[i][0] - aux)
            val_aux = abs(X[i] - v_aux[i])
            v_aux[i] = X[i]
            if val_aux > val_max:
                val_max = val_aux
            if abs(X[i]) > val_max_X:
                val_max_X = abs(X[i])

        dist_relativo = val_max/val_max_X if val_max_X != 0 else val_max

        if val_max < eps and dist_relativo < eps:
            residuo = B - np.dot(A, X)
            fim = time.perf_counter()
            tempo = fim - inicio
            return X, residuo, x, tempo
        
        x+=1

    residuo = B - np.dot(A, X);
    fim = time.perf_counter()
    tempo = fim - inicio
    return X, residuo, x, tempo

        

def metodo_gaussjacobi2(A, b, eps=1e-6, MAX_ITERACOES=1000):
    inicio = time.perf_counter()
    n, _ = np.shape(A)
    inv = np.linalg.inv(A * np.eye(n))
    B = np.eye(n) - inv@A
    d = inv @ b
    X_prev = np.zeros(n)
    X = np.zeros(n)
    i = 0
    err = 1

    diag = np.diag(np.abs(A))
    resto_linhas = np.sum(np.abs(A), axis=1) - diag
    if np.any(diag <= resto_linhas):
        print("Nao converge: há diagonais nao dominantes")


    while i <= MAX_ITERACOES and err > eps:
        X = B @ X_prev + d
        err = np.max(np.abs(X - X_prev))/np.max(np.abs(X))

        X_prev = np.copy(X)

        i += 1


    residuo = 0


    fim = time.perf_counter()

    tempo = fim - inicio
    
    residuo = b - A @ X

    return X, residuo, i, tempo


    


