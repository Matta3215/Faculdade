programa
{
  funcao inicio()
  {
    inteiro n
    inteiro v
    inteiro d = 2
    
    escreva("Digite um numero inteiro positivo: ")
    leia(n)

    v = primo(n, d)

    se(n == 1)
    {
      escreva("\n ", n, " não é primo")
    }
    senao se(v == 1)
    {
      escreva("\n ", n, " é primo")
    }
    senao
    {
      escreva("\n ", n, " não é primo")
    }
    escreva("\n")
  }

  funcao inteiro primo(inteiro n, inteiro d)
  {
    inteiro primo = 1
    enquanto(primo == 1 e n / 2 >= d) 
    {
      se(n % d == 0)
      {
        primo = 0
      }
        d = d + 1
    }
    retorne primo
  }
}