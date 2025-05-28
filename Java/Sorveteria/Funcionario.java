public abstract class Funcionario{
    protected String nome;
    protected String cpf;
    protected double salario;
    
    public Funcionario(String nome, String cpf, double salario) {
        this.nome = nome;
        this.cpf = cpf;
        this.salario = salario;
    }
    
    public abstract void calcTaxa();
    
    public abstract void bonus();
}