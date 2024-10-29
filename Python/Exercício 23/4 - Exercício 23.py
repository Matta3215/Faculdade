def remove_duplicatas(vetor):
    return list(dict.fromkeys(vetor))

n = int(input("Digite a quantidade de números que deseja colocar: "))

lista = []
for x in range(n):
    num = int(input("Digite um número: "))
    lista.append(num)

lista_sem_duplicatas = remove_duplicatas(lista)

print(f"Lista original: {lista}")
print(f"Lista sem duplicatas: {lista_sem_duplicatas}")