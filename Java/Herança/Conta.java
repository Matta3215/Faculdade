public abstract class Conta {
    private double saldo;

    public Conta(double saldo) {
        this.saldo = saldo;
    }

    public void Depositar(double valor){
        this.saldo+=valor;
    }
    
    public abstract void Sacar(double valor);
    
    public abstract void AplicarRendimento();
    
    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }
    
    public String TipoConta(){
        return "Conta Simples";
    }
    
    
    
}
