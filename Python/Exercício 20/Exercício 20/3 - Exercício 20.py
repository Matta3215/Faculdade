n = int(input("Digite a quantidade de inputs que deseja fazer: "))

for x in range(n):
    i = input("Digite um input: ")

    try:
        i_int = int(i)
        print(f"'{i}' é número inteiro")
    except ValueError:
        try:
            i_float = float(i)
            print(f"'{i}' é um número real")
        except ValueError:
            print(f"'{i}' é uma string")
