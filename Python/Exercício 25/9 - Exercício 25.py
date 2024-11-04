def media(vetor):
    valores = 0
    for i in vetor:
        valores += i
    calc_media = valores / len(vetor)
    return calc_media

vetor = []
for x in range(15):
    num = float(input("Digite uma nota: "))
    vetor.append(num)

print(f"\nVetor original: {vetor}")
print(f"Média dos alunos: {media(vetor)} \n")