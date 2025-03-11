public class Conta {
    int numero;
    double limite;
    double saldo;
    Cliente titular;
    
    void Info_Dados(){
        System.out.println("\n===================================");
        System.out.println("               CONTA");
        System.out.println("===================================");
        System.out.printf("Nome: %s", titular.nome);
        System.out.printf("\nSobrenome: %s", titular.sobrenome);
        System.out.printf("\nCPF: %s", titular.cpf);
        System.out.printf("\nNúmero da Conta: %d", numero);
        System.out.printf("\nSeu saldo é:  R$ %.2f", saldo);
        System.out.printf("\nSeu limite é: R$ %.2f", limite);
        System.out.println("\n===================================");
    }
    
    void Sacar(double saque){
        if(saque > limite){
            System.out.println("Valor do saque ultrapassa o limite.");
        }
        else if(saque > saldo){
            System.out.println("Valor do saldo insuficiente.");
        }
        else{
            saldo -= saque;
            System.out.println("Saque realizado com sucesso!");
        }
    }
    
    void Deposito(double deposito){
        saldo += deposito;
    }
}
