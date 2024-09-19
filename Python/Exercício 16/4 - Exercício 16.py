nota1 = float(input("\nDigite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if(media >= 7 and media < 10):
    print(f"Aprovado")
elif(media < 7):
    print(f"Reprovado")
elif(media == 10):
    print(f"Aprovado com Distinção")