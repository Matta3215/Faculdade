
public class Main
{
	public static void main(String[] args) {
		
		Editora e1 = new Editora("Tinindo", "tinindo.editora@gmail.com");
		Autor a1 = new Autor("Paçoca", "Pafocam");
		Autor a2 = new Autor("Gnomo da Liberdade", "Felinas");
		Livro l1 = new Livro("Bolo Molhadinho", 2024, e1);
		
		l1.adicionarAutor(a1);
		l1.adicionarAutor(a2);
		System.out.println();
		
	    a1.adicionarContato("Telefone", "(27)3208-7667");
		a1.adicionarContato("Celular", "(27)99222-3333");
		System.out.println();
		
		l1.Imprimir();
		System.out.println();
		
		a1.Imprimir();
	}
}