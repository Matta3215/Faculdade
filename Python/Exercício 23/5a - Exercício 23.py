n = int(input("\nDigite a quantidade de números ou palavras que deseja colocar: "))

lista = []

for x in range(n):
    elemento = input("Digite um número ou palavra: ")
    lista.append(elemento)

print(f"\nLista original: {lista}")

contagem = {}
for item in lista:
    if item in contagem:
        contagem[item] += 1
    else:
        contagem[item] = 1

print(f"Lista com contagem de ocorrências: {contagem}\n")
