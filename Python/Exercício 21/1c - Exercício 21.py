def calcular_media(num):
    media = (sum(num))/len(num)
    return media

n = int(input("Digite a quantidade de notas que deseja colocar: "))
num = []

for i in range(n):
    notas = float(input("Digite uma nota: "))
    num.append(notas)

calcular_media(num)

if (calcular_media(num) >= 7):
    print(f"O aluno está aprovado")

elif(calcular_media(num) < 7 and calcular_media(num) >= 5):
    print(f"O aluno está em recuperação")

elif(calcular_media(num) < 5):
    print(f"O aluno está reprovado")
