def soma_posicao(vetor):
    x = int(input("Digite a posição de x (0 a 7): "))
    while x > 7 or x < 0:
        print("Valor inválido")
        x = int(input("Digite novamente a posição de x (0 a 7): "))
    
    y = int(input("Digite a posição de y (0 a 7): "))
    while y > 7 or y < 0:
        print("Valor inválido")
        y = int(input("Digite novamente a posição de y (0 a 7): "))
    
    vx = vetor[x]
    vy = vetor[y]
    soma = vx + vy
    return soma

vetor = []
for x in range(8):
    num = int(input("Digite um número: "))
    vetor.append(num)
    
print(f"\nVetor original: {vetor}")
print(f"Soma dos valores: {soma_posicao(vetor)}\n")