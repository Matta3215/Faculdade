i = 0

while (i != 1000):
    i = int(input("Digite um número inteiro: "))
    primo = 1
    d = 2
    
    if(i == 1000):
        print()
        break
    
    if(i == 1):
        primo = 0

    while(primo == 1 and i / 2 >= d):
        
        if(i % d == 0):
            primo = 0
        
        d += 1
    
    if(primo == 1):
        print(f"{i} é primo\n")
    
    else:
        print(f"{i} não é primo\n")