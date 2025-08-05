using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    internal class AgendaTelefonica
    {
        Dictionary<string, string> agenda = new();

        public void Inserir(string nome, string numero)
        {
            agenda.Add(nome, numero);            
        }

        public string BuscarNumero(string numero)
        {
            Console.WriteLine($"Númerp:{agenda[numero]}");
        }

        public void Remover(string nome)
        {

        }

        public int tamanho()
        {

        }
    }
}
