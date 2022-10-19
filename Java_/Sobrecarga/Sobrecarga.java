package Sobrecarga;

public class Sobrecarga {
    public static void main(String[] args) {
        // Métodos
        Persona personal = new Persona("Cristobal", 20);
        personal.correr();
        // Método sobrecargado
        // es necesario hacerlos con diferente cantidad de parametros.
        Persona persona2 = new Persona("210279067");
        persona2.correr(100);
    }

}
