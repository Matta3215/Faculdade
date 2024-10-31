vetor1 = []
for x1 in range(5):
    num1 = int(input("Digite um número para o primeiro vetor: "))
    vetor1.append(num1)

prod1 = 1 
for i1 in vetor1:
    prod1 *= i1

vetor2 = []
for x2 in range(5):
    num2 = int(input("Digite um número para o segundo vetor: "))
    vetor2.append(num2)

prod2 = 1 
for i2 in vetor2:
    prod2 *= i2

print(f"\nPrimeiro vetor: {vetor1}")
print(f"Segundo vetor: {vetor2}")

soma = prod1 + prod2
print(f"A soma de seus produtos é igual a: {soma}")