public class Main
{
	public static void main(String[] args) {
        Aluno al;
        al = new Aluno();
        
        al.SetPeriodo(3);
        
        
        al.TrocarInfo(al.SetMatricula(), "Arthur", "Ciencia", 'C', al.GetPeriodo(), 20, 14, 15);
        al.ImprimirInfo();
        al.CalcMedia();
        al.SetPeriodo(4);
        al.Passar('D', al.GetPeriodo());
        al.ImprimirInfo();
	}
}