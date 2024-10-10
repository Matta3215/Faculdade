n = int(input("Digite o tamanho da sua lista: "))

lista = []

for x in range(n):
    b = input("Digite um valor 'true' ou 'false': ").strip().lower()
    if b == 'true':
        lista.append(True)
    elif b == 'false':
        lista.append(False)
    else:
        print("Valor inválido, por favor digite 'true' ou 'false'.")
        x -= 1  

if all(lista):
    print("A lista é verdadeira")
else:
    print("A lista é falsa")