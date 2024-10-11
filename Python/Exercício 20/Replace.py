texto = "***Olá, mundo!***"
texto_limpo = texto.replace("*", " ").replace("!", "").replace(",", " ")
print(texto_limpo)  # Saída: "Olá mundo"