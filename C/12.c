#include <stdio.h>

int main()
{
    int i = 1;
    int ii = 1;
    for (int i = 1; i <= 100; i++ ){
        printf("\n%d", i);
    }
    while (i <= 100){
        printf("\n%d", i);
        i++;
    }
    do {
        printf("\n%d", ii);
        ii++;
    } while (ii <= 100);
    
    return 0;
}