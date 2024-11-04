def soma_impar(vetor):
    impar = 0
    for i in vetor:
        if i % 2 != 0:
            impar += i
    return impar

def vetor_modificado(vetor):
    valor4 = vetor[4]
    vetor.pop(5)
    vetor.pop(4)
    valor4 *= 100
    vetor.insert(4, valor4)
    return vetor
    
vetor = []
for x in range(6):
    num = int(input("Digite um número: "))
    vetor.append(num)

print(f"\nVetor original: {vetor}")
print(f"Soma dos ímpares: {soma_impar(vetor)}")
print(f"Vetor modificado: {vetor_modificado(vetor)}\n")