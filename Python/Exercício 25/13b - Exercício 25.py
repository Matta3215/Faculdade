vetor = []
for x in range(20):
    num = int(input("Digite um número: "))
    vetor.append(num)
    
print(f"\nVetor original: {vetor}")
print(f"Vetor sem elementos repetidos: {list(set(vetor))}\n")
