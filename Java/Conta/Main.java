import java.util.Scanner;

public class Main
{
	public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        Cliente cli1, cli2;
		cli1 = new Cliente();
		cli2 = new Cliente();
		
		Conta ct1, ct2; 
        ct1 = new Conta();
        ct2 = new Conta();
        
        ct1.titular = cli1;
        ct2.titular = cli2;
        
        ct1.titular.nome = "Arthur";
        ct1.titular.sobrenome = "Agostini";
        ct1.titular.cpf = "555.724.276-08";
        ct1.numero = 1;
        ct1.saldo = 15000;
        ct1.limite = 1500;
        
        ct2.titular.nome = "Luiz Inácio";
        ct2.titular.sobrenome = "Lula";
        ct2.titular.cpf = "131.313.131-13";
        ct2.numero = 13;
        ct2.saldo = 13000;
        ct2.limite = 1300;
        
        ct2.Info_Dados();
        ct1.Info_Dados();
        
        cli1.Casar(cli2);
        
        System.out.println(c1.titular.conjuge.nome);
        
        int verificador1 = 1;
        while (verificador1 == 1){
            
            int verificador = 1;
            while (verificador == 1){
                System.out.println("===================================");
                System.out.printf("[1] Saque\n[2] Depósito\n"); 
                System.out.println("===================================");
                
                int opcao = scan.nextInt();
                if (opcao == 1){
                    System.out.println("\n===================================");
                    System.out.println("               SAQUE");
                    System.out.println("===================================");
                    System.out.printf("Digite quantos reais deseja sacar: "); double valor = scan.nextDouble();
                    ct1.Sacar(valor);
                    
                    verificador = 0;
                }
                else if (opcao == 2){
                    System.out.println("\n===================================");
                    System.out.println("               DEPÓSITO");
                    System.out.println("===================================");
                    System.out.printf("Digite quantos reais deseja depositar: "); double valor = scan.nextDouble();
                    ct1.Deposito(valor);
                    
                    verificador = 0;
                }
                else{
                    System.out.println("\nValor inválido");
                }
            }
        do{
            System.out.println("===================================");
            System.out.printf("Deseja fazer outra ação?\n[1] Sim\n[2] Não\n[3] Ver Menu\n");
            System.out.println("===================================");
            verificador1 = scan.nextInt();
            if (verificador1 == 2){
                System.out.println("\nPrograma Finalizado!");
            }
            else if (verificador1 == 3){
                ct1.Info_Dados();
            }
        }while (verificador1 < 1 || verificador1 > 2);
        
        }
	}
}