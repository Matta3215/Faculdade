sal = float(input("Digite seu salário bruto: "))
print()

ir = sal * 0.11

inss = sal * 0.08

sind = sal * 0.05

salb = sal - sind - inss - ir

print(f"Seu salário bruto é {sal}\n")

print(f"Você pagou R${inss} ao inss\n")

print(f"Você pagou R${sind} ao sindicato\n")

print(f"Seu salário líquido é de R${salb}\n")