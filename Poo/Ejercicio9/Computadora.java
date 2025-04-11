package Ejercicio9;
public class Computadora {
    private String cpu;
    private int ram; 
    private int discoDuro;
    private boolean estaEncendida;

    public Computadora(String cpu, int ram, int discoDuro) {
        this.cpu = cpu;
        this.ram = ram;
        this.discoDuro = discoDuro;
        this.estaEncendida = false;
    }
    //a) Muestra los componentes principales de la computadora
    public void mostrarComponentes() {
        System.out.println("Procesador: " + cpu);
        System.out.println("Memoria RAM: " + ram + " GB");
        System.out.println("Almacenamiento: " + discoDuro + " GB");
    }
    //b) Muestra el estado de la computadora (encendido o apagado)
    public void encender() {
        if (!estaEncendida) {
            estaEncendida = true;
            System.out.println("La computadora se ha encendido.");
        } else {
            System.out.println("La computadora ya está encendida.");
        }
    }

    public void apagar() {
        if (estaEncendida) {
            estaEncendida = false;
            System.out.println("La computadora se ha apagado.");
        } else {
            System.out.println("La computadora ya está apagada.");
        }
    }

    public void mostrarEstado() {
        System.out.println("Estado: " + (estaEncendida ? "Encendida" : "Apagada"));
    }

    public static void main(String[] args) {
        //c) Crea una instancia y simula encender y apagar la computadora.
        Computadora miComputadora = new Computadora("Ryzen3", 12, 256);
        miComputadora.mostrarComponentes();
        miComputadora.mostrarEstado();
        miComputadora.encender();
        miComputadora.mostrarEstado();
        miComputadora.apagar();
        miComputadora.mostrarEstado();
    }
}