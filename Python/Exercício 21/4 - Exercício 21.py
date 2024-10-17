def gerar_tabuada(num):
    for i in range(1, 11):
        tabuada = num * i
        print(f"{i} * {num} = {tabuada}")
    
num = int(input("Digite um número inteiro: "))

gerar_tabuada(num)