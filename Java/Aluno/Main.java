/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/


public class Main
{
	public static void main(String[] args) {
        Aluno al;
        al = new Aluno();
        
        al.SetPeriodo(3);
        
        
        al.TrocarInfo("2020202020", "Arthur", "Ciencia", 'C', al.GetPeriodo(), 20, 14, 15);
        al.ImprimirInfo();
        al.CalcMedia();
        al.SetPeriodo(4);
        al.Passar('D', al.GetPeriodo());
        al.ImprimirInfo();
        
        System.out.printf("\nNova Matrícula: %s ", al.SetMatricula());
	}
}