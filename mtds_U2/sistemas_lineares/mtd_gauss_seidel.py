import numpy as np
import time

"""
Verifica o critério das linhas e colunas para convergência.

Args:
    A (np.ndarray): Matriz dos coeficientes.

Returns:
    int: True se o critério de convergência for satisfeito, False caso contrário.
"""
def criterio_lc(A):
    n = len(A)
    
    ctr_colunas = True
    ctr_linhas = True
    
    for i in range(0, n):
        sum_linha_without_diag = 0
        sum_coluna_without_diag = 0
        
        # elemento da diagonal principal
        val_diagonal = abs(A[i][i]) # em módulo né?

        for j in range(0, n):
          if i != j:
            sum_linha_without_diag += abs(A[i][j])
            sum_coluna_without_diag += abs(A[j][i])

        # Verifica se o valor da diagonal é maior que a soma da coluna
        if (val_diagonal < sum_coluna_without_diag):
          ctr_colunas = False
        # Verifica se o valor da diagonal é maior que a soma da linha
        if (val_diagonal < sum_linha_without_diag):
          ctr_linhas = False
    
    if ctr_linhas or ctr_colunas:
        return True
    else:
        return False

"""
Implementa o método de Gauss-Seidel para resolver sistemas lineares.

Args:
    A (np.ndarray): Matriz dos coeficientes.
    X (np.ndarray): Vetor inicial de soluções.
    B (np.ndarray): Vetor dos termos independentes.
    eps (float): Critério de parada (precisão). Default é 1e-6.

Returns:
    np.ndarray: Vetor solução aproximado.
    str: Mensagem indicando que o método não converge.
    None: Se o número máximo de iterações for atingido.
"""
def metodo_gauss_seidel(A, B, eps=1e-6, MAX_ITERACOES=1000):
    inicio = time.perf_counter()
    n = len(A)

    # Verifica o critério de convergência (pelo menos um critério deve ser satisfeito)
    if not (criterio_lc(A)):
        print("Aviso: O método não garante a convergencia para esta matriz")

    # Corrige elementos nulos na diagonal
    for i in range(n):
        if A[i][i] == 0:
            for k in range(i + 1, n):
                if A[k][i] != 0:
                    # Troca as linhas i e k em A e B
                    A[[i, k]] = A[[k, i]]
                    B[[i, k]] = B[[k, i]]
                    break
            if A[i][i] == 0:
                raise "Erro: Não foi possível evitar divisão por zero mesmo após troca de linhas."
    
    X = np.array([B[i] / A[i][i] for i in range(n)])
    x = 0  # iterador
    while x < MAX_ITERACOES:
        X_anterior = np.copy(X)

        for i in range(n):
            aux = 0
             # calcula os ax_i(na primeira iteração usa Vetor inicial de soluções) e soma 
            for j in range(n):
                if i != j:
                    aux += A[i][j] * X[j]

            if A[i][i] == 0:
                raise ValueError("Erro: Elemento da diagonal é zero, divisão por zero!") # precisa msm?

            X[i] = (1 / A[i][i]) * (B[i] - aux) # calcula o 1/a_ii(b - ax_i ...)

        # Calcula a distância absoluta
        dist_absoluto = np.max(np.abs(X - X_anterior)) 

        # Calcula a distância relativa
        norma_X_atual = np.max(np.abs(X))
        dist_relativo = dist_absoluto / norma_X_atual if norma_X_atual != 0 else dist_absoluto

        # Critério de parada: distância absoluta E distância relativa devem ser menores que eps
        if dist_absoluto < eps and dist_relativo < eps:
            # Calcula o vetor resíduo
            residuo = B - np.dot(A, X)
            fim = time.perf_counter()
            tempo = fim - inicio
            return X, residuo, x, tempo

        x += 1

    residuo = B - np.dot(A, X)
    fim = time.perf_counter()
    tempo = fim - inicio
    return X, residuo, x, tempo  


def metodo_gauss_seidel2(A, b, eps=1e-6, MAX_ITERACOES=1000):
    inicio = time.perf_counter()
    if not (criterio_lc(A)):
        print("Aviso: O método não garante a convergencia para esta matriz")
    n = len(b)
    X = np.zeros_like(b, dtype=np.double)
    X_anterior = np.zeros_like(X)
    
    i = 0
    while i < MAX_ITERACOES:
        X_anterior[:] = X
        
        for j in range(n):
            soma = np.dot(A[j, :j], X[:j]) + np.dot(A[j, j+1:], X_anterior[j+1:])
            
            X[j] = (b[j] - soma) / A[j, j]
            
        er = np.linalg.norm(X - X_anterior, np.inf) / np.linalg.norm(X, np.inf)
        
        if er < eps:
            break
        i += 1
            
    fim = time.perf_counter()
    tempo = fim - inicio
    residuo = b - np.dot(A, X)
    
    return X, residuo, i + 1, tempo
