
public class Main
{
	public static void main(String[] args) {
	    Motorista mo;
	    mo = new Motorista();
	    
	    Carro ca;
	    ca = new Carro();
	    
	    mo.Motorista("Arthur", "12345");
	    //ca.Carro("Honda Civic");
	    mo.ImprimirMotorista();
	    ca.ImprimirCarro();
	    
	    System.out.println(mo.getNome());
	    //ca.Motorista_Carro("Honda Civic");
	    //mo.Dirigir();
	}
}