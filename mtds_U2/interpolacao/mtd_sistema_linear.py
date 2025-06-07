import numpy as np
from ..sistemas_lineares.mtd_fatoracao_lu import fatoracao_lu
from ..sistemas_lineares.mtd_gauss import elim_gauss
from ..sistemas_lineares.mtd_gauss_jacobi import metodo_gaussjacobi
from ..sistemas_lineares.mtd_gauss_seidel import metodo_gauss_seidel


def mtd_sistema_linear(P, mtd_resolucao_sistema):
    '''
        Interpolação polinomial pela resolução de um sistema linear
        Entrada: P -> Lista de pontos P[i] = (x_i, y_i)
        Saída: Uma lista com os coeficientes do polinômio interpolado (a0, a1, a2, ..., an)
        a_i é o coeficiente do termo x^i
    '''

    sz = len(P);
    b = list(map(lambda x: x[1], P));

    A = np.zeros((sz, sz))

    for i in range(0, sz):
        x_i = P[i][0]
        for j in range(0, sz):
            A[i][j] = x_i ** j

    return mtd_resolucao_sistema(A, b)[0]


def mtd_sistema_linear_fatoracao_lu(P):
    return mtd_sistema_linear(P, fatoracao_lu)

def mtd_sistema_linear_elim_gauss(P):
    return mtd_sistema_linear(P, elim_gauss)

def mtd_sistema_linear_gauss_jacobi(P):
    return mtd_sistema_linear(P, metodo_gaussjacobi)

def mtd_sistema_linear_metodo_gauss_seidel(P):
    return mtd_sistema_linear(P, metodo_gauss_seidel)