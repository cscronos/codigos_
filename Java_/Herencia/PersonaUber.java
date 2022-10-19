package Herencia;

public class PersonaUber extends AutoArriendo {

    // Variables
    String nombre;
    int cantPersonas;

    // Contructor
    PersonaUber(String aMatricula, String aMarca, int aCantPasajeros, int aCantRuedas, String aTipo, String aNombre,
            int aCanPersonas) throws Exception {
        super(aMatricula, aMarca, aCantPasajeros, aCantRuedas, aTipo);
        if (aCanPersonas > 0) {
            nombre = aNombre;
            cantPersonas = aCanPersonas;
        } else {
            throw new Exception("Ingrese bien los datos");
        }
    }

    // Polimorfismo
    // @Override

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
