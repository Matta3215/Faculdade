#include <stdio.h>

int main()
{
    int x = 0; 
    int i = 0;
    while (i < 5){
        
        if (x % 3 == 0 && x != 0){
            printf("\n%d", x);
            i++;
        }else{
            printf("\nX");
        }
        x++;
    }
    return 0;
}