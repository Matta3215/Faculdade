def calcular_media(n1, n2, n3):
    media = (n1 + n2 + n3)/3
    return media


n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
n3 = int(input("Digite a terceira nota: "))

media = calcular_media(n1, n2, n3)

if (media >= 7):
    print(f"O aluno está aprovado")

elif(media >= 5 and media < 7):
    print(f"O aluno está em recuperação")

elif(media < 5):
    print(f"O aluno está reprovado")
