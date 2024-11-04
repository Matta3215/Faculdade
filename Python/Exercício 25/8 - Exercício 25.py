def posicao(vetor):
    maior_valor = max(vetor)
    posicao_valor = 0
    for i in vetor:
        if i == maior_valor:
            return posicao_valor
        posicao_valor += 1

vetor = []
for x in range(10):
    num = int(input("Digite um número: "))
    vetor.append(num)
    
print(f"\nVetor original: {vetor}")
print(f"Maior elemento: {max(vetor)}; Posição no vetor: {posicao(vetor)} \n")