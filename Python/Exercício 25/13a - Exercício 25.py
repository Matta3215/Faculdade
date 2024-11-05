def posicao_igual(vetor):
    vetorigual = []
    for item in vetor:
        if item not in vetorigual:
            vetorigual.append(item)
        else:
            continue
    return vetorigual

vetor = []
for x in range(20):
    num = int(input("Digite um número: "))
    vetor.append(num)
    
print(f"\nVetor original: {vetor}")
print(f"Vetor sem elementos repetidos: {sorted(posicao_igual(vetor))}\n")