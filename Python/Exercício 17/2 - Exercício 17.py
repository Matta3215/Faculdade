sal = float(input("Digite o seu salário: "))

if(sal <= 280):
    sal *= 1.20
    print(f"{sal:.2f}")

elif(sal > 280 and sal <= 700):
    sal *= 1.15
    print(f"{sal:.2f}")

elif(sal > 700 and sal <= 1500):
    sal *= 1.10
    print(f"{sal:.2f}")

elif(sal > 1500 ):
    sal *= 1.05
    print(f"{sal:.2f}")