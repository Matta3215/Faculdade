programa
{
  inclua biblioteca Matematica --> mat
  
  funcao inicio()
  {
    inteiro i, n, n1
    real n2, q, rq, n3, c, rc

    escreva("\nDigite a quantidade de n�meros que deseja imprimir: ")
    leia(n)

    se(n % 2 == 0)
    {
      n2 = n / 2
      para(i = 0; i < n2; i++)
      {
        escreva("\nDigite o n�mero que deseja fazer a raiz quadrada: ")
        leia(q)

        rq = mat.raiz(q, 2.0)

        escreva("A raiz quadrada de ", q," � igual a ", rq,"\n")
      }
    }
    senao se(n % 2 != 0)
    {
      n3 = n * 2
      para(i = 0; i < n3; i++)
      {
        escreva("\nDigite o n�mero que deseja fazer a raiz c�bica: ")
        leia(c)

        rc = mat.raiz(c, 3.0)

        escreva("A raiz c�bica de ", c," � igual a ", rc,"\n")
      }
    }
  }
}