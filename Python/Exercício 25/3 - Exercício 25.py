def invertido(vetor):
    vetor.sort(reverse=True)
    return vetor

n = int(input("Digite a quantidade de números que deseja armazenar no vetor: "))

vetor = []
for x in range(n):
    num = int(input("Digite um número: "))
    vetor.append(num)

print(f"\nVetor: {vetor}")
print(f"Vetor invertido: {invertido(vetor)}\n")