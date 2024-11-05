def vetor_intercecao(vetor1, vetor2):
    vetor_igual = []
    for item in vetor1:
        if item in vetor2:
            vetor_igual.append(item)
        else:
            continue
    return vetor_igual

vetor1 = []
for x in range(10):
    num = int(input("Digite um número para o primeiro vetor: "))
    vetor1.append(num)

vetor2 = []
for y in range(10):
    num = int(input("Digite um número para o segundo vetor: "))
    vetor2.append(num)

print(f"\nPrimeiro Vetor: {sorted(vetor1)}")
print(f"Segundo Vetor: {sorted(vetor2)}")
print(f"Vetor interceção: {sorted(vetor_intercecao(vetor1, vetor2))}\n")