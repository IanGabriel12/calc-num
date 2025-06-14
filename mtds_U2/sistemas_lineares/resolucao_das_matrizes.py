# from scipy.io import mmread 
from fast_matrix_market import mmread
import numpy as np
import utils
from mtd_fatoracao_lu import fatoracao_lu
from mtd_gauss import elim_gauss
from mtd_gauss_jacobi import metodo_gaussjacobi, metodo_gaussjacobi2
from mtd_gauss_seidel import metodo_gauss_seidel, metodo_gauss_seidel2

import sys

matriz_um = mmread('mtds_U2/matrizes/bcsstk22.mtx').toarray()
matriz_dois = mmread('mtds_U2/matrizes/bcsstk23.mtx').toarray()
matriz_tres = mmread('mtds_U2/matrizes/bcsstk24.mtx').toarray()

B1 = np.array(
    list(map(lambda x: [int(x)], open('mtds_U2/matrizes/B1.txt').readline().split()))
)

B2 = np.array(
    list(map(lambda x: [int(x)], open('mtds_U2/matrizes/B2.txt').readline().split()))
)

B3 = np.array(
    list(map(lambda x: [int(x)], open('mtds_U2/matrizes/B3.txt').readline().split()))
)

testes = [(matriz_um, B1), (matriz_dois, B2), (matriz_tres, B3)]

def executar_metodo_no_teste(metodo_func, nome_metodo, num_teste, teste):
        A, B = teste
        solucao, residuo, iteracoes, tempo = metodo_func(A, B)
        utils.salvar_solucao_sistema_linear(nome_metodo, num_teste, solucao.flatten(), residuo.flatten(), iteracoes, tempo)

def executar_metodo(metodo_func, nome_metodo, lista_testes):
    for (i, teste) in enumerate(lista_testes):
        print(f"Rodando método {nome_metodo} no teste {i}")
        executar_metodo_no_teste(metodo_func, nome_metodo, i, teste)


# resolução com gauss jacobi
# executar_metodo(metodo_gaussjacobi, "gauss_jacobi", testes)

# # resolução com gauss seidel
# executar_metodo(metodo_gauss_seidel, "gauss_seidel", testes)

# # resolução com gauss
# executar_metodo(elim_gauss, "elim_gauss", testes)

# # resolução com fatoração lu
# executar_metodo(fatoracao_lu, "fatoracao_lu", testes)

if __name__ == "__main__":
    nome_metodo = sys.argv[1]

    metodo_func = ""
    if nome_metodo == "gauss":
        metodo_func = elim_gauss
    elif nome_metodo == "fatoracao_lu":
        metodo_func = fatoracao_lu
    elif nome_metodo == "gauss_jacobi":
        metodo_func = metodo_gaussjacobi
    elif nome_metodo == "gauss_jacobi2":
        metodo_func = metodo_gaussjacobi2
    elif nome_metodo == "gauss_seidel":
        metodo_func = metodo_gauss_seidel
    elif nome_metodo == "gauss_seidel2":
        metodo_func = metodo_gauss_seidel2
    else:
        raise NameError("Não existe método com esse nome")

    if len(sys.argv) == 2:
        executar_metodo(metodo_func, nome_metodo, testes)
    else:
        num_teste = int(sys.argv[2])
        print(f"Rodando método {nome_metodo} no teste {num_teste}")
        executar_metodo_no_teste(metodo_func, nome_metodo, num_teste, testes[num_teste])

