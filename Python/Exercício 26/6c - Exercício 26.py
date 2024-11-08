import numpy as np

def soma_vetores(vetor1, vetor2):
    vetor_soma = vetor1 + vetor2
    soma = 0
    for i in vetor_soma:
        soma += i
    print(f"Soma dos elementos dos vetores: {vetor_soma} = {soma}")

def prod_escalar_vetores(vetor1, vetor2):
    vetor_prod = vetor1 * vetor2
    prod = 0
    for i in vetor_prod:
        prod += i
    print(f"Produto escalar dos vetores: {vetor_prod} = {prod}\n")

vetor1 = np.random.randint(1, 11, size=(5))
vetor2 = np.random.randint(1, 11, size=(5))

print(f"\nVetores:\n{vetor1}\n{vetor2}\n")
soma_vetores(vetor1, vetor2)
prod_escalar_vetores(vetor1, vetor2)