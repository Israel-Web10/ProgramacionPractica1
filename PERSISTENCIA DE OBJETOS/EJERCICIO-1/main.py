import json
import os

class Empleado:
    def __init__(self, nombre: str, edad: int, salario: float):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
    
    def to_dict(self):
        return {"nombre": self.nombre, "edad": self.edad, "salario": self.salario}
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Salario: ${self.salario:.2f}"

class ArchivoEmpleado:
    def __init__(self, nomA: str):
        self.nomA = nomA
        if not os.path.exists(self.nomA):
            self.crearArchivo()
    
    def crearArchivo(self):
        with open(self.nomA, 'w') as f:
            json.dump([], f)  # Archivo JSON vacío
    
    # a) Guardar empleado
    def guardarEmpleado(self, e: Empleado):
        empleados = self._leer_empleados()
        empleados.append(e.to_dict())
        with open(self.nomA, 'w') as f:
            json.dump(empleados, f, indent=4)
    
    # b) Buscar por nombre
    def buscaEmpleado(self, n: str) -> Empleado:
        empleados = self._leer_empleados()
        for emp in empleados:
            if emp["nombre"] == n:
                return Empleado(emp["nombre"], emp["edad"], emp["salario"])
        return None
    
    # c) Buscar por salario mayor
    def mayorSalario(self, s: float) -> Empleado:
        empleados = self._leer_empleados()
        for emp in empleados:
            if emp["salario"] > s:
                return Empleado(emp["nombre"], emp["edad"], emp["salario"])
        return None
    
    def _leer_empleados(self):
        with open(self.nomA, 'r') as f:
            return json.load(f)

# --- Pruebas ---
if __name__ == "__main__":
    archivo = ArchivoEmpleado("empleados.json")
    
    # Resetear archivo para pruebas (esta parte es opcional auxi :D)
    with open("empleados.json", 'w') as f:
        json.dump([], f)
    
    # Guardar empleados
    archivo.guardarEmpleado(Empleado("Ana", 30, 2500.50))
    archivo.guardarEmpleado(Empleado("Luis", 25, 1800.75))
    archivo.guardarEmpleado(Empleado("Carlos", 40, 3200.00))
    
    # Buscar empleado
    print("--- Buscar 'Luis' ---")
    print(archivo.buscaEmpleado("Luis") or "No encontrado")
    
    # Mayor salario
    print("\n--- Salario > $2000 ---")
    print(archivo.mayorSalario(2000) or "No encontrado")