using System.ServiceModel;

namespace CalcInterfaces
{
    [ServiceContract]
    public interface ICalcService
    {
        [OperationContract]
        int Add(int a, int b);

        [OperationContract]
        int Subtract(int a, int b);

        [OperationContract]
        int Multiply(int a, int b);

        [OperationContract]
        double Divide(double a, double b);

        [OperationContract]
        int Modulo(int a, int b);
    }
}
