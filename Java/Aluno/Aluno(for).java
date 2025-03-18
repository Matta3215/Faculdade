import java.time.Year;
import java.util.Random;
import java.util.Scanner;

public class Aluno{
    public static int quantidade_de_alunos = 0;
    
    public String matricula;
    public String nome;
    public String curso;
    public char turma;
    private int periodo;
    public double nota_1b;
    public double nota_2b;
    public double nota_final;
    
    
    public void TrocarInfo(String matricula, String nome, String curso, char turma, int periodo, double nota_1b, double nota_2b, double nota_final){
        this.matricula = matricula;
        this.nome = nome;
        this.curso = curso;
        this.turma = turma;
        this.periodo = periodo;
        this.nota_1b = nota_1b;
        this.nota_2b = nota_2b;
        this.nota_final = nota_final;
        quantidade_de_alunos++;
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
        System.out.printf("\nNota final: %.2f", this.nota_final);
        System.out.printf("\n=======================================");
    }
    
    public int GetPeriodo(){
        return periodo;
    }
    
    public void SetPeriodo(int periodo){
        this.periodo = periodo;
    }
    
    public void CalcMedia(){
        double media = (this.nota_1b + this.nota_2b + nota_final) / 3;
        System.out.printf("\n\nMédia final: %.2f\n", media);
    }
    
    public void Passar(char turma, int periodo){
        this.turma = turma;
        this.periodo = periodo;
    }
    public String SetMatricula(){
        Random rand = new Random();
        int n = 4;
        int v[] = new int[n];
        int i;
        for (i=0; i<n; i++){
            v[i] = rand.nextInt(9);
        }
        int[] array = {1, 2, 3, 4, 5};
        String quatro_numeros = ""; // Sei que tem StringBuilder também
        for (i = 0; i < n; i++){
            quatro_numeros += v[i];
        }
        
        int ano_atual = Year.now().getValue();
        
        String matriculaData =  Integer.toString(ano_atual) + quatro_numeros; 
        return matriculaData;
    }
    
}

