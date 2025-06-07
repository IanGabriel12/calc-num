import numpy as np
from mtds_U2.sistemas_lineares.mtd_fatoracao_lu import fatoracao_lu
from mtds_U2.sistemas_lineares.mtd_gauss import elim_gauss
from mtds_U2.sistemas_lineares.mtd_gauss_jacobi import metodo_gaussjacobi
from mtds_U2.sistemas_lineares.mtd_gauss_seidel import metodo_gauss_seidel


print("Sistemas Lineares")
print("Questões da lista: ")

def print_questao_15(A, b):
    try:
        resposta, residuo, iteracoes = elim_gauss(A.copy(), b.copy())
        print(resposta.flatten(), residuo.flatten())
        resposta, residuo, iteracoes = fatoracao_lu(A.copy(), b.copy())
        print(resposta.flatten(), residuo.flatten())
    except:
        print("Sistema não tem solução única")
    
    

def print_questao_16(A, b):
    try:
        resposta, residuo, iteracoes = metodo_gaussjacobi(A.copy(), b.copy(), 1e-3, 5)
        print(resposta.flatten(), residuo.flatten(), iteracoes)
        resposta, residuo, iteracoes = metodo_gauss_seidel(A.copy(), b.copy(), 1e-3, 5)
        print(resposta.flatten(), residuo.flatten(), iteracoes)
    except:
        print("Sistema não tem solução única")

def print_questao_17(A, b):
    try:
        resposta, residuo, iteracoes = elim_gauss(A.copy(), b.copy())
        print(resposta.flatten(), residuo.flatten())
        resposta, residuo, iteracoes = metodo_gauss_seidel(A.copy(), b.copy(), 1e-3, 10)
        print(resposta.flatten(), residuo.flatten(), iteracoes)
    except:
        print("Sistema não possui solução única")

def print_questao_19(A, b):
    try:
        resposta, residuo, iteracoes = elim_gauss(A.copy(), b.copy())
        print(resposta.flatten(), residuo.flatten())
        resposta, residuo, iteracoes = fatoracao_lu(A.copy(), b.copy())
        print(resposta.flatten(), residuo.flatten())
        resposta, residuo, iteracoes = metodo_gaussjacobi(A.copy(), b.copy(), 5e-2, 5)
        print(resposta.flatten(), residuo.flatten(), iteracoes)
        resposta, residuo, iteracoes = metodo_gauss_seidel(A.copy(), b.copy(), 5e-2, 5)
        print(resposta.flatten(), residuo.flatten(), iteracoes)
    except:
        print("Sistema não tem solução única")

# Questão 15 a)
A = np.array(
    [[-9, 5, 6],
    [2, 3, 1],
    [-1, 1, -3]], dtype=float
)

b = np.array([[11], [4], [-2]], dtype=float)

print_questao_15(A, b);



# Questão 15 b)
A = np.array(
    [[2, -1, 1],
    [3, 3, 9],
    [3, 3, 5]], dtype=float
)

b = np.array([[-1], [0], [4]], dtype=float)

print_questao_15(A, b)


# Questão 15 c) [não encontra solução]
A = np.array(
    [[0.252, 0.36, 0.12],
    [0.112, 0.16, 0.24],
    [0.147, 0.21, 0.25]], dtype=float
)

b = np.array([[7], [8], [9]], dtype=float)

print_questao_15(A, b)

# Questão 15 d)
A = np.array(
    [[3, -2, 5, 1],
    [-6, 4, -8, 1],
    [9, -6, 19, 1],
    [6, -4, -6, 15]], dtype=float
)

b = np.array([[7], [-9], [23], [11]], dtype=float)

print_questao_15(A, b)


# Questão 16 a)
A = np.array(
    [[10, -1, 2, 0],
    [-1, 11, -1, 3],
    [2, -1, 10, -1],
    [0, 3, -1, 8]], dtype=float
)

b = np.array([[0], [25], [-11], [15]], dtype=float)

print_questao_16(A, b)

# Questão 16 b)
A = np.array(
    [[0, 5, -1, 2],
    [0, 8, -1, 1],
    [2, 1, -1, -1],
    [0, -1, -2, 1]], dtype=float
)

b = np.array([[10], [16], [2], [-2]], dtype=float)
print_questao_16(A, b)


# Questão 16 c)
A = np.array(
    [[1, 0.5, -0.1, 0.1],
    [0.2, 1, -0.2, -0.1],
    [-0.1, -0.2, 1, 0.2],
    [0.1, 0.3, 0.2, 1]], dtype=float
)

b = np.array([[0.2], [-2.6], [1.0], [-2.5]], dtype=float)
print_questao_16(A, b)

# Questão 17
print("Questao 17")
A = np.array([
    [1, 1, -1, 2, -1],
    [2, 0, 0, 0, 0],
    [0, 2, 0, 0, 0],
    [4, 0, 0, 16, 0],
    [0, 0, 4, 0, 0]
], dtype=float)

b = np.array([
    [2], [2], [2], [20], [4]
])

print_questao_17(A, b)

# Questão 19
A = np.array(
    [[0, 15, 1, 3],
    [15, 2, 2, 3],
    [0, 4, 15, 1],
    [1, 2, 2, 15]], dtype=float
)

b = np.array([[-3], [4], [7], [5]], dtype=float)

print_questao_19(A, b)


