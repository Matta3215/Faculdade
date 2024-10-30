# Solicita ao usuário para inserir uma lista de elementos separados por vírgulas
entrada = input("Digite uma lista de palavras ou números, separados por vírgulas: ")

# Converte a entrada em uma lista, removendo espaços em branco extras
lista = [item.strip() for item in entrada.split(',')]

# Cria um dicionário para contar as ocorrências de cada elemento
contagem = {}

# Conta cada elemento na lista
for item in lista:
    if item in contagem:
        contagem[item] += 1
    else:
        contagem[item] = 1

# Exibe o resultado
print(contagem)