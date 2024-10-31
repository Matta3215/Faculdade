vetor1 = []
for x1 in range(5):
    num1 = int(input("Digite um número para o primeiro vetor: "))
    vetor1.append(num1)

vetor2 = []
for x2 in range(5):
    num2 = int(input("Digite um número para o segundo vetor: "))
    vetor2.append(num2)

soma = 0
for i in range(5):
    produto = vetor1[i] * vetor2[i]
    soma += produto

print(f"\nPrimeiro vetor: {vetor1}")
print(f"Segundo vetor: {vetor2}")
print(f"O produto escalar é igual a: {soma}\n")