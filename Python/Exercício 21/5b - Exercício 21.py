def contar_vogais(texto):
    contagem = 0
    vogais = "aeiou"

    for letra in texto.lower():     
        if letra in vogais:
            contagem += 1
    
    print(f"Essa palavra possui {contagem} vogais")
    
texto = input("Digite uma palavra: ")

contar_vogais(texto)