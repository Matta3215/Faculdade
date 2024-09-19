num1 = int(input("\nDigite um número: "))

num2 = int(input("Digite outro número: "))

num3 = int(input("Digite outro número: "))

if(num1 == num2 == num3):
    print(f"Iguais")
elif(num1 > num2 and num1 > num3):
    print(f"{num1} é maior que os demais")
elif(num2 > num1 and num2 > num3):
    print(f"{num2} é maior que os demais")
elif(num3 > num1 and num3 > num2):
    print(f"{num3} é maior que os demais")

if(num1 < num2 and num1 < num3):
    print(f"{num1} é menor que os demais")
elif(num2 < num1 and num2 < num3):
    print(f"{num2} é menor que os demais")
elif(num3 < num1 and num3 < num2):
    print(f"{num3} é menor que os demais")
    