import java.util.ArrayList;
import java.util.List;

public class Sorvete {
    private double preco;
    private int qntbolas;
    private List<Bola> bolas;

    public Sorvete() {
        bolas = new ArrayList<>();
        qntbolas = 0;
    }

    public void adicionarBola(String sabor) {
        Bola temp = new Bola(sabor);
        bolas.add(temp);
        qntbolas += 1;
    }

    public void imprimir() {
        System.out.println("Sorvete: ");
        for (Bola temp : bolas) {
            System.out.println(temp);
        }
    }

    public void calcPreco() {
        preco = 4.5 * qntbolas;
        System.out.println("Total de bolas de sorvete: " + qntbolas + ". Valor total: R$ " + preco);
    }

    public double getPreco() {
        return preco;
    }

    public int getQntBolas() {
        return qntbolas;
    }
}
