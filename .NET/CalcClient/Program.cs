using CalcInterfaces;
using System;
using System.ServiceModel;

namespace CalcClient
{
    class Program
    {
        static void Main(string[] args)
        {
            var factory = new ChannelFactory<ICalcService>("CalcServiceEndpoint");
            ICalcService proxy = factory.CreateChannel();

            Console.WriteLine("5 + 4 = " + proxy.Add(5, 4));
            Console.WriteLine("5 - 4 = " + proxy.Subtract(5, 4));
            Console.WriteLine("5 * 4 = " + proxy.Multiply(5, 4));
            Console.WriteLine("5 / 4 = " + proxy.Divide(5, 4));
            Console.WriteLine("5 % 4 = " + proxy.Modulo(5, 4));

            ((IClientChannel)proxy).Close();
            factory.Close();

            Console.WriteLine("\nPress Enter to exit...");
            Console.ReadLine();
        }
    }
}
