num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite outro número: "))

if (num1 > num2 and num1 > num3):
    if(num2 > num3):
        print(f"{num1}\n{num2}\n{num3}")
    elif(num3 > num2):
        print(f"{num1}\n{num3}\n{num2}")

elif (num2 > num1 and num2 > num3):
    if(num1 > num3):
        print(f"{num2}\n{num1}\n{num3}")
    elif(num3 > num1):
        print(f"{num2}\n{num3}\n{num1}")

elif (num3 > num1 and num3 > num2):
    if(num2 > num1):
        print(f"{num3}\n{num2}\n{num1}")
    elif(num1 > num2):
        print(f"{num3}\n{num1}\n{num2}")