area = float(input("Digite a área a ser pintada (em metros quadrados): "))

litros = area / 3

latas = litros / 18

preco = litros * 4.4

print(f"A quantidade de latas a serem utilizadas serão {latas}")

print(f"A valor total será de R${preco}")