import numpy as np
from mtds_U2.sistemas_lineares.mtd_fatoracao_lu import fatoracao_lu
from mtds_U2.sistemas_lineares.mtd_gauss import elim_gauss
from mtds_U2.sistemas_lineares.mtd_gauss_jacobi import metodo_gaussjacobi
from mtds_U2.sistemas_lineares.mtd_gauss_seidel import metodo_gauss_seidel

from mtds_U2.interpolacao.mtd_lagrange import mtd_interp_lagrange
from mtds_U2.interpolacao.mtd_newton import interpolacao_newton_completa

print("Sistemas Lineares")
print("Questões da lista: ")

def print_questao_15(A, b):
    try:
        resposta, residuo, iteracoes, tempo = elim_gauss(A.copy(), b.copy())
        print(resposta.flatten(), residuo.flatten())
        resposta, residuo, iteracoes, tempo = fatoracao_lu(A.copy(), b.copy())
        print(resposta.flatten(), residuo.flatten())
    except ValueError as ex:
        print("Sistema não tem solução única")
    
def print_questao_16(A, b):
    try:
        resposta, residuo, iteracoes, tempo = metodo_gaussjacobi(A.copy(), b.copy(), 1e-3, 5)
        print(resposta.flatten(), residuo.flatten(), iteracoes)
        resposta, residuo, iteracoes, tempo = metodo_gauss_seidel(A.copy(), b.copy(), 1e-3, 5)
        print(resposta.flatten(), residuo.flatten(), iteracoes)
    except ValueError as ex:
        print("Sistema não tem solução única")

def print_questao_17(A, b):
    try:
        resposta, residuo, iteracoes, tempo = elim_gauss(A.copy(), b.copy())
        print(resposta.flatten(), residuo.flatten())
        resposta, residuo, iteracoes, tempo = metodo_gauss_seidel(A.copy(), b.copy(), 1e-3, 10)
        print(resposta.flatten(), residuo.flatten(), iteracoes)
    except ValueError as ex:
        print("Sistema não possui solução única")

def print_questao_19(A, b):
    try:
        resposta, residuo, iteracoes, tempo = elim_gauss(A.copy(), b.copy())
        print(resposta.flatten(), residuo.flatten())
        resposta, residuo, iteracoes, tempo = fatoracao_lu(A.copy(), b.copy())
        print(resposta.flatten(), residuo.flatten())
        resposta, residuo, iteracoes, tempo = metodo_gaussjacobi(A.copy(), b.copy(), 5e-2, 5)
        print(resposta.flatten(), residuo.flatten(), iteracoes)
        resposta, residuo, iteracoes, tempo = metodo_gauss_seidel(A.copy(), b.copy(), 5e-2, 5)
        print(resposta.flatten(), residuo.flatten(), iteracoes)
    except ValueError as ex:
        print("Sistema não tem solução única")

def print_questao_21(P, x):
    resposta = mtd_interp_lagrange(P, x)
    print(f"f({x}) = {resposta}")


def print_questao_22(P, x):
    _diferencas, resposta = interpolacao_newton_completa(P, x)
    print(f"f({x}) = {resposta}")


def print_questao_23(P, x):
    resposta = mtd_interp_lagrange(P, x)
    print(f"f({x}) = {resposta}")


def print_questao_24(P, x, observado):
    resposta = mtd_interp_lagrange(P, x)
    print(f"f({x}) = {resposta}")
    print(f"Diferença entre o valor observado e o estipulado: |{resposta}-{observado}| = {abs(resposta-observado)}")



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

# Questão 21 (Lagrange)
print("Questão 21")
x = 0.75
P = np.array([[0.0, 1.0], [0.2, 1.2408], [0.4, 1.5735], [0.6, 2.0333], [0.8, 2.6965], [1.0, 3.7183]])
print_questao_21(P, x)

# Questao 22 (Newton)

print("Questão 22")
x = 15.6
P = np.array([[0.0, 10.0], [10.0, 20.56], [20.0, 30.67], [30.0, 67.78]])
print_questao_22(P, x)


# Questao 23
print("Questao 23")
x = 7
P = np.array([[0., 6.67], [6., 17.33], [10., 42.67], [13., 37.33], [17., 30.1]])
print_questao_23(P, x)

# Questao 24
print("Questão 24")
P = np.array([[1970.0, 327.0], [1980.0, 337.0], [1990.0, 335.0], [2000.0, 370.0], [2010.0, 388.0]])
x = 2008.
observado = 381.
print_questao_24(P, x, observado)





