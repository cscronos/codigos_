package Ejemplos;

public class ElMain {
    public static void main(String[] args) {
        // Métodos
        // Solucion de erroes
        try {
            Persona persona1 = new Persona("Cristobal", 20, 200);
            persona1.setNombre("Cs");
            persona1.Detalles();

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

    }
}