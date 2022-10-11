package Herencia;

public class AutoArriendo {
    String matricula;
    String marca;
    int cantPasajeros;
    int cantRuedas;
    String tipo; // Acuatico, terreste, aereo

    // Contructor
    AutoArriendo(String aMatricula, String aMarca, int aCantPasajeros, int aCantRuedas, String aTipo)
            throws Exception {
        if (aCantPasajeros > 0 && aCantRuedas > 2) {
            matricula = aMatricula;
            marca = aMarca;
            cantPasajeros = aCantPasajeros;
            cantRuedas = aCantRuedas;
            tipo = aTipo;
        } else {
            throw new Exception("Ingrese bien los datos");

        }
    }
}
