import numpy as np

def determinante(matriz):
    det_matriz = np.linalg.det(matriz)
    if det_matriz != 0:
        print(f"\nA matriz não é singular\n")
    else:
        print(f"\nA matriz é singular\n")

matriz = np.random.randint(1, 21, size=(4,4))
print(f"\nMatriz:\n{matriz}\n")
determinante(matriz)