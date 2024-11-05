def vetorinvertido(vetor):
    vetor.sort(reverse=True)
    return vetor

vetor = []
for x in range(10):
    num = int(input("Digite um número: "))
    vetor.append(num)

print(f"\nVetor: {vetor}")
print(f"Vetor invertido: {vetorinvertido(vetor)}\n")