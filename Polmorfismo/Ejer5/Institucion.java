package Polmorfismo.Ejer5;

public class Institucion {
    public static void main(String[] args) {
     
        Oficina oficinaA = new Oficina(4, 2, 3);
        Oficina oficinaB = new Oficina(5, 3, 2);

        Aula aulaA = new Aula("A101", 30, 30);
        Aula aulaB = new Aula("B202", 25, 25);

        Laboratorio laboratorio = new Laboratorio("Lab Computacion", 20, 10, 20);

        System.out.println("-----------------OFICINAS----------------");
        System.out.println("Oficina tiene: " + oficinaA.calcularTotalMuebles(4, 3, 2));

        oficinaB.mostrarDetalles();
        System.out.println("Total muebles: " + oficinaB.calcularTotalMuebles());

        System.out.println("--------------------AULAS----------------------");
        aulaA.mostrarDetalles();
        System.out.println("Total muebles: " + aulaA.calcularTotalMuebles());

        aulaB.mostrarDetalles();
        System.out.println("Total muebles: " + aulaB.calcularTotalMuebles());

        System.out.println("-----------------LABORATORIO-----------------");
        laboratorio.mostrarDetalles();
        System.out.println("Total muebles: " + laboratorio.calcularTotalMuebles());
    }
}

class Oficina {
    int cantidadSillas, cantidadEscritorios, cantidadEstanterias;

    public Oficina(int sillas, int escritorios, int estanterias) {
        this.cantidadSillas = sillas;
        this.cantidadEscritorios = escritorios;
        this.cantidadEstanterias = estanterias;
    }

    public void mostrarDetalles() {
        System.out.println("Sillas: " + cantidadSillas);
        System.out.println("Escritorios: " + cantidadEscritorios);
        System.out.println("Estanterias: " + cantidadEstanterias);
    }

    public int calcularTotalMuebles(int sillas, int escritorios, int estanterias) {
        return sillas + escritorios + estanterias;
    }

    public int calcularTotalMuebles() {
        return calcularTotalMuebles(cantidadSillas, cantidadEscritorios, cantidadEstanterias);
    }
}

class Aula {
    String nombreAula;
    int capacidadAula, cantidadPupitres;

    public Aula(String nombre, int capacidad, int pupitres) {
        this.nombreAula = nombre;
        this.capacidadAula = capacidad;
        this.cantidadPupitres = pupitres;
    }

    public void mostrarDetalles() {
        System.out.println("Aula: " + nombreAula);
        System.out.println("Capacidad: " + capacidadAula);
        System.out.println("Pupitres: " + cantidadPupitres);
    }

    public int calcularTotalMuebles(int pupitres) {
        return pupitres;
    }

    public int calcularTotalMuebles() {
        return calcularTotalMuebles(cantidadPupitres);
    }
}

class Laboratorio {
    String nombreLaboratorio;
    int capacidadLaboratorio, cantidadMesas, cantidadSillas;

    public Laboratorio(String nombre, int capacidad, int mesas, int sillas) {
        this.nombreLaboratorio = nombre;
        this.capacidadLaboratorio = capacidad;
        this.cantidadMesas = mesas;
        this.cantidadSillas = sillas;
    }

    public void mostrarDetalles() {
        System.out.println("Laboratorio: " + nombreLaboratorio);
        System.out.println("Capacidad: " + capacidadLaboratorio);
        System.out.println("Mesas: " + cantidadMesas);
        System.out.println("Sillas: " + cantidadSillas);
    }

    public int calcularTotalMuebles(int mesas, int sillas) {
        return mesas + sillas;
    }
    
    public int calcularTotalMuebles() {
        return calcularTotalMuebles(cantidadMesas, cantidadSillas);
    }
}