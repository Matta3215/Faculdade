def eh_primo(num):
    primo = 1
    div = 2
    
    if(num == 1):
        return False

    while(primo == 1 and num / 2 >= div):
        
        if(num % div == 0):
            return False
        
        div += 1
    
    if(primo == 1):

        return True

num = int(input("Digite um número inteiro: "))

print(f"{eh_primo(num)}")