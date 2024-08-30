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

      a = calcularAreaQuadrado(l)
      escreva("A área do quadrado é igual a: ", a, " m")
      escreva("\n")
    }
    senao se(formageo == "RETANGULO")
    {
      escreva("\nDigite o comprimento(em metros): ")
      leia(c)
      escreva("\nDigite a largura(em metros): ")
      leia(l)

      a = calcularAreaRetangulo(c, l)
      escreva("\nA área do retângulo é igual a: ", a, " m")
      escreva("\n")
    }
    senao se(formageo == "CIRCULO")
    {
      escreva("\nDigite o raio do círculo(em metros): ")
      leia(r)

      a =  calcularAreaCirculo(r)
      escreva("\nA área do círculo é igual a: ", a, " m")
      escreva("\n")
    }
    senao 
    escreva("figura geométrica não consta na lista")
  }
  funcao real calcularAreaQuadrado(real l)
  {
    real calcularAreaQuadrado = l * l
    retorne calcularAreaQuadrado
  }  
  funcao real calcularAreaRetangulo(real c, real l)
  {
    real calcularAreaRetangulo = c * l
    retorne calcularAreaRetangulo
  }  
  funcao real calcularAreaCirculo(real r)
  {
    real calcularAreaCirculo = 3.14 * (r * r)
    retorne calcularAreaCirculo
  }
}
