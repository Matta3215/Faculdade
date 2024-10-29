n = int(input("\n3Digite a quantidade de números que deseja colocar: "))

lista = []

for x in range(n):
    num = int(input("Digite um número: "))

    lista.append(num)

print(f"Menor número: {min(lista)}")
print(f"Maior número: {max(lista)}\n")
