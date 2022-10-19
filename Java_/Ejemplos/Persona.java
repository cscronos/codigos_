package Ejemplos;

public class Persona {
    // Atributos
    private String nombre;
    private int edad;
    int tamaño;

    // Contructores con solucion de error
    Persona(String aNombre, int aEdad, int aTamaño) throws Exception {
        if (aEdad <= 0 || aTamaño < 0) {
            throw new Exception("La edad y el tamaño no puede ser menor que 0");
        } else {
            nombre = aNombre;
            edad = aEdad;
            tamaño = aTamaño;
        }

    }

    // Metodos
    public void Detalles() {
        System.out.println("Soy " + nombre + ", tengo " + edad + " años y mido " + tamaño + " cm");
    }

    // Set
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    // Get
    public String getNombre() {
        return nombre;
    }
}
