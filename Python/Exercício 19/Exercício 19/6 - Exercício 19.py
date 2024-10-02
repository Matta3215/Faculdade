mas = 0
fem = 0
sexh = 0
sexf = 0
idadegrupo = 0

for i in range(0, 10):
    sex = input("Digite seu gênero: ")
    
    idade = int(input("Digite sua idade: "))

    idadegrupo = idadegrupo + idade

    if(sex == "masculino"):
        mas = mas + idade
        sexh += 1

    elif(sex == "feminino"):
        fem = fem + idade
        sexf += 1
    print(i)

mediah = mas / sexh

mediaf = fem / sexf

mediag = idadegrupo / 10

print(f"A média de idade do gênero masculino é {mediah}\n")

print(f"A média de idade do gênero feminino é {mediaf}\n")

print(f"A média de idade do grupo é {mediag}\n")