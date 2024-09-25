kg = int(input(f"Digite a quantidade de peixes(em kg): "))

if(kg > 50):
    taxa = kg - 50
    taxa *= 4
    print(f"O valor da multa a ser paga é igual a {taxa}\n")

else:
    print(f"Sem multa a pagar\n")