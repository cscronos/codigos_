package FlotaAutos;

public class Camiones extends Vehiculo {
    int tonelaje;

    public Camiones(String Matricula, int Anho, String Marca, int _tonelaje) {
        super(Matricula, Anho, Marca);
        tonelaje = _tonelaje;
    }

    public void tarifa() {
        int total = 10000 + (5000 * tonelaje);
        System.out.println("tarifa de camiones: " + total);
    }
}
