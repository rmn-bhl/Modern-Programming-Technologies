using CalcInterfaces;
using System;

namespace CalcServer
{
    public class CalcService : ICalcService
    {
        public int Add(int a, int b) => a + b;

        public int Subtract(int a, int b) => a - b;

        public int Multiply(int a, int b) => a * b;

        public double Divide(double a, double b)
        {
            if (b == 0) throw new DivideByZeroException("Ділення на нуль!");
            return a / b;
        }

        public int Modulo(int a, int b)
        {
            if (b == 0) throw new DivideByZeroException("Ділення на нуль!");
            return a % b;
        }
    }
}
