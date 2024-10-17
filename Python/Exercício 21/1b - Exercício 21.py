def calcular_media(num):
    media = (sum(num))/len(num)
    return media

n = int(input("Digite a quantidade de notas que deseja colocar: "))
num = []

for i in range(n):
    notas = float(input("Digite uma nota: "))

    num.append(notas)

media = calcular_media(num)

print(media)

if (media >= 7):
    print(f"O aluno está aprovado")

elif(media < 7 and media >= 5):
    print(f"O aluno está em recuperação")

elif(media < 5):
    print(f"O aluno está reprovado")
