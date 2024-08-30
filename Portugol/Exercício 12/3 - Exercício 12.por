programa
{
  inclua biblioteca Matematica --> mat
  funcao inicio()
  {
    real c, f, k, r

    escreva("\nDigite se deseja converter de Celsius para Fahrenheit, de Fahrenheit para Kelvin ou de Kelvin para Fahrenheit(responda, respectivamente, 1, 2 ou 3 para as conversões): ")
    leia(r)

    se(r == 1)
    {
      escreva("\nDigite a temperatura em Celcius: ")
      leia(c)

      f = celsiusparafahrenheit(c)

      f = mat.arredondar(f,2)

      escreva("\n ", c," °C esquivale a ", f, " °F")
    }
    senao se(r == 2)
    {
      escreva("\nDigite a temperatura em Fahrenheit: ")
      leia(f)

      k = fahrenheitparakelvin(f)

      k = mat.arredondar(k,2)

      escreva("\n ", f," °F esquivale a ", k, " K")
    }
    senao se(r == 3)
    {
      escreva("\nDigite a temperatura em Kelvin: ")
      leia(k)

      c = kelvinparacelsius(k)

      c = mat.arredondar(c,2)

      escreva("\n ", k," K esquivale a ", c, " °C")
    }
    escreva("\n")
  }


  funcao real celsiusparafahrenheit(real c)
  {
    real celsiusparafahrenheit = ((c * 9) / 5) + 32
    retorne celsiusparafahrenheit
  }
  funcao real fahrenheitparakelvin(real f)
  {
    real fahrenheitparakelvin = (f + 459.67) / 1.8
    retorne fahrenheitparakelvin
  }
  funcao real kelvinparacelsius (real k)
  {
    real kelvinparacelsius = (k - 273.15)
    retorne kelvinparacelsius
  }
}
