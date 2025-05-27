import java.util.ArrayList;
import java.util.List;

public class Livro{
    private String titulo;
    private int anoPubli;
    private List<Autor> autores = new ArrayList<>();
    Editora editora;
    
    public Livro(String titulo, int anoPubli, Editora editora){
        this.titulo = titulo;
        this.anoPubli = anoPubli;
        this.editora = editora;
    }
    
    public void adicionarAutor(Autor autor){
        autores.add(autor);
        System.out.println("Autor adicionado");
    }
    
    public void Imprimir(){
        System.out.println("Livro: " + titulo);
        System.out.println(editora.toString());
        for(Autor temp: autores){
            System.out.println(temp);
        }
    }
        
    public int getAnoPubli(){
        return anoPubli;
    }
    
    public void setAnoPubli(int anoPubli){
        this.anoPubli = anoPubli;
    }
    
    public String getTitulo(){
       return titulo;
    }
    
    public void setTitulo(String titulo){
        this.titulo = titulo;
    }
    
    public List<Autor> getAutores() {
        return autores;
    }
    
    @Override
    public String toString(){
        return "Livro{titulo: " + titulo + ", Ano de Publicação: " + anoPubli + '}';
    }
}