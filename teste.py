from mtds_U2.fatoracao_lu import fatoracao_lu

A = [
    [0, 1, 7],
    [1, 3, 2],
    [2, 5, 3]
]

b = [
    1, 
    2, 
    3
]

x = fatoracao_lu(A, b)

print(x)