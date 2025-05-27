public class Motorista {
    private String nome;
    private String cnh;
    private static int quantidadeMotoristas =0;

    public Motorista(String nome, String cnh) {
        this.nome = nome;
        this.cnh = cnh;
        quantidadeMotoristas++;
    }

    public static int getQuantidadeMotoristas() {
        return quantidadeMotoristas;
    }

    
    @Override
    public String toString() {
        return "Motorista{" + "nome=" + nome + ", cnh=" + cnh + '}';
    }
    
    
}
