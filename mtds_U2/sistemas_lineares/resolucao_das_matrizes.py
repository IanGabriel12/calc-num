from scipy.io import mmread 
import numpy as np
import utils
from mtd_fatoracao_lu import fatoracao_lu
from mtd_gauss import elim_gauss
from mtd_gauss_jacobi import metodo_gaussjacobi
from mtd_gauss_seidel import metodo_gauss_seidel

matriz_um = mmread('mtds_U2/matrizes/bcsstk22.mtx').toarray()
matriz_dois = mmread('mtds_U2/matrizes/bcsstk23.mtx').toarray()
matriz_tres = mmread('mtds_U2/matrizes/bcsstk24.mtx').toarray()

B1 = np.random.randint(1, 51, size=(138, 1))
B2 = np.random.randint(1, 51, size=(3134, 1))
B3 = np.random.randint(1, 51, size=(3562, 1))

testes = [(matriz_um, B1), (matriz_dois, B2), (matriz_tres, B3)]

def executar_metodo(metodo_func, nome_metodo, lista_testes):
    for (i, teste) in enumerate(lista_testes):
        A, B = teste
        solucao, residuo, iteracoes, tempo = metodo_func(A, B)
        utils.salvar_solucao_sistema_linear(nome_metodo, i, solucao.flatten(), residuo.flatten(), iteracoes, tempo)


# resolução com gauss jacobi
executar_metodo(metodo_gaussjacobi, "gauss_jacobi", testes)

# resolução com gauss seidel
executar_metodo(metodo_gauss_seidel, "gauss_seidel", testes)

# resolução com gauss
executar_metodo(elim_gauss, "elim_gauss", testes)

# resolução com fatoração lu
executar_metodo(fatoracao_lu, "fatoracao_lu", testes)