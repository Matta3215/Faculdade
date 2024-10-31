def produto(vetor):
    prod = 1
    for i in vetor:
        prod *= i
    return prod

vetor1 = []
for x1 in range(5):
    num = int(input("Digite um número para o primeiro vetor: "))
    vetor1.append(num)

vetor2 = []
for x2 in range(5):
    num = int(input("Digite um número para o segundo vetor: "))
    vetor2.append(num)

print(f"\nPrimeiro vetor: {vetor1}")
print(f"Segundo vetor: {vetor2}")

soma = produto(vetor1) + produto(vetor2)
print(f"A soma de seus produtos é igual a: {soma}\n")