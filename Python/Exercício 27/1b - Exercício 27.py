import numpy as np

def nao_nulo(linha, coluna):
    nulos = 0
    for i in range(linha): 
        for j in range(coluna):
            if j != 0:
                nulos += 1
    return nulos

linha = 5
coluna = 5
matriz = np.random.randint(0,5,(linha,coluna))

print(f"\nMatriz:\n{matriz}\n")

print(f"Posições não nulas na matriz: {nao_nulo(linha, coluna)}\n")