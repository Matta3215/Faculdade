#include <stdio.h>

int somar(int x, int y, int z){
    return x+y+z;
}

int main()
{
    int x,y,z;
    printf("Digite três números: ");
    scanf("%d %d %d", &x,&y,&z);
    
    printf("\nResultado da soma: %d", somar(x,y,z));

    return 0;
}