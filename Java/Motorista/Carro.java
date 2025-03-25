public class Carro{
    private String modelo;
    Motorista mot;
    
    public void Carro(String modelo){
        this.modelo = modelo;
    }
    
    public void ImprimirCarro(){
        System.out.printf("\n======================================");
        System.out.printf("\nModelo do Carro: %s", this.modelo);
        System.out.printf("\n======================================");
    }
    
    public String getModelo(){
        return modelo;
    }
    
    public void setModelo(String modelo){
        this.modelo = modelo;
    }
    
    public boolean nullModelo(){
        if (this.modelo == null){
            return true;
        }else{
            return false;
        }
    }
    
    public void Motorista_Carro(String modelo){
        if (this.modelo == null){
            this.modelo = modelo;
            System.out.printf("Motorista %s adquiriu um %s", mot.getNome(), modelo);
        }
        else{
            System.out.printf("Motorista %s trocou de %s para um %s", mot.getNome(), this.modelo, modelo);
            this.modelo = modelo;
        }
    }
}
