package FlotaAutos;

// Herencia
public class Colectivo extends Vehiculo {
    int asientos;

    public Colectivo(String Matricula, int Anho, String Marca, int _asientos) {
        super(Matricula, Anho, Marca);
        asientos = _asientos;
    }

    public void tarifa() {
        int precio = (asientos * 3000) + 10000;
        System.out.println("Tarifa de el colectivo: " + precio);
    }
}
