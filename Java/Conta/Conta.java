public class Conta {
    String nome;
    int numero;
    double valor;
    double limite;
    double saldo;
    
    
    void Info_Dados(){
        System.out.println("\n===================================");
        System.out.println("\n               CONTA");
        System.out.println("\n===================================");
        System.out.printf("Nome: %s", nome);
        System.out.printf("\nNúmero da Conta: %d", numero);
        System.out.printf("\nSeu saldo é:  R$ %.2f", saldo);
        System.out.printf("\nSeu limite é: R$ %.2f", limite);
        System.out.println("\n===================================");
    }
    
    void Sacar(double valor){
        if(valor > saldo){
            System.out.println("\nValor do saldo insuficiente.");
        }
        else if(valor > limite){
            System.out.println("\nValor do saque ultrapassa o limite.");
        }
        else{
            saldo -= valor;
        }
    }
    
    void Deposito(double valor){
        saldo += valor;
    }
}