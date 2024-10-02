nmax = int(input("Digite a capacidade máxima do restaurante: "))
print()

nclientes = 0

while (nclientes < nmax):
    clientes = int(input("Digite o número de clientes que acabaram de entrar: "))
    
    nclientes = nclientes + clientes

print("Atingiu a capacidade máxima")