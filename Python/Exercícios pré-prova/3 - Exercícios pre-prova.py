a = int(input("Digite um número inteiro positivo: "))
b = int(input("Digite outro número inteiro positivo: "))
print()

if(b < a):
    b = int(input("Digite novamente outro número inteiro positivo(dessa vez maior que o primeiro digitado): "))
    print()

for x in range (a, b + 1):
    if(x % 2 == 0):
        print(f"{x}")
print()