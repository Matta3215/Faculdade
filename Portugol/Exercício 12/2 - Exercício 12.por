programa
{
  funcao inicio()
  {
    inteiro n
    inteiro d = 2
    inteiro primo = 1

    escreva("Digite um numero inteiro positivo: ")
    leia(n)
    escreva("Inteiro dado = ", n)

    enquanto(primo == 1 e n / 2 >= d) 
    {
      se(n % d == 0)
      {
        primo = 0
      }
        d = d + 1
    }
    se(n == 1)
    {
      escreva("\n ", n, " n�o � primo")
    }
    senao se(primo == 1)
    {
      escreva("\n ", n, " � primo")
    }
    senao
      escreva("\n ", n, " n�o � primo")
  }
}