#include <stdio.h>

int main()
{
    int x, y;
    printf("Digite dois números: ");
    scanf("%d %d", &x,&y);
    
    if(x > y){
        printf("%d é maior que %d e sua diferença é de %d", x, y, x-y);
    }
    else if(y > x){
        printf("%d é maior que %d e sua diferença é de %d", y, x, y-x);
    }else{
        printf("Os valores são iguais, sua diferença é 0");
    }
    return 0;
}