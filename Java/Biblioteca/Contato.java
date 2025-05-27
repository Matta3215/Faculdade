public class Contato{
    private String tipo;
    private String numero;
    
    public Contato(String tipo, String numero){
        this.tipo = tipo;
        this.numero = numero;
    }
    
    public String getNumero(){
        return numero;
    }
    
    public void setNumero(String numero){
        this.numero = numero;
    }
    
    public String getTipo(){
       return tipo;
    }
    
    public void setTipo(String tipo){
        this.tipo = tipo;
    }
    
    @Override
    public String toString(){
        return "Contato{Tipo: " + tipo + ", Número: " + numero + '}';
    }
}