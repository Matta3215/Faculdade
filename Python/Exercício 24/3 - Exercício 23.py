def par_impar(vetor):
    par = 0
    impar = 0
    for i in vetor:       
        if i % 2 == 0:
            par += 1
        else:
            impar += 1
    print(f"Pares: {par}; Ímpares: {impar}")
        

vetor = []
for x in range(20):
    num = int(input("Digite um número: "))
    vetor.append(num)

print(f"Vetor: {vetor}")
par_impar(vetor)
