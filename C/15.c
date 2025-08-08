#include <stdio.h>

int main()
{
    int menor, menor_menor, maior, maior_maior, n_novo;
    int n = 0;
    int n_antigo = 0;
    
    do {
        printf("Digite um número inteiro: ");
        scanf("%d", &n);
        n_novo = n;
        if (n_novo > n_antigo){
            maior = n_novo;
            if (maior > maior_maior){
                maior_maior = maior;
            }
        }
        else if(n_novo <= n_antigo && n_novo > 0){
            menor = n_novo;
            if (menor < menor_menor){
                menor_menor = menor;
            }
        }
        n_antigo = n;
    } while (n >= 0);
    
    printf("\nMaior: %d", maior_maior);
    printf("\nMenor: %d", menor_menor);
}