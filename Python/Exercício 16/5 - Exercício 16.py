preco1 = float(input("\nDigite o primeiro preço: "))

preco2 = float(input("Digite o segundo preço: "))

preco3 = float(input("Digite o terceiro preço: "))

if(preco1 < preco2 and preco1 < preco3):
    print(f"Você deve comprar o primeiro produto")
elif(preco2 < preco1 and preco2 < preco3):
    print(f"Você deve comprar o segundo produto")
elif(preco3 < preco1 and preco3 < preco2):
    print(f"Você deve comprar o terceiro produto")