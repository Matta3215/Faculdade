public class Main {

    public static void main(String[] args) {
        
        System.out.println("AGREGAÇÃO / COMPOSIÇÃO");
        
        Motorista m1 =  new Motorista("Cassio", "31351");
        Motorista m2 =  new Motorista("Pedro", "5424544");
        Motorista m3 =  new Motorista("João", "231321");
        
        System.out.println("Quantidade Motoristas: "+ Motorista.getQuantidadeMotoristas());
        
        Carro c1 = new Carro("gol", m1, 100, "eletrico");
        
        Carro c2 = new Carro("celta", m2, 100, "gasolina");
        
        System.out.println(c1);
        c1.setMotorista(m2);
        c1.setMotorista(m3);
        System.out.println(c1);
        System.out.println(c2);
        
        System.out.println(c1.toString());
    }
}