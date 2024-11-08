import numpy as np

matriz = np.random.randint(1, 21, size=(4,4))

print(f"\nMatriz:\n{matriz}\n")
print(f"Submatriz selecionada:\n{matriz[2:, 2:]}\n")
