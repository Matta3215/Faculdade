import numpy as np

def info(matriz):
    print(f"Média da matriz: {np.mean(matriz).round(2)}")
    print(f"Desvio padrão da matriz: {np.std(matriz).round(2)}")
    print(f"Valor mínimo da matriz: {np.min(matriz)}")
    print(f"Valor máxima da matriz: {np.max(matriz)}\n")

matriz = np.random.randint(1, 101, size=(6,6))
print(f"\nMatriz:\n{matriz}\n")
info(matriz)