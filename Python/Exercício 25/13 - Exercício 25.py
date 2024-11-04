vetor = []
for x in range(10):
    num = int(input("Digite um número: "))
    vetor.append(num)
    
print(f"\nVetor original: {vetor}")
print(f"Elementos iguais no vetor: {list(set(vetor))}\n")
