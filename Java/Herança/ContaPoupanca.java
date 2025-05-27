public class ContaPoupanca extends Conta{
    
    public ContaPoupanca(double saldo) {
        super(saldo);
    }
    
    @Override
    public void Sacar(double valor){
        if(getSaldo()>=(valor+15)){
            setSaldo(getSaldo()-(valor+15));
        }else{
            System.out.println("Saldo insuficiente!");
        }
    }
    
    @Override
    public void AplicarRendimento(){
        super.setSaldo(getSaldo()*1.005);
    }
    
    @Override
    public String TipoConta(){
        return "Conta Poupança";
    }
}
