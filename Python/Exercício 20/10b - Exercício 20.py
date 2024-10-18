n = int(input("Digite uma quantidade de números que deseja colocar na lista: "))

lista = []

for i in range(n):
    num = int(input("Digite um número: "))
    
    lista.append(num)

print(f"\n{lista}")

print(f"{list(reversed(lista))}\n")