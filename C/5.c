#include <stdio.h>
#include <math.h>

int main()
{
    int x;
    printf("Digite um  número: ");
    scanf("%d", &x);
    
    printf("\nAntecessor: %d\nSucessor: %d", x-1, x+1);
    return 0;
}