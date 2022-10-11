package Peliculas;

public class Pelis {
    // Atributos
    private String nombre;
    private String genero;
    private int añoEstreno;
    int puntuacion;

    // Contructor con arreglo de error
    Pelis(String aNombre, String aGenero, int aEstreno, int aPuntuacion) throws Exception {
        if (aEstreno <= 1700 && aPuntuacion <= 0) {
            throw new Exception("Ingrese bien los datos");
        } else {
            nombre = aNombre;
            genero = aGenero;
            añoEstreno = aEstreno;
            puntuacion = aPuntuacion;
        }
    }

    // Metodos
    public void Detalles() {
        System.out.println(getGenero());
    }

    public String Peliculasa() {
        return ("Nombre Peli: " + getNombre() + "\n" +
                "Genero: " + genero + "\n" +
                "Año de estreno: " + getAñoEstreno() + "\n" +
                "Puntuacion : " + puntuacion + "\n\n");
    }

    public String VerGenero() {
        return getNombre();
    }

    // Set y Get nombre
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getNombre() {
        return nombre;
    }

    // Set y Get Genero
    public void setGenero(String genero) {
        this.genero = genero;
    }

    public String getGenero() {
        return genero;
    }

    // Set y Get AñoEstreno
    public void setAñoEstreno(int añoEstreno) {
        this.añoEstreno = añoEstreno;
    }

    public int getAñoEstreno() {
        return añoEstreno;
    }
}
