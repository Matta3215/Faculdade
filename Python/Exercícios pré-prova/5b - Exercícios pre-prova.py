# Programa para desenhar uma pirâmide de asteriscos
n = int(input("Digite o número de linhas da pirâmide: "))
# Desenha a pirâmide
for i in range(1, n + 1):
    espacos = ' ' * (n - i)  # Define a quantidade de espaços à esquerda
    asteriscos = '*' * (2 * i - 1)  # Define a quantidade de asteriscos
    print(espacos + asteriscos)