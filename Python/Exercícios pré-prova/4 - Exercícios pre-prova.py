n = int(input("Digite um número inteiro positivo: "))
print()
fat = 1

for x in range (0, n):
        num = n - x
        fat = fat * num
print(f"{fat}")
print()