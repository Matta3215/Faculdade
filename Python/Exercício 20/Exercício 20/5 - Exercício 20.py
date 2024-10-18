n = int(input("Digite a quantidade de números que deseja colocar na lista: "))

lista = []

for x in range(n):
    num = float(input("Digite um número: "))
    lista.append(num)

print(f"{max(lista)}\n")