import numpy as np
B1 = np.random.randint(1, 51, size=(138, 1))
B2 = np.random.randint(1, 51, size=(3134, 1))
B3 = np.random.randint(1, 51, size=(3562, 1))

with open("mtds_U2/matrizes/B1.txt", "w") as arquivo:
    for x in B1.flatten():
        arquivo.write(f"{x} ")

with open("mtds_U2/matrizes/B2.txt", "w") as arquivo:
    for x in B2.flatten():
        arquivo.write(f"{x} ")

with open("mtds_U2/matrizes/B3.txt", "w") as arquivo:
    for x in B3.flatten():
        arquivo.write(f"{x} ")