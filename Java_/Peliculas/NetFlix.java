package Peliculas;

import java.util.ArrayList;

public class NetFlix {
    private ArrayList<Pelis> peliculass;
    String nombre;

    // Contructor
    NetFlix(String aNombre) {
        peliculass = new ArrayList<>();
        nombre = aNombre;
    }

    // Metodo
    public void addPeli(Pelis p) {
        peliculass.add(p);
    }

    public String impri() {
        String resultado = "";
        for (Pelis pelis : peliculass) {
            resultado += pelis.Peliculasa();
        }
        return resultado;
    }

    // public String GeneroPeli() {
    // String resultado2 = "";
    // for (Pelis pelis : peliculass) {
    // resultado2 += pelis.Peliculasa();
    // }
    // if (pelicula.VerGenero() == resultado2) {
    // return resultado2;
    // }

    // }
}
