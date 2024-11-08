import numpy as np

def calc_coordenada(i, j):
    return i * j

matriz = np.fromfunction(calc_coordenada, (3, 4), dtype=int)

print(f"\nMatriz:\n{matriz}\n")
 