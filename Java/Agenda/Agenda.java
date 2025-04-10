import java.util.Map;
import java.util.HashMap;


public class Agenda{
    Map <String, String> map = new HashMap <>();
    
    public void Imprimir(){
        for(String key: map.keySet()){
            System.out.printf("\nNome: %s\nNúmero: %s\n", key, map.get(key));
        }
    }
    
    public void Inserir(String nome, String numero){
        map.put(nome, numero);
    }
    
    public String BuscarNumero(String nome){
        return map.get(nome);
    }
    
    public void Remover(String nome){
        map.remove(nome);
    }
    
    public int Tamanho(){
        return map.size();
    }
}