n = int(input("Digite a quantidade de números que deseja colocar: "))

lista = []
soma = 0

for x in range(n):
    num = int(input("Digite um número: "))
    soma = soma + num
    
lista.append(soma)
print(f"{lista}")
