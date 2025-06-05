import numpy as np
def interpolacao_newton_completa(T, x_interpolar):
  """
  Calcula as diferenças divididas e realiza a interpolação
  via polinômio de Newton.

  Args:
      T (list): Lista de pontos T[i] = (x_i, y_i).
      x_interpolar (float): O valor que se quer interpolar.

  Returns:
      tuple: Uma tupla contendo a matriz de diferenças divididas
             e o valor interpolado em x_interpolar.
  """
  n = len(T)
  fdd = np.zeros((n, n))

  # Preencher a primeira coluna com os valores de y
  for i in range(n):
    fdd[i][0] = T[i][1]

  # as diferenças divididas
  for j in range(1, n):
    for i in range(n - j):
      fdd[i][j] = (fdd[i+1][j-1] - fdd[i][j-1]) / (T[i+j][0] - T[i][0])

  # fazer a interpolação
  P = fdd[0][0] # O primeiro termo é f(x_0)

  for j in range(1, n):
    term = fdd[0][j]
    for i in range(j):
      term *= (x_interpolar - T[i][0])
    P += term

  return fdd, P
