public class Main
{
	public static void main(String[] args){
	    
	    Loja l1 = new Loja();
	    
	    Produto p1 = new Produto("001", "Bola", "Nike", 49.99);
	    Produto p2 = new Produto("002", "Tênis", "Nike", 149.99);
	    
	    l1.adicionarProduto ("0001", p1);
	    l1.adicionarProduto ("0002", p2);
	    
	    l1.imprimirMap();
	    
		l1.adicionarCategoria()
	}
}