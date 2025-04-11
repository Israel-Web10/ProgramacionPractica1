package Ejercicio7;
public class Celular {
    public int espacioDisponible = 1024; 
    public String[] aplicaciones = new String[20]; 
    public int[] tamanos = new int[20];
    public int bateria = 100; 
    public int contadorApps = 0; 
    //a) Crea un método para instalar una nueva aplicación
    public boolean instalarAplicacion(String nombre, int tamano) {
        if (contadorApps >= 20) {
            System.out.println("No se pueden instalar mas aplicaciones. Limite alcanzado.");
            return false;
        }
        if (tamano > espacioDisponible) {
            System.out.println("No hay suficiente espacio para instalar la aplicacion.");
            return false;
        }
        aplicaciones[contadorApps] = nombre;
        tamanos[contadorApps] = tamano;
        espacioDisponible -= tamano;
        contadorApps++;
        System.out.println("Aplicacion " + nombre + " instalada correctamente.");
        return true;
    }
//b) Crea un método para utilizar una aplicación (las aplicaciones que pesan más
//de 100Mb utilizan un 2% de batería por cada 10 minutos uso, las que pesan
//más de 250Mb utilizan 5% por cada 10 minutos de uso, en otros casos utiliza
//un 1% cada 10 minutos de uso)
    public void usarAplicacion(String nombre, int minutos) {
        if (bateria <= 0) {
            System.out.println("El celular esta apagado. No se puede usar.");
            return;
        }

        for (int i = 0; i < contadorApps; i++) {
            if (aplicaciones[i].equals(nombre)) {
                int tamano = tamanos[i];
                int consumo = 0;

                if (tamano > 250) {
                    consumo = 5 * (minutos / 10);
                } else if (tamano > 100) {
                    consumo = 2 * (minutos / 10);
                } else {
                    consumo = 1 * (minutos / 10);
                }

                bateria -= consumo;
                if (bateria <= 0) {
                    bateria = 0;
                    System.out.println("El celular se ha apagado por falta de bateria.");
                } else {
                    System.out.println("Usaste " + nombre + " por " + minutos + " minutos. Bateria restante: " + bateria + "%.");
                }
                return;
            }
        }
        System.out.println("La aplicacion " + nombre + " no esta instalada.");
    }
//c) Muestra el porcentaje de batería restante

    public void mostrarBateria() {
        System.out.println("Bateria restante: " + bateria + "%.");
    }
    //d) Cuando la batería se acabe al tratar de utilizar el celular este debe mostrar el
//mensaje de celular apagado

    public class Main {
        public static void main(String[] args) {
            
            celular celu = new celular();
            celu.instalarAplicacion("WhatsApp", 50);
            celu.instalarAplicacion("Yango", 300);
            celu.instalarAplicacion("RedBall4", 150);
            celu.usarAplicacion("RedBall4", 20);
            celu.mostrarBateria();    
            celu.usarAplicacion("Yango", 30);
            celu.mostrarBateria();
            celu.usarAplicacion("WhatsApp", 10);
            celu.mostrarBateria();
             //d) Cuando la batería se acabe al tratar de utilizar el celular este debe mostrar el
//mensaje de celular apagado
            celu.usarAplicacion("WhatsApp", 1000);
            celu.mostrarBateria();
            celu.usarAplicacion("Yango", 10);
            celu.mostrarBateria();
            celu.usarAplicacion("RedBall4", 10);
        }
    }
}