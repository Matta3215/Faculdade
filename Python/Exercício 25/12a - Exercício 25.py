def posicao_igual(vetor):
    vetorigual = []
    vetorcomparacao = []
    for item in vetor:
        if item in vetorcomparacao:
            if item not in vetorigual:
                vetorigual.append(item)
        else:
            vetorcomparacao.append(item)
    return vetorigual

vetor = []
for x in range(10):
    num = int(input("Digite um número: "))
    vetor.append(num)
    
print(f"\nVetor original: {vetor}")
print(f"Elementos iguais no vetor: {posicao_igual(vetor)}\n")
