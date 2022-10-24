package FlotaAutos;

public class Micros extends Vehiculo {
    int asientos;
    int pasajerosDepie;

    public Micros(String Matricula, int Anho, String Marca, int _asientos, int _pasajerosDepie) {
        super(Matricula, Anho, Marca);
        asientos = _asientos;
        pasajerosDepie = _pasajerosDepie;
    }

    public void tarifa() {
        int total = (asientos * 250) + (pasajerosDepie * 200) + (10000 - (500 * (2022 - Anho)));
        System.out.println("Tarifa de la micro: " + total);
    }
}
