area = float(input("Digite a área a ser pintada (em metros quadrados): "))
print()

litros = area / 6

latas = litros / 18

preco = int(latas * 80)

rlatas = litros % 18

galao = litros / 3.6

precog = galao * 25

rgalao = litros % 3.6

print(f"Quantidade de latas: {latas:.3f}\n")

print(f"Resto das latas: {rlatas:.3f}\n")

print(f"Quantidade de latas: {galao:.3f}\n")

print(f"Resto do galão: {rgalao:.3f}\n")

print(f"A valor total em latas será de R${preco:.3f}\n")

print(f"A valor total em galões será de R${precog:.3f}\n")
