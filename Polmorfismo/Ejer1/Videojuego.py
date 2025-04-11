class Videojuego:
    def __init__(self, nombre, plataforma, cantidad_jugadores=None):
        self.nombre = nombre
        self.plataforma = plataforma
        if cantidad_jugadores is None:
            self.cantidad_jugadores = 2  
        else:
            self.cantidad_jugadores = cantidad_jugadores

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Plataforma: {self.plataforma}")
        print(f"Jugadores: {self.cantidad_jugadores}")

    def agregar_jugador(self, cantidad=1):
        self.cantidad_jugadores += cantidad


if __name__ == "__main__":
    v1 = Videojuego("It takes two", "PC")
    v2 = Videojuego("FIFA 24", "PS5", 5)

    print("----------ANTES DE AGREGAR JUGADORES----------")
    v1.mostrar()
    v2.mostrar()

    v1.agregar_jugador()
    v2.agregar_jugador(3)

    print("----------DESPUÉS DE AGREGAR JUGADORES--------")
    v1.mostrar()
    v2.mostrar()
