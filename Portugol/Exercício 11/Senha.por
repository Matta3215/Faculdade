programa {
  funcao inicio() 
  {
   cadeia senha

   enquanto(senha != "cascadebala")
   {
    escreva("\n\ndigite a senha: ")
    leia(senha)
    se(senha != "cascadebala")
    {
      escreva("\nsenha incorreta, digite novamente")
    }
   }
   escreva("\nsenha correta, acesso permitido")
   escreva("\n")
  }
}
