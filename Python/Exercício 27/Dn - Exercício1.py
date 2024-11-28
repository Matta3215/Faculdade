import numpy as np
linha = int(input("Digite o número de alunos: "))
coluna = int(input("Digite o número de disciplinas: "))
matriz = np.zeros((linha,coluna))

print(matriz)
for i in range(linha):
    print(f"Digite a nota do {i + 1}° aluno: ")
    for j in range(coluna):
        nota = float(input(f"na {j + 1}° matéria: "))
        matriz[i][j] = nota
print(matriz)

for i in range(linha):
    media = np.mean(matriz[i])
    menor = np.min(matriz[i])
    maxi = np.max(matriz[i])
    print(f"A média do {i + 1}° aluno é: {media}\n")
    print(f"A menor nota do {i + 1}° aluno é: {menor}\n")
    print(f"A maior nota do {i + 1}° aluno é: {maxi}\n")
mediaT = np.mean(matriz)
print(f"A média de todos alunos é: {mediaT}")