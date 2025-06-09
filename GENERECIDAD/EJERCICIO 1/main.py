from typing import TypeVar, Generic

# Definimos un tipo generico T
T = TypeVar('T')

class Caja(Generic[T]):
    def __init__(self):
        self.contenido = None  # Inicialmente estara vacaa

        # a) Agrega metodos
    def guardar(self, obj: T):
        self.contenido = obj
        print(f"✅ Objeto guardado en la caja: {obj}")

    def obtener(self) -> T:
        if self.contenido is None:
            raise ValueError("La caja está vacía")
        return self.contenido


# --- Uso de la clase genérica ---
if __name__ == "__main__":
    # b) Crear dos cajas con tipos diferentes
    caja_entero = Caja[int]()       # Caja para enteros
    caja_string = Caja[str]()       # Caja para strings

    # Guardar datos en las cajas
    caja_entero.guardar(42)         # Guarda un entero
    caja_string.guardar("Hola")     # Guarda un string

    # c) Mostrar contenido de las cajas
    print("\n=== Contenido de las cajas ===")
    print(f"Caja de enteros: {caja_entero.obtener()}")
    print(f"Caja de strings: {caja_string.obtener()}")