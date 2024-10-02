for i in range(1, 1001):
    primo = 1
    d = 2
    
    if(i == 1):
        primo = 0

    while(primo == 1 and i / 2 >= d):
        
        if(i % d == 0):
            primo = 0
        
        d += 1
    
    if(primo == 1):

        print(f"{i} é primo")