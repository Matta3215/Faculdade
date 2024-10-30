n = int(input("\nDigite a quantidade de números que deseja colocar: "))

lista = []

for x in range(n):
    num = int(input("Digite um número: "))
    lista.append(num)
    
print(f"\nLista original: {lista}")

lista.sort(reverse = True)
print(f"Lista certa: {lista}\n")
 