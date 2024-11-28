import numpy as np

def multiplicacao_matrizes(matriz1, matriz2):
    multi_matriz = 0
    for i in range(linha):
        for j in range(coluna):
            multi_matriz += matriz1[i][j] * matriz2[i][j]
    return multi_matriz

def soma_matrizes(matriz1, matriz2):
    soma_matriz = 0
    for i in range(linha):
        for j in range(coluna):
            soma_matriz += (matriz1[i][j] + matriz2[i][j])
    return soma_matriz

def sub_matrizes(matriz1, matriz2):
    sub_matriz = 0
    for i in range(linha):
        for j in range(coluna):
            sub_matriz += (matriz1[i][j] - matriz2[i][j])
    return sub_matriz


linha, coluna = 3, 3
matriz1 = np.random.randint(0, 11, (linha,coluna))
matriz2 = np.random.randint(0, 11, (linha,coluna))

print(f"\nPrimeira matriz:\n{matriz1}\n")

print(f"\nSegunda matriz:\n{matriz2:}\n")

print(f"Multiplicação das matrizes: {multiplicacao_matrizes(matriz1, matriz2)}\n")

print(f"Soma das matrizes: {soma_matrizes(matriz1, matriz2)}\n")

print(f"Subtração das matrizes: {sub_matrizes(matriz1, matriz2)}\n")