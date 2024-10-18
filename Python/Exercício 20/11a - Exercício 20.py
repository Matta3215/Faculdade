n = int(input("\nDigite o tamanho da sua lista: "))
lista = []

for i in range(n):
    b = input("Digite um valor 'true' ou 'false': ").lower()
    while b not in ['true', 'false']:
        b = input("Valor inválido. Digite 'true' ou 'false': ").lower()
    lista.append(b == 'true')

if any(lista):
    print("A lista possui pelo menos um valor verdadeiro\n")
else:
    print("A lista não possui nenhum valor verdadeiro\n")