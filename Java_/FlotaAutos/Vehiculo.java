package FlotaAutos;

public class Vehiculo {
    String Matricula;
    int Anho;
    String Marca;

    public Vehiculo(String _Matricula, int _Anho, String _Marca) {
        Matricula = _Matricula;
        Anho = _Anho;
        Marca = _Marca;
    }

    public String getMatricula() {
        return Matricula;
    }
}
