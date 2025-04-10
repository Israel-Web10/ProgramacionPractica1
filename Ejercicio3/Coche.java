package Ejercicio3;
public class Coche {
        public String fabricante;
        public String tipo;
        public int rapidez;
        public Coche(String fabricante, String tipo) {
            this.fabricante = fabricante;
            this.tipo = tipo;
            this.rapidez = 0;
        }

        public void acelerar() {
            rapidez += 10;
        }

        public void frenar() {
            if (rapidez >= 5) {
                rapidez -= 5;
            } else {
                rapidez = 0;
            }
        }

        public int getRapidez() {
            return rapidez;
        }

        public String getFabricante() {
            return fabricante;
        }

        public String getTipo() {
            return tipo;
        }
    public static void main(String[] args) {
        Coche coche1 = new Coche("Toyota", "Corolla");
        Coche coche2 = new Coche("Ford", "Focus");

        coche1.acelerar();
        coche1.acelerar();
        coche2.acelerar();

        coche1.frenar();
        coche2.frenar();

        System.out.println("Coche 1 (" + coche1.getFabricante() + " " + coche1.getTipo() + ") rapidez: " + coche1.getRapidez());
        System.out.println("Coche 2 (" + coche2.getFabricante() + " " + coche2.getTipo() + ") rapidez: " + coche2.getRapidez());
    }
}