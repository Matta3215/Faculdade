programa 
{
  funcao inicio() 
  {
    inteiro i = 6
    inteiro c

    para(c = 6; c <= 100; c = c + 2)
    {
      se(c != 100)
      {
      escreva(" ", c," +")
      }
      se(c == 100)
      {
        escreva(" ", c)
      }
      i = i + c
    }
    escreva("\nSoma total: ", i)

    escreva("\nAcabou!")
  }
}
