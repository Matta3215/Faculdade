largura = 0
comprimento = 0

while (largura != 99 or comprimento != 99):
    largura = int(input("Digite a largura do retângulo(em metros): "))
    if(largura == 99):
        break

    comprimento = int(input("Digite a comprimento do retângulo(em metros): "))
    if (comprimento == 99):
        break

    area = largura * comprimento
    
    print(f"A largura é igual a {largura}")

    print(f"A comprimento é igual a {comprimento}")
    
    print(f"A área é igual a {area}")