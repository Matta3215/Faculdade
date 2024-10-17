def contar_vogais(texto):
    vogal = 0

    for letra in texto.lower():
        print(letra)
        
        if (letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
            vogal += 1
    
    print(f"{vogal}")
    
texto = input("Digite uma palavra: ")

contar_vogais(texto)