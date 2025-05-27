public class Main {

    public static void main(String[] args) {
        System.out.println("EXEMPLO");
        
        Cliente c1 = new Cliente("Cassio", "00000000000");
        
        c1.CriarConta(200, 1);
        c1.CriarConta(300, 1);
        c1.CriarConta(500, 2); 
        
        c1.mostrarSaldo();
        
        c1.getContas().get(0).Sacar(50);
        c1.getContas().get(1).Sacar(50);
        c1.getContas().get(2).Sacar(50);
        c1.mostrarSaldo();
        
        for(Conta c: c1.getContas()){
            c.AplicarRendimento();
        }
        
        c1.mostrarSaldo();
    }
}




