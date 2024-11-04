vetor = []
for x in range(5):
    num = int(input("Digite um número: "))
    vetor.append(num)

n = int(input("Digite 0, 1 ou 2: "))

while n != 0 and n != 1 and n != 2:
    n = int(input("Digite 0, 1 ou 2: "))

if n == 0:
    print("\nPrograma finalizado\n")
    exit

if n == 1:
    print(f"\nVetor: {vetor}\n")

if n == 2:
    vetor.sort(reverse=True)
    print(f"\nVetor: {vetor}\n")