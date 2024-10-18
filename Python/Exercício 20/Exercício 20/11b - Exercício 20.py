n = int(input("\nDigite o tamanho da sua lista: "))
lista = []

for i in range(n):
    b = input("Digite um valor 'true' ou 'false': ").lower()
    if b == 'true':
        lista.append(1)
    elif b == 'false':
        lista.append(0)
    else:
        print("Valor inválido, por favor digite 'true' ou 'false'.")
        i -= 1  

if(bool(max(lista)) == True):
    print("A lista possui pelo menos um valor verdadeiro\n")
else:
    print("A lista não possui nenhum valor verdadeiro\n")