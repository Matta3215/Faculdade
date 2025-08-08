#include <stdio.h>

int main()
{
    int x;
    
    printf("Digite um número inteiro par: ");
    scanf("%d", &x);
    while (x % 2 != 0){
        printf("Valor inválido.\nDigite um número inteiro par: ");
        scanf("%d", &x);
    }
    while (x >= 0){
        if (x % 2 == 0){
            printf("\n%d", x);
            x--;
        }else{
            x--;
        }
    }
    return 0;
}