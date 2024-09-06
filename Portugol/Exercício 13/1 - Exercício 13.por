programa
{
  inclua biblioteca Matematica --> mat
  funcao inicio()
  {
    inteiro i, n

    escreva("Digite a quantidade de números que deseja imprimir: ")
    leia(n)

    para(i = 0; i < n; i++)
    {
      real num
      escreva("\nDigite o número que deseja arredondar: ")
      leia(num)

      num = mat.arredondar(num,1)

      escreva("Esse número arredondado é igual a: ", num, "\n")
    }
  }
}
