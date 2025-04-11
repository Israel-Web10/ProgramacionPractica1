package Ejercicio5;
//5. Crea una clase Estudiante con nombre, nota_1, nota_2
public class Estudiante {
    public String nombre;
    public int nota_1,nota_2;

    public Estudiante(String nombre, int nota_1, int nota_2) {
        this.nombre=nombre;
        this.nota_1=nota_1;
        this.nota_2=nota_2;
    }
    //a) Agrega un método para calcular el promedio
    public double promedio() {
        return (nota_1+nota_2)/2;
    }
    //b) Agrega un método para verificar si aprobó
    public void aprobo() {
        if( promedio()>=6){
            System.out.println("Aprobo");
        }else{
            System.out.println("No aprobo");
        }
    }
    public static void main(String[] args) {
        //c) Crea tres estudiantes, muestra sus promedios y si aprobaron
        Estudiante e1=new Estudiante("Carla",5,6);
        Estudiante e2=new Estudiante("Romina",7,8);
        Estudiante e3=new Estudiante("Pablo",4,3);
        System.out.println(e1.nombre + " - Promedio: " + e1.promedio());
        e1.aprobo();
        System.out.println(e2.nombre + " - Promedio: " + e2.promedio());
        e2.aprobo();
        System.out.println(e3.nombre + " - Promedio: " + e3.promedio());
        e3.aprobo();
    }
}