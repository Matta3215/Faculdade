n = int(input("Digite a quantidade de números que deseja colocar: "))

lista = []

for x in range(n):
    num = int(input("Digite um número: "))

    lista.append(num)

print(sum(lista))
