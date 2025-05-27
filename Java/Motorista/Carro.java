public class Carro {
    private String modelo;
    private Motor motor;
    private Motorista motorista;
    private int variacaoMotorista = 0;

    public Carro(String modelo, Motorista motorista, int potencia, String tipoCombustivel) {
        this.modelo = modelo;
        this.motorista = motorista;
        this.motor = new Motor(potencia, tipoCombustivel);
        this.variacaoMotorista++;
    }

    public void setMotorista(Motorista motorista) {
        this.motorista = motorista;
        this.variacaoMotorista++;
    }

    @Override
    public String toString() {
        return "Carro{" + "modelo=" + modelo + 
                ", motor=" + motor.toString() + ", motorista=" + motorista.toString() + ", variacaoMotorista=" + variacaoMotorista + '}';
    }
    
    
    
    
    
}
