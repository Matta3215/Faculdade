import numpy as np

def multiplicacao_matrizes(matriz1, matriz2):
    """Realiza a multiplicação elemento a elemento e retorna a somatória do resultado."""
    resultado = np.multiply(matriz1, matriz2)
    print(resultado)
    return np.sum(resultado)

def soma_matrizes(matriz1, matriz2):
    """Soma duas matrizes e retorna a somatória do resultado."""
    resultado = np.add(matriz1, matriz2)
    print(resultado)
    return np.sum(resultado)

def sub_matrizes(matriz1, matriz2):
    """Subtrai matriz1 de matriz2 e retorna a somatória do resultado."""
    resultado = np.subtract(matriz1, matriz2)
    print(resultado)
    return np.sum(resultado)

# Definindo o tamanho das matrizes
linha, coluna = 3, 3

# Gerando as matrizes aleatórias
matriz1 = np.random.randint(0, 11, (linha, coluna))
matriz2 = np.random.randint(0, 11, (linha, coluna))

# Exibindo as matrizes
print(f"\nPrimeira matriz:\n{matriz1}\n")
print(f"\nSegunda matriz:\n{matriz2}\n")

# Realizando as operações e exibindo os resultados como valores somados
print(f"Soma total das matrizes: {soma_matrizes(matriz1, matriz2)}\n")
print(f"Multiplicação total das matrizes: {multiplicacao_matrizes(matriz1, matriz2)}\n")
print(f"Subtração total das matrizes: {sub_matrizes(matriz1, matriz2)}\n")
