n = int(input("Digite um número inteiro: "))

i = 0

while (n < 0):
        i += 1
        n = int(input("Digite um número inteiro: "))

print(f"Foram digitados {i} números negativos")
print()