public class Caixa extends Funcionario implements Vendas{
    Sorvete sorvete;
    private double comissao;
    private static int qntvendas = 0;
    
    public Caixa(String nome, String cpf, double salario){
        super(nome, cpf, salario);
    }
    
    @Override
    public void calcTaxa(){
        salario *= 0.95;
    }
    
    @Override
    public void bonus(){
        salario += comissao;
    }
    
    @Override
    public String toString(){
        return "Funcionario{Nome: " +nome+ ", CPF: " +cpf+ ", Salário: " +salario+ '}';
    }
    
    public void vender(){
        if (sorvete != null) {
            comissao = sorvete.getPreco() * 0.05;
            qntvendas += 1;
        } else {
            System.out.println("Nenhum sorvete selecionado para venda.");
        }
    }
    
    public void negociar(){
        System.out.println("Negociação feita com o cliente");
    }
    
    public int getQntVendas(){
        return qntvendas;
    }
    
    public void setSorvete(Sorvete s){
        this.sorvete = s;
    }
}
