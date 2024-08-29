programa 
{
  funcao inicio() 
  {
    cadeia formageo
    real l, c, r, a

    escreva("Digite o tipo de forma geométrica deseja calcular a área(R.: QUADRADO, CIRCULO ou RETANGULO): ")
    leia(formageo)

    se(formageo == "QUADRADO")
    {
      escreva("\nDigite o lado do quadrado(em metros): ")
      leia(l)

      a = l * l
      escreva("A área do quadrado é igual a: ", a, " m")
      escreva("\n")
    }
    senao se(formageo == "RETANGULO")
    {
      escreva("\nDigite o comprimento(em metros): ")
      leia(c)
      escreva("\nDigite a largura(em metros): ")
      leia(l)

      a = l * c
      escreva("\nA área do retângulo é igual a: ", a, " m")
      escreva("\n")
    }
    senao se(formageo == "CIRCULO")
    {
      escreva("\nDigite o raio do círculo(em metros): ")
      leia(r)

      a =  3.14 * (r * r)
      escreva("\nA área do círculo é igual a: ", a, " m")
      escreva("\n")
    }
    senao 
    escreva("figura geométrica não consta na lista")
  }
}
