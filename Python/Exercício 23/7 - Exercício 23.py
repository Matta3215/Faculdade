n = int(input("\nDigite a quantidade de números que deseja colocar: "))

lista = []

for x in range(n):
    num = int(input("Digite um número: "))
    lista.append(num)

prod = 1
for i in lista:
    prod = prod * i

print(f"\nLista original: {sorted(lista)}")
print(f"Produto da lista: {prod}\n")
 