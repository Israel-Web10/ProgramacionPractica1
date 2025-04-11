package Polmorfismo.Ejer1; 
public class Videojuego {
    private String nombre; 
    private String plataforma; 
    private int jugadores; 
    
    public Videojuego(String nombre, String plataforma) 
    {
        this.nombre = nombre;
        this.plataforma = plataforma;
        this.jugadores = 2; 
    }
    
    public Videojuego(String nombre, String plataforma, int jugadores) 
    {
        this.nombre = nombre;
        this.plataforma = plataforma;
        this.jugadores = jugadores; 
    }
    
    public void mostrar()
    {
        System.out.println("Nombre: " + nombre);
        System.out.println("Plataforma: " + plataforma);
        System.out.println("Jugadores: " + jugadores);
    }
    
    public void agregarJugador()
    {
        this.jugadores += 1; 
    }
    
    public void agregarJugador(int jugadores) 
    {
        this.jugadores += jugadores; 
    }
    
    public static void main(String[] args) {
        Videojuego juego1 = new Videojuego("It takes two", "PC"); 
        Videojuego juego2 = new Videojuego("FIFA 24", "PS5", 5); 
        
        System.out.println("----------ANTES DE AGREGAR JUGADORES----------");
        juego1.mostrar();
        juego2.mostrar();
        
        juego1.agregarJugador();
        juego2.agregarJugador(3);
        
        System.out.println("----------DESPUES DE AGREGAR JUGADORES--------");
        juego1.mostrar();
        juego2.mostrar();
    }  
}