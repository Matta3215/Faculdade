num = []
x = 0
while x < 5:
    n = int(input("Digite um número: "))
    num.append(n)
    x += 1

if num == sorted(num):
    print(f"True")
else:
    print(f"False")