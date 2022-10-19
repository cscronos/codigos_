package Herencia;

public class Home {
    public static void main(String[] args) throws Exception {
        try {
            PersonaUber Persona1 = new PersonaUber("AH1-495-LOP", "Mercedes", 4, 4, "Terrestre", "Luis", 2);
            EmpresaZoo Persona2 = new EmpresaZoo("AKJ-381-AS1", "Toyota", 24, 6, "Terrestre", "WinZoo", 7);

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
