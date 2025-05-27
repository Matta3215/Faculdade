public class Produto{
    private String id;
    private String nome; 
    private String marca;
    private double preco;
    
    public Produto(String id, String nome, String marca, double preco){
        this.id = id;
        this.nome = nome;
        this.marca = marca;
        this.preco = preco;
    }
    
 
 @Override
 public String toString(){
     return "Produto{Id do produto: " +id+ ", Nome: " +nome+ ", Marca: " +marca+ ", Preço: " +preco+ '}';
 }
}