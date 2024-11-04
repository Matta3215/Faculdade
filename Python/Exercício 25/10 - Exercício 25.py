def num_neg(vetor):
    qnt_neg = 0
    for i in vetor:
        if i < 0:
            qnt_neg += 1
    return qnt_neg

def soma_positivo(vetor):
    soma_pos = 0
    for i in vetor:
        if i >= 0:
            soma_pos += i
    return soma_pos


vetor = []
for x in range(10):
    num = float(input("Digite uma nota: "))
    vetor.append(num)

print(f"\nVetor original: {vetor}")
print(f"Quantidade de números negativos: {num_neg(vetor)}")
print(f"Soma dos números positivos: {soma_positivo(vetor)}\n")