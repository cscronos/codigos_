package Sobrecarga;

public class Persona {
    // Atributos
    String nombre;
    int edad;
    String dmi;

    // Contructores
    // Esta es una sobrecarga de contructores
    public Persona(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    // Contructor sobrecargado
    public Persona(String dmi) {
        this.dmi = dmi;
    }

    // Metodos
    public void correr() {
        System.out.println("Soy " + nombre + ", tengo " + edad + " años y estoy corriendo una maraton");
    }

    // Sobrecarga de metodos
    public void correr(int km) {
        System.out.println("He corrido " + km + "kilometros");
    }
}
