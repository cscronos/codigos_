package Peliculas;

public class Actores {
    // Atributos
    String nombre;
    private int edad;

    // Contructores
    Actores(String aNombre, int aEdad) throws Exception {
        if (aEdad > 0) {
            throw new Exception("Ingrese bien los datos");
        } else {
            nombre = aNombre;
        }
    }

    // Set y Get 01
    public void setNombreActor(int edad) {
        this.edad = edad;
    }

    public int getEdadActor() {
        return edad;
    }

}
