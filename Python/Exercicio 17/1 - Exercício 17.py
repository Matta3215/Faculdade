turno = (input("Digite o turno em que você estuda(M, V ou N): "))

if(turno == "M"):
    print(f"Bom Dia!\n")
elif(turno == "V"):
    print(f"Boa Tarde!\n")
elif(turno == "N"):
    print(f"Boa Noite!\n")
else:
   print(f"Valor invalido!\n")