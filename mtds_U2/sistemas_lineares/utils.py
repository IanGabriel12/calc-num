import numpy as np
def resolve_inferior(A, b):
    '''
    Resolve um sistema trivial de equações lineares Ax = b, 
    assumindo que A é uma matriz triangular inferior.
    '''
    N = len(A)
    x = np.zeros((N, 1))
    for i in range(0, N):
        acc =  0
        for j in range(0, i):
            acc += A[i][j] * x[j][0]
        
        x[i][0] = (b[i][0] - acc) / A[i][i]

    return x


def resolve_superior(A, b):
    '''
    Resolve um sistema trivial de equações lineares Ax = b, 
    assumindo que A é uma matriz triangular superior.
    '''
    N = len(A)
    x = np.zeros((N, 1))
    for i in range(N-1, -1, -1): # de N-1 até 0
        acc = 0
        for j in range(i+1, N):
            acc += A[i][j] * x[j][0]
        
        x[i][0] = (b[i][0] - acc)/A[i][i]
    
    return x