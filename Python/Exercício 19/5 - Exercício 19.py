i = 0

for x in range(0, 10):
    n = int(input("Digite um número inteiro: "))
    if(n > 10 and n < 50):
        i += 1
print(f"Houveram {i} números entre 10 e 50")
print()