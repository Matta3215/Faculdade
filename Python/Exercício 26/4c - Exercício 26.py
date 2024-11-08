import numpy as np

def vetor_quadrado(vetor):
    return vetor ** 2

vetor = np.array([1,2,3,4,5,6,7,8,9,10])

print(f"\nPrimeiro vetor: {vetor}")
print(f"Segundo vetor: {vetor_quadrado(vetor)}\n")