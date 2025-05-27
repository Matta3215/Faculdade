public class Motor {
    private int potencia;
    private String tipoCompbustivel;

    public Motor(int potencia, String tipoCompbustivel) {
        this.potencia = potencia;
        this.tipoCompbustivel = tipoCompbustivel;
    }

    @Override
    public String toString() {
        return "Motor{" + "potencia=" + potencia + ", tipoCompbustivel=" + tipoCompbustivel + '}';
    }
    
}
