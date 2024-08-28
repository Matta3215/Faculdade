programa 
{
  funcao inicio() 
  {
    inteiro x
    inteiro i
    inteiro c

    escreva("Digite o primeiro Valor: ")
    leia(c)
    escreva("Digite o último Valor: ")
    leia(i)
    escreva("Digite o incremento: ")
    leia(x)

    se(c < i)
    {
      para(c; c <= i; c = c + x)
      {   
        escreva(" ", c)
      }
    }
    senao se(c > i)
    {
      para(c; c >= i; c = c - x)
      {   
        escreva(" ", c)
      }
    }
    escreva("\nAcabou!")
  }
}
