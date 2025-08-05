namespace ConsoleApp1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("É Manassés");

            int idade = 18;
            var idade2 = 19;

            if (idade != idade2)
            {
                Console.WriteLine("São irmãos próximos");
            }
            else {
                Console.WriteLine("São distantes");
            }

            Carro c01 = new Carro();
            c01.Modelo = "Fusca";
            c01.Acelerar();
        }
    }
}
