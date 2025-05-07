public class Contato{

private String tipo;
private String contato;

public Contato(String tipo, String contato){
    this.tipo = tipo;
    this.contato = contato;
} 

public String getTipo(){
    return tipo;
}

public void setTipo(String tipo){
    this.tipo = tipo
}

public String getContato(){
    return contato;
}

public void setContato(String contato){
    this.contato = contato;
}

@Override
public String toString(){
    return "Contato{Tipo: " + tipo + " Número: " + contato + '}'
}

}