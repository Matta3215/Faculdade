public class Main
{
	public static void main(String[] args) {
        Aluno al;
        al = new Aluno();
        
        al.setNome("Arthur");
        al.setCurso("Ciencia");
        al.setTurma('C');
        al.setPeriodo(3);
        al.setNota_1b(20);
        al.setNota_2b(16);
        
        
        al.Aluno(al.SetMatricula(), al.getNome(), al.getCurso(), al.getTurma(), al.getPeriodo(), al.getNota_1b(), al.getNota_2b());
        al.ImprimirInfo();
        al.CalcMedia();
        
        al.setPeriodo(4); 
        al.setTurma('D');
        
        al.Passar(al.getTurma(), al.getPeriodo());
        al.ImprimirInfo();
	}
}