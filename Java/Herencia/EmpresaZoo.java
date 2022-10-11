package Herencia;

public class EmpresaZoo extends AutoArriendo {

    // Variables
    String nombreEmpresa;
    String queTransporta;
    int cantAnimales;

    // Contructor
    EmpresaZoo(String aMatricula, String aMarca, int aCantPasajeros, int aCantRuedas, String aTipo,
            String aNombreEmpresa,
            int aCantAnimales) throws Exception {
        super(aMatricula, aMarca, aCantPasajeros, aCantRuedas, aTipo);
        if (aCantAnimales >= 0) {
            cantAnimales = aCantAnimales;
            nombreEmpresa = aNombreEmpresa;
        } else {
            throw new Exception("Ingrese bien los datos");

        }

    }

    // Metodo
    public String QueTramporta() {
        String resultado = "";
        return resultado;
    }

    // Metodo Sobrecargado
    public String Pagar(int pago) {
        String resultado = "";
        return resultado;
    }
}
