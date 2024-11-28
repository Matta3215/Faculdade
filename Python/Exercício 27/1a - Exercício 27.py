import numpy as np

linha = 5
coluna = 5
matriz = np.random.randint(0,5,(linha,coluna))

print(f"\nMatriz:\n{matriz}\n")

nulos = 0
for i in range(linha): 
    for j in range(coluna):
        if j != 0:
            nulos += 1
print(f"Posições não nulas na matriz: {nulos}\n")