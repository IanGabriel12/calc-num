from scipy.io import mmread

matriz_um = mmread('mtds_U2/matrizes/bcsstk22.mtx').toarray()

print(matriz_um[0][0])