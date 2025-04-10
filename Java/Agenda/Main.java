
public class Main
{
	public static void main(String[] args) {
		Agenda ag = new Agenda();
		
		ag.Inserir("Arthur", "(27) 99313-2828");
		ag.Inserir("Isabela", "(27) 99131-8282");
		
		System.out.printf("\nNúmero: %s\n", ag.BuscarNumero("Arthur"));
		System.out.printf("\nTamanho: %d\n", ag.Tamanho());
		
		ag.Imprimir();
	}
}