import numpy as np

def soma_vetores(vetor1, vetor2):
    return vetor1 + vetor2

def prod_escalar_vetores(vetor1, vetor2):
    return vetor1 * vetor2

vetor1 = np.random.randint(1, 11, size=(5))
vetor2 = np.random.randint(1, 11, size=(5))

print(f"\nVetores:\n{vetor1}\n{vetor2}\n")
print(f"Soma dos elementos dos vetores: {soma_vetores(vetor1,vetor2)}")
print(f"Produto escalar dos vetores: {prod_escalar_vetores(vetor1,vetor2)}\n")