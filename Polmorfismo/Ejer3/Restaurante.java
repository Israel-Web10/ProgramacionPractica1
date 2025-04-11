package Polmorfismo.Ejer3;

public class Restaurante {
    public static void main(String[] args) {
        Cocinero cocinero1 = new Cocinero("Carlos", 2500, 10, 15);
        Mesero mesero1 = new Mesero("Luis", 1800, 5, 12, 200);
        Mesero mesero2 = new Mesero("Ana", 1700, 8, 12, 150);
        Administrativo administrativo1 = new Administrativo("Marta", 3000, "Gerente");
        Administrativo administrativo2 = new Administrativo("Pedro", 2500, "Supervisor");

        System.out.println("----------------Calculo de sueldos totales--------------");
        cocinero1.calcularSueldoTotal();
        mesero1.calcularSueldoTotal();
        mesero2.calcularSueldoTotal();
        administrativo1.calcularSueldoTotal();
        administrativo2.calcularSueldoTotal();

        float sueldoBuscado = 2500;
        System.out.println("--------------------------------------------------------");
        System.out.println("Empleados con sueldo igual a " + sueldoBuscado + ":");
        if (cocinero1.getSueldoMensual() == sueldoBuscado) cocinero1.mostrarInformacion();
        if (mesero1.getSueldoMensual() == sueldoBuscado) mesero1.mostrarInformacion();
        if (mesero2.getSueldoMensual() == sueldoBuscado) mesero2.mostrarInformacion();
        if (administrativo1.getSueldoMensual() == sueldoBuscado) administrativo1.mostrarInformacion();
        if (administrativo2.getSueldoMensual() == sueldoBuscado) administrativo2.mostrarInformacion();
    }
}

class Cocinero {
    private String nombre;
    private float sueldoMensual, sueldoPorHora;
    private int horasExtras;

    public Cocinero(String nombre, float sueldoMensual, int horasExtras, float sueldoPorHora) {
        this.nombre = nombre;
        this.sueldoMensual = sueldoMensual;
        this.horasExtras = horasExtras;
        this.sueldoPorHora = sueldoPorHora;
    }

    public void calcularSueldoTotal() {
        float sueldoTotal = sueldoMensual + (horasExtras * sueldoPorHora);
        System.out.println(nombre + " es Cocinero y su sueldo total es: " + sueldoTotal);
    }

    public float getSueldoMensual() {
        return sueldoMensual;
    }

    public void mostrarInformacion() {
        System.out.println("Nombre: " + nombre + ", Sueldo: " + sueldoMensual);
    }
}

class Mesero {
    private String nombre;
    private float sueldoMensual, sueldoPorHora, propinas;
    private int horasExtras;

    public Mesero(String nombre, float sueldoMensual, int horasExtras, float sueldoPorHora, float propinas) {
        this.nombre = nombre;
        this.sueldoMensual = sueldoMensual;
        this.horasExtras = horasExtras;
        this.sueldoPorHora = sueldoPorHora;
        this.propinas = propinas;
    }

    public void calcularSueldoTotal() {
        float sueldoTotal = sueldoMensual + (horasExtras * sueldoPorHora) + propinas;
        System.out.println(nombre + " es Mesero y su sueldo total es: " + sueldoTotal);
    }

    public float getSueldoMensual() {
        return sueldoMensual;
    }

    public void mostrarInformacion() {
        System.out.println("Nombre: " + nombre + ", Sueldo: " + sueldoMensual);
    }
}

class Administrativo {
    private String nombre, cargo;
    private float sueldoMensual;

    public Administrativo(String nombre, float sueldoMensual, String cargo) {
        this.nombre = nombre;
        this.sueldoMensual = sueldoMensual;
        this.cargo = cargo;
    }

    public void calcularSueldoTotal() {
        System.out.println(nombre + " es Administrativo y su sueldo total es: " + sueldoMensual);
    }

    public float getSueldoMensual() {
        return sueldoMensual;
    }

    public void mostrarInformacion() {
        System.out.println("Nombre: " + nombre + ", Sueldo: " + sueldoMensual + ", Cargo: " + cargo);
    }
}
