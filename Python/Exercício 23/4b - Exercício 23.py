n = int(input("Digite a quantidade de números que deseja colocar: "))

lista = []
listacerta = []

for x in range(n):
    num = int(input("Digite um número: "))
    lista.append(num)
    
listtemp = {}
for i in range(len(lista)):
    if listtemp.get(lista[i]) == None:
        listacerta.append(lista[i])
    listtemp[lista[i]] = lista[i]

print(f"Lista original: {lista}")
print(f"Lista certa: {listacerta}")
