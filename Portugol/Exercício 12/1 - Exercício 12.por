programa 
{
  funcao inicio() 
  {
    cadeia formageo
    real l, c, r, a

    escreva("Digite o tipo de forma geom�trica deseja calcular a �rea(R.: QUADRADO, CIRCULO ou RETANGULO): ")
    leia(formageo)

    se(formageo == "QUADRADO")
    {
      escreva("\nDigite o lado do quadrado(em metros): ")
      leia(l)

      a = l * l
      escreva("A �rea do quadrado � igual a: ", a, " m")
      escreva("\n")
    }
    senao se(formageo == "RETANGULO")
    {
      escreva("\nDigite o comprimento(em metros): ")
      leia(c)
      escreva("\nDigite a largura(em metros): ")
      leia(l)

      a = l * c
      escreva("\nA �rea do ret�ngulo � igual a: ", a, " m")
      escreva("\n")
    }
    senao se(formageo == "CIRCULO")
    {
      escreva("\nDigite o raio do c�rculo(em metros): ")
      leia(r)

      a =  3.14 * (r * r)
      escreva("\nA �rea do c�rculo � igual a: ", a, " m")
      escreva("\n")
    }
    senao 
    escreva("figura geom�trica n�o consta na lista")
  }
}
