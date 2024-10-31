def produto_escalar(vet1, vet2):
    soma = 0
    for i in range(5):
        produto = vet1[i] * vet2[i]
        soma += produto
    return soma

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
print(f"O produto escalar é igual a: {produto_escalar(vetor1, vetor2)}\n")