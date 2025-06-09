from typing import TypeVar, Generic, List, Callable

T = TypeVar('T')  

class Catalogo(Generic[T]):
    def __init__(self):
        self.elementos: List[T] = [] 


         # a) Agrega metodos
    def agregar(self, item: T):
        
        self.elementos.append(item)
        print(f"✅ '{item}' agregado al catálogo")

    def buscar(self, condicion: Callable[[T], bool]) -> List[T]:
        
        return [item for item in self.elementos if condicion(item)]

    def mostrar(self):
        
        print("\n📋 Contenido del catálogo:")
        for item in self.elementos:
            print(f"- {item}")
        print("-------------------")

# ===== Clases para probar =====
class Libro:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"Libro: {self.titulo} ({self.autor})"

class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre} - ${self.precio:.2f}"

# ===== Pruebas =====
if __name__ == "__main__":
    # b) Catálogo de libros
    catalogo_libros = Catalogo[Libro]()
    catalogo_libros.agregar(Libro("Cien años de soledad", "García Márquez"))
    catalogo_libros.agregar(Libro("1984", "George Orwell"))
    
    print("\n🔍 Buscar libros de García Márquez:")
    resultados = catalogo_libros.buscar(lambda libro: "García" in libro.autor)
    for libro in resultados:
        print(f"- {libro}")

    # c) Catálogo de productos
    catalogo_productos = Catalogo[Producto]()
    catalogo_productos.agregar(Producto("Laptop", 999.99))
    catalogo_productos.agregar(Producto("Mouse", 25.50))
    
    print("\n🔍 Buscar productos caros (> $100):")
    resultados = catalogo_productos.buscar(lambda prod: prod.precio > 100)
    for prod in resultados:
        print(f"- {prod}")

    # Mostrar todos los elementos
    catalogo_libros.mostrar()
    catalogo_productos.mostrar()