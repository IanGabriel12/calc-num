from scipy.io import mmread 
import numpy as np
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

# resolução com fatoração lu
print(fatoracao_lu(matriz_um, B1))
print(fatoracao_lu(matriz_dois, B2))
print(fatoracao_lu(matriz_tres, B3))

# resolução com gauss jacobi
print(metodo_gaussjacobi(matriz_um, B1, eps=10e-6, MAX_ITERACOES=10000))
print(metodo_gaussjacobi(matriz_dois, B2, eps=10e-6, MAX_ITERACOES=10000))
print(metodo_gaussjacobi(matriz_tres, B3, eps=10e-6, MAX_ITERACOES=10000))

# resolução com gauss seidel
print(metodo_gauss_seidel(matriz_um, B1, eps=10e-6, MAX_ITERACOES=10000))
print(metodo_gauss_seidel(matriz_dois, B2, eps=10e-6, MAX_ITERACOES=10000))
print(metodo_gauss_seidel(matriz_tres, B3, eps=10e-6, MAX_ITERACOES=10000))

# resolução com gauss
print(elim_gauss(matriz_um, B1))
print(elim_gauss(matriz_dois, B2))
print(elim_gauss(matriz_tres, B3))