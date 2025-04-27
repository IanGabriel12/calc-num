# utilização de método de newton para resolução das questões 3 e 4
import time

def f(x):
    return x**2 + x - 6

def der_f(x):
    return 2*x + 1

def mtd_newton(x_0):
    e = 10**(-8)
    boolean = False
    i = 1
    start_time = time.time()

    while boolean == False:
        x_1 = x_0 - f(x_0)/der_f(x_0)

        if abs(x_1 - x_0) < e:
            end_time = time.time()  
            elapsed_time = end_time - start_time  
            print("A raiz aproximada foi, ", x_1, " depois de ", i, " iterações")
            print("Erro absoluto: ", abs(2 - x_1))
            print("Erro relativo: ", abs(2 - x_1)/x_1)
            print(elapsed_time)
            return x_1
        
        x_0 = x_1
        i+=1

mtd_newton(1.8)

