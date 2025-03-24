import java.time.Year;
import java.util.Random;
import java.util.Scanner;

public class Aluno{
    private static int quantidade_de_alunos = 0;
    
    private String matricula;
    private String nome;
    private String curso;
    private char turma;
    private int periodo;
    private double nota_1b;
    private double nota_2b;
    private double nota_final;
    
    
    public void Aluno(String matricula, String nome, String curso, char turma, int periodo, double nota_1b, double nota_2b){
        this.matricula = matricula;
        this.nome = nome;
        this.curso = curso;
        this.turma = turma;
        this.periodo = periodo;
        this.nota_1b = nota_1b;
        this.nota_2b = nota_2b;
        quantidade_de_alunos++;
        CalcMedia();
    }
    
    public void ImprimirInfo(){
        System.out.printf("\n=======================================");
        System.out.printf("\nMatrícula: %s", this.matricula);
        System.out.printf("\nNome: %s", this.nome);
        System.out.printf("\nCurso: %s", this.curso);
        System.out.printf("\nTurma: %c", this.turma);
        System.out.printf("\nPeríodo: %d", this.periodo);
        System.out.printf("\nNota 1: %.2f", this.nota_1b);
        System.out.printf("\nNota 2: %.2f", this.nota_2b);
        System.out.printf("\nNota Final: %.2f", this.nota_final);
        System.out.printf("\n=======================================");
    }
    
    public String getNome(){
        return nome;
    }
    
    public String getCurso(){
        return curso;
    }
    
    public char getTurma(){
        return turma;
    }
    
    public int getPeriodo(){
        return periodo;
    }
    
    public double getNota_1b(){
        return nota_1b;
    }
    
    public double getNota_2b(){
        return nota_2b;
    }
    
    public double getNota_Final(){
        return nota_final;
    }

    public int getQuantidade_de_Alunos(){
        return quantidade_de_alunos;
    }
    
    public void setNome(String nome){
        this.nome = nome;
    }
    
    public void setCurso(String curso){
        this.curso = curso;
    }
    
    public void setTurma(char turma){
        this.turma = turma;
    }
    
    public void setPeriodo(int periodo){
        this.periodo = periodo;
    }
    
    public void setNota_1b(double nota_1b){
        this.nota_1b = nota_1b;
    }
    
    public void setNota_2b(double nota_2b){
        this.nota_2b = nota_2b;
        CalcMedia();
    }
    
    public void CalcMedia(){
        nota_final = (this.nota_1b + this.nota_2b) / 2;
    }
    
    public boolean Passar(char novaTurma, int novoPeriodo){
        if(this.nota_final>=7){
            this.turma = novaTurma;
            this.periodo = novoPeriodo;
            return true;
        }
        System.out.println("Reprovado.");
        return false;
    }
    
    
    public String SetMatricula(){
        Random rand = new Random();
        int n = 4;
        int v[] = new int[n];
        int i;
        for (i=0; i<n; i++){
            v[i] = rand.nextInt(9);
        }
        String quatro_numeros = "";
        for (i = 0; i < n; i++){
            quatro_numeros += v[i];
        }
        
        int ano_atual = Year.now().getValue();
        
        String matriculaData =  Integer.toString(ano_atual) + quatro_numeros; 
        return matriculaData;
    }
    
}
