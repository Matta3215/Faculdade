def vetor_quadrado(vetor):
    quadrado = 0
    posicao = 0
    vetor_novo = []
    for i in vetor:
        quadrado = i * i
        vetor_novo.insert(posicao, quadrado)
        posicao += 1
    return vetor_novo

vetor = []
for x in range(10):
    vetor.append(x+1)

print(f"\nPrimeiro vetor: {vetor}")
print(f"Segundo vetor: {vetor_quadrado(vetor)}\n")