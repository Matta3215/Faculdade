n = 0

while n >= 0:
    n = int(input("Digite um número inteiro: "))
    if(n < 0):
        break

    elif (n % 2 == 0):
        print(f"Par\n")

    elif (n % 2 != 0):
        print(f"Ímpar\n")
print()