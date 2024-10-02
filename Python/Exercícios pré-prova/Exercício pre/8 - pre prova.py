pal = 47
n = int(input("Insira seu palpite: "))
print()

if (n < pal):
    print(f"Maior\n")
elif (n > pal):
    print(f"Menor\n")

while n != pal:
    n = int(input("Insira novamente seu palpite seu palpite: "))
    if (n < pal):
        print(f"Maior\n")
    elif (n > pal):
        print(f"Menor\n")

print(f"Você descobriu o número secreto 47\n")
