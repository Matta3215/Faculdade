#include <stdio.h>

int main()
{
    int x;
    printf("Digite um número: ");
    scanf("%d",&x);
    
    if(x % 2 == 0){
        printf("%d é par", x);
    }else{
        printf("%d é ímpar", x);
    }
}