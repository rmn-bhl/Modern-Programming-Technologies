using System;
using System.ServiceModel;

namespace CalcServer
{
    class Program
    {
        static void Main(string[] args)
        {
            using (ServiceHost host = new ServiceHost(typeof(CalcService)))
            {
                host.Open();
                Console.WriteLine("CalcService is running. Address:");

                foreach (var endpoint in host.Description.Endpoints)
                    Console.WriteLine($"{endpoint.Address} ({endpoint.Binding.Name})");

                Console.WriteLine("\nPress Enter to stop...");
                Console.ReadLine();

                host.Close();
            }
        }
    }
}
