def posicao_igual(vetor):
    vetorigual = []
    contagem = {}
    for item in vetor:
        if item in contagem:
            if item not in vetorigual:
                vetorigual.append(item)
        else:
            contagem[item] = 1
    return vetorigual

vetor = []
for x in range(10):
    num = int(input("Digite um número: "))
    vetor.append(num)
    
print(f"\nVetor original: {vetor}")
print(f"Elementos iguais no vetor: {posicao_igual(vetor)}\n")
