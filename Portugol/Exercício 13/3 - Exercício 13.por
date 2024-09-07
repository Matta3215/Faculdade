programa
{
  inclua biblioteca Texto --> txt
  funcao inicio()
  {
    cadeia nome, caixaalta
    
    faca
    {
      escreva("\ndigite um nome qualquer ou digite fim para acabar: ")
      leia(nome)

      se(nome != "fim")
      {
        caixaalta = txt.caixa_alta(nome)
        escreva(" ", caixaalta, "\n") 
      }
    }
    enquanto(nome != "fim")
  }
}
