num = []
x = 0
while x < 5:
    n = int(input("Digite um número: "))
    num.append(n)
    x += 1

if all(num[i] <= num[i + 1] for i in range(len(num) - 1)):
    print(f"True")

else:
    print(f"False")