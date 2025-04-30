import math

lista_func = [
    lambda x : x**2 + x - 6, # Questão 3
    lambda x : 2*x**4 + 4*x**3 + 3*x**2 - 10*x - 15, # Questões 4 e 5
    lambda x : x**5 - 2*x**4 - 9*x**3 + 22*x**2 + 4*x - 24 # Questões 4 e 5
]

# Funções de iteração para o método do ponto fixo
lista_iter_func = [
    lambda x: math.sqrt(6-x),
    lambda x: (2 * x**4 + 4 * x**3 + 3 * x**2 - 15) / 10,
    lambda x: (24 - x**5 + 2 * x**4 + 9 * x**3 - 22 * x**2) / 4
]

# Derivadas para o método de newton
lista_derivadas = [
    lambda x : 2*x + 1,
    lambda x : 8*x**3 + 12*x**2 + 6*x - 10,
    lambda x : 5*x**4 - 8*x**3 - 27*x**2 + 44*x + 4
]
