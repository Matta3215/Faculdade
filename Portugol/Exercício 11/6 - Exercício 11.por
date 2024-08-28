programa 
{
  funcao inicio() 
  {
    inteiro c
    
    para(c = 30; c >= 1; c--)
    {   
      se(c % 4 == 0)
      {
        escreva(" [", c, "]")
      }
      senao
      {
        escreva(" ", c)
      }
    }
    escreva("\nAcabou!")
  }
}
