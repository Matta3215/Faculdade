import numpy as np

def tranposta(matriz):
    matriz_tranposta = np.transpose(matriz)
    print(f"\nMatriz transposta:\n{matriz_tranposta}\n")

matriz = np.random.randint(1, 16, size=(5,3))
print(f"\nMatriz:\n{matriz}\n")
tranposta(matriz)