package FlotaAutos;

public class Flota {
    // Atributos
    String Nombre;
    String Arrendatario;
    String[] Vehiculos;

    // Contructor
    public Flota(String _Nombre, String _Arrendatario) {
        Nombre = _Nombre;
        Arrendatario = _Arrendatario;
    }

    // Metodo
    public void MostrarAtributos() {
        System.out.println(Nombre);
        System.out.println(Arrendatario);
    }

}
