public class Main
{
	public static void main(String[] args) {
		Sorvete s1 = new Sorvete();

		s1.adicionarBola("Morango");
		s1.adicionarBola("Flocos");
		s1.adicionarBola("Chocolate");
		s1.adicionarBola("Nutella");
		s1.adicionarBola("Doce de Leite");
		s1.adicionarBola("Creme");

		s1.imprimir();
		s1.calcPreco();

		Caixa c1 = new Caixa("Ricardo", "000.000.000-01", 1450);
		
		System.out.println(c1.toString());
		
		c1.calcTaxa();
		
		c1.setSorvete(s1);
        c1.vender();
        c1.negociar();
        c1.bonus();
        
        System.out.println(c1.toString());
	}
}