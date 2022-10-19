package Peliculas;

public class CinePlanes {
    public static void main(String[] args) {
        // Video Club
        try {
            Pelis pelicula1 = new Pelis("Shrek", "Comedia", 1600, 9);
            Pelis pelicula2 = new Pelis("Interestelar", "Ficción", 2014, 8);

            // LISTA
            NetFlix cine = new NetFlix("CinePlanet");
            // if (pelicula.VerGenero().equals(resultado2))
            cine.addPeli(pelicula1);
            cine.addPeli(pelicula2);
            System.out.println(cine.impri());
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

    }
}
