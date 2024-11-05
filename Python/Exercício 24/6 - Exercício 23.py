def vetor_sem_iguais(vetor):
    vetor_igual = []
    for item in vetor:
        if item not in vetor_igual:
            vetor_igual.append(item)
        else:
            continue
    return vetor_igual

vetor = []
for x in range(10):
    num = int(input("Digite um número: "))
    vetor.append(num)

print(f"\nVetor: {vetor}")
print(f"Vetor sem elementos iguais: {sorted(vetor_sem_iguais(vetor))}\n")