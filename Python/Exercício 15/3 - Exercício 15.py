num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

op = (input("Digite uma operação para fazer(adição, subtração, multiplicação ou divisão): "))

if(op == "adição"):
    ad = num1 + num2
    print("A soma é igual a", ad)

if(op == "subtração"):
    sub = num1 - num2
    print("A subtração é igual a", sub)

if(op == "multiplicação"):
    mul = num1 * num2
    print("A multiplicação é igual a", mul)

if(op == "divisão"):
    div = num1 / num2
    print("A divisão é igual a", div)
