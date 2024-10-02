n = int(input("Digite um número inteiro positivo: "))
print()


for i in range (1, n + 1):
        esp = " " * (n - i)
        ast = "*" * (2 * i - 1)

        print(f"{esp + ast}")
print()