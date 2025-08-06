#include <stdio.h>

int main()
{
    int x, y;
    printf("Digite dois números: ");
    scanf("%d %d", &x,&y);
    
    if(x > y){
        printf("%d é maior que %d", x, y);
    }
    else if(y > x){
        printf("%d é maior que %d", y, x);
    }else{
        printf("Os valores são iguais");
    }
    return 0;
}