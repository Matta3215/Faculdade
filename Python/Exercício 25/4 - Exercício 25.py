def quadrado(vetor):
    vetor_quadrado = []
    for i in vetor:
        quad = i * i
        vetor_quadrado.append(quad)
    return vetor_quadrado

vetor = []
for x in range(10):
    num = int(input("Digite um número: "))
    vetor.append(num)
    
print(f"\nVetor original: {vetor}")
print(f"Vetor modificado: {quadrado(vetor)}\n")