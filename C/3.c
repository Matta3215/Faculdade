#include <stdio.h>
#include <math.h>

int main()
{
    float x;
    printf("Digite um  número: ");
    scanf("%f", &x);
    
    printf("O quadrado de %.0f é %.0f",x, pow(x,2));
    return 0;
}
