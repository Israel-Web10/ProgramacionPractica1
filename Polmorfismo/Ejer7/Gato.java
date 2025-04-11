package Polmorfismo.Ejer7;
public class Gato {
    private String nombre;
    private String color;

    public Gato(String nombre, String color) {
        this.nombre = nombre;
        this.color = color;
    }
    //b) Sobrecargar el método hacerSonido() para que cada animal emita su sonido
    //característico.
    public void hacerSonido() {
        System.out.println("El gato " + nombre + " miau miau");
    }
    public void hacerSonido(int veces) {
        System.out.println("El gato " + nombre + " miau miau " + veces + " veces");
    }
    public void hacerSonido(String tono, int veces) {
        System.out.println("El gato " + nombre + " miau miau con un tono " + tono + " " + veces + " veces");
    }
    //c) Implementar un método moverse() que indique cómo se mueve cada animal
    //(correr, saltar, volar, etc.).
    public void moverse() {
        System.out.println("El gato " + nombre + " salta ");
    }
    
}
