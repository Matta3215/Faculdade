public class Bola{
    private String sabor;
    
    public Bola(String sabor){
        this.sabor = sabor;
    }
    
    @Override
    public String toString(){
        return "Bola de Sorvete{Sabor: " +sabor+ '}';
    }
}