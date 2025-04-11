package Polmorfismo.Ejer7;

public class Main {
    public static void main(String[] args) {
        //a) Instanciar 1 Perro, 1 Gato y 1 Pájaro.
        Perro perro = new Perro("Nata", 5, "Labrador");
        Pajaro pajaro = new Pajaro("Lorito", "Canario");
        Gato gato = new Gato("Lia", "Gris");

        //b) Sobrecargar el método hacerSonido() para que cada animal emita su sonido
        //característico.
        System.out.println("-------I N C I S O     B-------");
        perro.hacerSonido(); 
        perro.hacerSonido(3); 
        perro.hacerSonido("grave", 2); 
        pajaro.hacerSonido();
        pajaro.hacerSonido(5);  
        pajaro.hacerSonido("agudo", 4);
        gato.hacerSonido();         
        gato.hacerSonido(2);
        gato.hacerSonido("suave", 3);
        //c) Implementar un método moverse() que indique cómo se mueve cada animal
        //(correr, saltar, volar, etc.).
        System.out.println("-------I N C I S O     c-------");
        perro.moverse(); 
        pajaro.moverse(); 
        gato.moverse(); 
    }    
}
