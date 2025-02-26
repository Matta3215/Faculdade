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
        
        int verificador = 1;
        while (verificador == 1){
            System.out.printf("\nSaque[1]\nDepósito[2]\n"); 
            int opcao = scan.nextInt();
        
            if (opcao == 1){
                System.out.println("\n===================================");
                System.out.println("\n               SAQUE");
                System.out.println("\n===================================");
                System.out.printf("\nDigite quantos reais deseja sacar: "); ct1.valor = scan.nextFloat();
                ct1.Sacar(ct1.valor);
                
                ct1.Info_Dados();
                verificador = 0;
            }
            else if (opcao == 2){
                System.out.println("\n===================================");
                System.out.println("\n               DEPÓSITO");
                System.out.println("\n===================================");
                System.out.printf("\nDigite quantos reais deseja depositar: "); ct1.valor = scan.nextFloat();
                ct1.Deposito(ct1.valor);
                
                ct1.Info_Dados();
                verificador = 0;
            }
            else{
                System.out.printf("\nValor inválido");
            }
        }
	}
}