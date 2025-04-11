package Polmorfismo.Ejer7;
public class Perro {
    private String nombre;
    private int edad;
    private String raza;

    public Perro(String nombre, int edad, String raza) {
        this.nombre = nombre;
        this.edad = edad;
        this.raza = raza;
    }
    //b) Sobrecargar el método hacerSonido() para que cada animal emita su sonido
    //característico.
    public void hacerSonido() {
        System.out.println("El perro " + nombre + " ladra ");
    }
    public void hacerSonido(int veces) {
        System.out.println("El perro " + nombre + " ladra " + veces + " veces");
    }
    public void hacerSonido(String tono, int veces) {
        System.out.println("El perro " + nombre + " ladra con un tono " + tono + " " + veces + " veces");
    }
    //c) Implementar un método moverse() que indique cómo se mueve cada animal
    //(correr, saltar, volar, etc.).
    public void moverse(){
        System.out.println("El perro " + nombre + " corre ");
    }
}
