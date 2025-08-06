#include <stdio.h>

int somar(int a, int b){
    return a + b;
}

int main()
{
    int a,b,c,d;
    
    printf("Digite o primeiro número: ");
    scanf("%d", &a);
    printf("Digite o segundo número: ");
    scanf("%d", &b);
    
    printf("Digite o terceiro e quarto número: ");
    scanf("%d %d", &c,&d);
    
    printf("\nPrimeiro resultado: %d", somar(a,b));
    printf("\nSegundo resultado: %d", somar(c,d));
    
    return 0;
}