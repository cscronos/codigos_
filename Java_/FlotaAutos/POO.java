package FlotaAutos;

public class POO {
    public static void main(String[] args) {
        Colectivo coleto = new Colectivo("JH-1J-0P", 2007, "Subaru", 4);
        Micros cromi = new Micros("JH-1J-0P", 2019, "Subaru", 20, 12);
        Camiones camioon = new Camiones("5T-PP-A7", 1997, "Mercedes", 30);

        cromi.tarifa();
        coleto.tarifa();
        camioon.tarifa();
    }
}