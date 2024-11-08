import numpy as np

matriz = np.array([9.5, 9, 8, 0, 5, 6, 7, 8.5, 9, 8, 8, 0],)

matriz.shape = (3,4)

print(f"\nMatriz:\n{matriz}")

print(f"\nNota do primeiro aluno: {matriz[0][1]}")
print(f"\nNota do terceiro aluno: {matriz[2][3]}")