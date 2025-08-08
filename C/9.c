#include <stdio.h>

int main()
{   
    float x, y, z;
    int modo;
    
    printf("Digite dois valores: ");
    scanf("%f %f", &x, &y);
    
    printf("Menu:\n[1]Soma\n[2]Subtração\n[3]Multiplicação\n[4]Divisão\n");
    scanf("%d", &modo);
    
    switch(modo){
        case 1:
        z = x+y;
        printf("\nResultado da soma: %.2f", z);
        break;
        
        case 2:
        if(x>=y){
        z = x-y;
        }else{
            z = y-x;
        }
        printf("\nResultado da subtração: %.2f", z);
        break;
        
        case 3:
        z = x*y;
        printf("\nResultado da multiplicação: %.2f", z);
        break;
        
        case 4:
        while (y == 0){
            printf("\nValor inválido para y");
            printf("\nDigite um novo valor para y: ");
            scanf("%f", &y);
        }
        z = x/y;
        
        printf("\nResultado da divisão: %2.f", z);
        break;
    }
    return 0;
}