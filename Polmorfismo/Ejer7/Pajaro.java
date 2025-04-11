package Polmorfismo.Ejer7;

public class Pajaro {
    private String nombre;
    private String tipo;

    public Pajaro(String nombre, String tipo) {
        this.nombre = nombre;
        this.tipo = tipo;
    }
    //b) Sobrecargar el método hacerSonido() para que cada animal emita su sonido
    //característico.
    public void hacerSonido() {
        System.out.println("El pájaro " + nombre + " silbidos y chirridos ");
    }
    public void hacerSonido(int veces) {
        System.out.println("El pájaro " + nombre + " silbidos y chirridos " + veces + " veces");
    }
    public void hacerSonido(String tono, int veces) {
        System.out.println("El pájaro " + nombre + " silbidos y chirridos con un tono " + tono + " " + veces + " veces");
    }
    //c) Implementar un método moverse() que indique cómo se mueve cada animal
    //(correr, saltar, volar, etc.).
    public void moverse() {
        System.out.println("El pájaro " + nombre + " vuela ");
    }
    
}
