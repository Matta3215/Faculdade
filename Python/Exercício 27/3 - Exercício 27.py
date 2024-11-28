import numpy as np

# Criando uma matriz 7xN (7 dias e N bairros)
dias = 7
bairros = int(input("\nQuantos bairros? "))
matriz_consumo = np.random.randint(0, 21, size=(dias, bairros))

print(f"\nMatriz:\n{matriz_consumo}\n")

def consumo_medio(matriz):
    return np.mean(matriz, axis=0)
 
def dia_maior_consumo(matriz):
    return np.argmax(np.sum(matriz, axis=1)) + 1  
def bairro_maior_consumo(matriz):
    return np.argmax(np.sum(matriz, axis=0)) + 1 
def bairro_menor_consumo(matriz):
    return np.argmin(np.sum(matriz, axis=0)) + 1 


print(f"Consumo médio semanal por bairro: {consumo_medio(matriz_consumo).round(2)}\n")
print(f"Dia de maior consumo: {dia_maior_consumo(matriz_consumo)}\n")
print(f"Bairro com maior consumo: {bairro_maior_consumo(matriz_consumo)}\n")
print(f"Bairro com menor consumo: {bairro_menor_consumo(matriz_consumo)}\n")
