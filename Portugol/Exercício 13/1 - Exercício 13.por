programa
{
  inclua biblioteca Matematica --> mat
  funcao inicio()
  {
    inteiro i, n

    escreva("Digite a quantidade de n�meros que deseja imprimir: ")
    leia(n)

    para(i = 0; i < n; i++)
    {
      real num
      escreva("\nDigite o n�mero que deseja arredondar: ")
      leia(num)

      num = mat.arredondar(num,1)

      escreva("Esse n�mero arredondado � igual a: ", num, "\n")
    }
  }
}
