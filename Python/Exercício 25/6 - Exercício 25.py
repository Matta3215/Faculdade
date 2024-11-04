def pares(vetor):
    qnt_pares = 0
    for i in vetor:
        if i % 2 == 0:
            qnt_pares += 1
    return qnt_pares

vetor = []
for x in range(10):
    num = int(input("Digite um número: "))
    vetor.append(num)
    
print(f"\nVetor original: {vetor}")
print(f"Quantidade de pares: {pares(vetor)}\n")