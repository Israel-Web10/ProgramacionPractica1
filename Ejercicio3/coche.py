class Coche:
    # Crea una clase Coche con marca, modelo y velocidad
    def __init__(self, marca, modelo, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad

    # a) Método para acelerar que aumenta la velocidad en 10
    def acelerar(self):
        self.velocidad += 10

    # b) Método para frenar que disminuye la velocidad en 5
    def frenar(self):
        self.velocidad -= 5


if __name__ == "__main__":
    # c) Crea dos coches, aceléralos, frénalos y muestra sus velocidades
    c1 = Coche("Toyota", "Kia", 50)
    c2 = Coche("Ford", "Mustang", 80)

    c1.acelerar()
    c2.acelerar()
    c1.acelerar()
    c2.frenar()
    c1.frenar()

    # Mostrar velocidades
    print(f"Coche 1: {c1.velocidad} km/h")
    print(f"Coche 2: {c2.velocidad} km/h")