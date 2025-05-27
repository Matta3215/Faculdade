import java.util.HashMap;
import java.util.Map;
import java.util.ArrayList;
import java.util.List;


public class Loja{
    private Map<String, Produto> produtos;
    private List<Produto> categorias;
    
    public Loja(){
        this.produtos = new HashMap<>();
    }
    
    public void adicionarProduto(String id_local, Produto produto){
        this.produtos.put(id_local, produto);
        System.out.println("Produto adicionado ao estoque.");
    }
    
    public Produto buscar(String id_local){
        return this.produtos.get(id_local);        
    }
    
    public void adicionarCategoria(Produto produto){
        categorias.add(produto);
        System.out.println("Produto adicionado a categoria.");
    }
    
    
    public void imprimirMap(){
        if(this.produtos.isEmpty()){
            System.out.println("Vazio.");
        }else{
            
        for(String id_local : produtos.keySet()){
            System.out.println("Id do local: "+id_local+ ", Nome: "+ produtos.get(id_local));
            }
        }
    }
}