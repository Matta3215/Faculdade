n = int(input("\nDigite a quantidade de números que deseja colocar: "))

vetor = []
for x in range(n):
    num = int(input("Digite um número: "))
    vetor.append(num)

print(f"Vetor: {vetor}")
print(f"Soma dos vetores: {sum(vetor)}")
