qnt = int(input("Digite a quantidade de números que deseja colocar na lista: "))

num = []

for x in range(0, qnt):
    n = int(input("Digite um número: "))
    num.append(n)

soma = sum(num)

print(f"A soma total é igual a {soma}")