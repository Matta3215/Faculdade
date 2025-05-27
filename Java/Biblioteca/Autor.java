import java.util.ArrayList;
import java.util.List;

public class Autor{
    private String nome;
    private String abrev;
    private List<Contato> contatos = new ArrayList<>();
    
    public Autor(String nome, String abrev){
        this.nome = nome;
        this.abrev = abrev;
    }
    
    public void adicionarContato(String tipo, String numero){
        Contato contato = new Contato(tipo, numero);
        contatos.add(contato);
        System.out.println("Contato adicionado");
    }
    
    public void Imprimir(){
        System.out.println("Autor: " + nome);
        for(Contato temp: contatos){
            System.out.println(temp);
        }
    }
        
    public String getAbrev(){
        return abrev;
    }
    
    public void setAbrev(String abrev){
        this.abrev = abrev;
    }
    
    public String getNome(){
       return nome;
    }
    
    public void setNome(String nome){
        this.nome = nome;
    }
    
    public List<Contato> getContatos() {
        return contatos;
    }
    
    @Override
    public String toString(){
        return "Autor{Nome: " + nome + ", Abreviação: " + abrev + '}';
    }
}