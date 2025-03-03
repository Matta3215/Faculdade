/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/
import java.util.Scanner;

public class Main
{
	public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
		Conta ct1, ct2; 
        ct1 = new Conta();
        ct2 = new Conta();
        
        ct1.nome = "Matta";
        ct1.numero = 1;
        ct1.saldo = 15000;
        ct1.limite = 1500;
        
        ct2.nome = "Luis";
        ct2.numero = 13;
        ct2.saldo = 13000;
        ct2.limite = 1300;
        
        ct2.Info_Dados();
        ct1.Info_Dados();
        
        int verificador1 = 1;
        while (verificador1 == 1){
            
            int verificador = 1;
            while (verificador == 1){
                System.out.println("===================================");
                System.out.printf("Saque[1]\nDepósito[2]\n"); 
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
            System.out.printf("Deseja fazer outra ação?\nSim[1]\nNão[2]\nVer Menu[3]\n");
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