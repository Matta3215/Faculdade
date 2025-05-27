import java.util.ArrayList;
import java.util.List;

public class Cliente {
    private String nome;
    private String cpf;
    private List<Conta> contas;
    
    public Cliente(String nome, String cpf) {
        this.nome = nome;
        this.cpf = cpf;
        contas = new ArrayList<>();
    }

    public void CriarConta(double saldoInicial, int tipo){
        Conta temporaria;
        
        if(tipo == 1){//conta corrente
            temporaria = new ContaCorrente(saldoInicial);
            contas.add(temporaria);
        }else if(tipo == 2){//conta poupanca
            temporaria = new ContaPoupanca(saldoInicial);
            contas.add(temporaria);
        }else{
            System.out.println("Opcao Invalida");
        }    
    }
    
    public void mostrarSaldo(){
        System.out.println("CONTAS:");
        for(Conta c : contas){
            System.out.println(c.TipoConta()+": "+c.getSaldo() );
        }
    }

    public List<Conta> getContas() {
        return contas;
    }
    
    
           
    
    
}
