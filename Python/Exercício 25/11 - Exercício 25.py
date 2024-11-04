def posicao_maior(vetor):
    maior_valor = max(vetor)
    posicao_valor = 0
    for i in vetor:
        if i == maior_valor:
            return posicao_valor
        posicao_valor += 1

def posicao_menor(vetor):
    menor_valor = min(vetor)
    posicao_valor = 0
    for i in vetor:
        if i == menor_valor:
            return posicao_valor
        posicao_valor += 1

vetor = []
for x in range(5):
    num = int(input("Digite um número: "))
    vetor.append(num)
    
print(f"\nVetor original: {vetor}\n")
print(f"Posição do menor elemento no vetor: {posicao_menor(vetor)}")
print(f"Posição do maior elemento no vetor: {posicao_maior(vetor)}\n")