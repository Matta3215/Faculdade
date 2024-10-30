n = int(input("\nDigite a quantidade de números que deseja colocar: "))

lista = []
listacerta = []

for x in range(n):
    num = int(input("Digite um número: "))
    lista.append(num)
    
print(f"\nLista original: {lista}")
print(f"Lista certa: {list(set(lista))}\n")
