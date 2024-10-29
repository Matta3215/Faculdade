n = int(input("Digite a quantidade de números que deseja colocar: "))

lista = []

for x in range(n):
    num = int(input("Digite um número: "))

    if num % 2 == 0:
        lista.append(num)

print(f"{sorted(lista)}")
