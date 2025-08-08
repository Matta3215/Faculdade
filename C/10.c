#include <stdio.h>

int main()
{
    int idade, tempo;
    printf("\nDigite sua idade e tempo de trabalho em anos: ");
    scanf("%d %d", &idade, &tempo);
    
    if (idade >= 65 || tempo >= 30 || idade >= 60 && tempo >= 25){
        printf("Você pode se aposentar.");
    }else{
        printf("Você não pode se aposentar ainda.");
    }
    return 0;
}