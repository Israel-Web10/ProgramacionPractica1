package Ejercicio3;
//Crea una clase Coche con marca, modelo y velocidad
public class Coche {
    public String marca;
    public String modelo;
    public int velocidad;

    public Coche(String marca, String modelo, int velocidad) {
        this.marca=marca;
        this.modelo=modelo;
        this.velocidad=velocidad;
    }
    //a) Agrega un método acelerar () que aumente la velocidad en 10
    public void acelerar() {
        velocidad += 10;
    }
    //b) Agrega un método frenar () que disminuya la velocidad en 5
    public void frenar() {
        velocidad -= 5;
    }
    public static void main(String[] args) {
        //c) Crea dos coches, aceléralos, frénalos y muestra sus velocidades
        Coche c1=new Coche("Toyota","Kia",50);
        Coche c2=new Coche("Ford","Mustang",80);
        c1.acelerar();
        c2.acelerar();
        c1.acelerar();
        c2.frenar();
        c1.frenar();
         // mostrar velocidades 
         System.out.println("coche 1: " + c1.velocidad);
         System.out.println("coche 2: " + c2.velocidad);
     
    }
}