from typing import TypeVar, Generic, List


T = TypeVar('T')

class Pila(Generic[T]):
    def __init__(self):
        self.elementos: List[T] = []  
    
    # a) Método para apilar
    def push(self, item: T) -> None:
        self.elementos.append(item)
    
    # b) Método para desapilar
    def pop(self) -> T:
        if not self.esta_vacia():
            return self.elementos.pop()
        else:
            raise IndexError("La pila está vacía")
    
    # Verificar si la pila esta vcia
    def esta_vacia(self) -> bool:
        return len(self.elementos) == 0
    
    # d) Mostrar los datos de la pila
    def mostrar(self) -> None:
        print("Contenido de la pila:")
        for item in reversed(self.elementos):
            print(item)

# c) Prueba con diferentes tipos de datos
if __name__ == "__main__":
    # Pila de enteros
    pila_enteros = Pila[int]()
    pila_enteros.push(10)
    pila_enteros.push(20)
    pila_enteros.push(30)
    pila_enteros.mostrar()
    print("Desapilado:", pila_enteros.pop())
    
    # Pila de strings
    pila_str = Pila[str]()
    pila_str.push("Hola")
    pila_str.push("Mundo")
    pila_str.mostrar()
    
    # Pila de objetos persnalizados
    class Persona:
        def __init__(self, nombre: str):
            self.nombre = nombre
        def __str__(self):
            return f"Persona: {self.nombre}"
    
    pila_personas = Pila[Persona]()
    pila_personas.push(Persona("Ana"))
    pila_personas.push(Persona("Luis"))
    pila_personas.mostrar()