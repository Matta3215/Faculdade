public class Motorista{
    private String nome;
    private String cnh;
    private static int quantidade_motoristas = 0;
    private static int quantidade_carro_uso = 0;
    Carro car;
    
    public void Motorista(String nome, String cnh){
        this.nome = nome;
        this.cnh = cnh;
        quantidade_motoristas++;
    }
    
    public void ImprimirMotorista(){
        System.out.printf("\n======================================");
        System.out.printf("\nNome: %s", this.nome.toUpperCase());
        System.out.printf("\nCNH: %s", this.cnh);
        System.out.printf("\n======================================");
    }
    
    public String getNome(){
        return nome.toUpperCase();
    }
    
    public String getCNH(){
        return cnh;
    }
    
    public void setNome(String nome){
        this.nome = nome;
    }
    
    public void setCNH(String cnh){
        this.cnh = cnh;
    }

    
    public void Dirigir(){
        if (car.nullModelo() == true){
            System.out.println("Indivíuo não possui carro.");
        }
        else{
            System.out.printf("%s dirigiu com %s.", this.nome, car.getModelo());
            quantidade_carro_uso++;
        }
    }
}
