import java.util.HashSet;
import java.util.Set;

public class Livro{

private String titulo;
private int anoPubli;
Autor autor
Set<Livro> autores;
Editora editora;

public Livro(String titulo, int anoPubli, Editora editora){
    this.titulo = titulo;
    this.anoPubli = anoPubli;
    this.autores = new HashSet<>();
    this.editora = editora;
} 

public void adicionarAutor(Autor autor){
    boolean retorno = autores.add(autor);
    
    if (retorno == true){
        System.out.println("Autor adicionado");
    }else{
        System.out.println("Autor já adiocionado");
    }
}

public void imprimir(){
    if (this.autores.isEmpty()){
        System.out.println("Não há autores");
    }else{
        System.out.println("Livro: " + this.titulo + ", Ano de publicação: " + this.anoPubli ", Editora: " + this.editora);
        for (autores temp : autores){
            System.out.println("Autores: " + autores);
        }
    }
}

public String getTitulo(){
    return titulo;
}

public void setTitulo(String titulo){
    this.titulo = titulo;
}

public String getanoPubli(){
    return anoPubli;
}

public void setanoPubli(String anoPubli){
    this.anoPubli = anoPubli;
}
}