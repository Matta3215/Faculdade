using System;

public class AgendaTel
{
	public AgendaTel()
	{
        Dictionary<string, string> agenda = new();

        public void Inserir(string nome, string numero)
    {
        agenda.Add(nome, numero);
    }

    public string BuscarNumero(string numero)
    {
        Console.WriteLine($"Número:{agenda[numero]}");
    }

    public void Remover(string nome)
    {

    }

    public int tamanho()
    {

    }
}
}
