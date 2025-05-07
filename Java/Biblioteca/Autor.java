import java.util.HashSet;
import java.util.Set;

public class Autor{

private String nome;
private String abrev;
Set<Autor> contatoAutor;

public Autor(String nome, String abrev){
    this.nome = nome;
    this.abrev = abrev;
    this.autor = new HashSet<>();
} 

public void adicionarContato(String tipo, String contato){
    Contato c = new Contato(tipo, contato);
    boolean retorno = contatoAutor.add(c);
    
    if (retorno == true){
        System.out.println("Contato adicionado");
    }else{
        System.out.println("Contato já adiocionado");
    }
}

public void imprimir(){
    if (this.contatoAutor.isEmpty()){
        System.out.println("Não há contatos para esse autor");
    }else{
        System.out.println("Autor: " + this.nome + ", Abreviação: " + this.abrev);
        for (contatoAutor temp : contatoAutor){
            System.out.println("Contatos: " + temp);
        }
    }
}

public String getNome(){
    return nome;
}

public void setNome(String nome){
    this.nome = nome;
}

public String getAbrev(){
    return abrev;
}

public void setAbrev(String abrev){
    this.abrev = abrev;
}

@Override
    public String toString() {
        return "Autor{Nome: " + nome + ", Abreviação: " + abrev + '}';
    }
}