import numpy as np

def prod_matricial(matriz1, matriz2):
    matriz_quadrada1 = matriz1 ** 2
    matriz_quadrada2 = matriz2 ** 2
    if matriz1.shape == matriz2.shape:
        return np.dot(matriz_quadrada1, matriz_quadrada2)
    else:
        exit()
    
matriz1 = np.random.randint(1, 10, size=(3,3))
matriz2 = np.random.randint(1, 10, size=(3,3))

print(f"\nMatrizes:\n{matriz1}\n\n{matriz2}\n")
print(f"Produto matricial:\n{prod_matricial(matriz1, matriz2)}\n")