import numpy as np

def determinante(matriz):
    det_matriz = np.linalg.det(matriz)
    if det_matriz != 0:
        inv_matriz = np.linalg.inv(matriz)
        print(f"\nMatriz invertida:\n{inv_matriz}\n")
    else:
        print("\n A matriz não é invertível")

matriz = np.random.randint(1, 11, size=(3,3))
print(f"\nMatriz:\n{matriz}\n")
determinante(matriz)