import json
import os

class Cliente:
    def __init__(self, id: int, nombre: str, telefono: int):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
    
    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "telefono": self.telefono}
    
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Teléfono: {self.telefono}"

class ArchivoCliente:
    def __init__(self, nomA: str):
        self.nomA = nomA
        if not os.path.exists(self.nomA):
            self.crearArchivo()
    
    def crearArchivo(self):
        with open(self.nomA, 'w') as f:
            json.dump([], f)  
    
    # a) Guardar cliente
    def guardaCliente(self, c: Cliente):
        clientes = self._leer_clientes()
        clientes.append(c.to_dict())
        with open(self.nomA, 'w') as f:
            json.dump(clientes, f, indent=4)
    
    # b) Buscar por ID
    def buscarCliente(self, id: int) -> Cliente:
        clientes = self._leer_clientes()
        for cli in clientes:
            if cli["id"] == id:
                return Cliente(cli["id"], cli["nombre"], cli["telefono"])
        return None
    
    # c) Buscar por teléfono
    def buscarCelularCliente(self, telefono: int) -> Cliente:
        clientes = self._leer_clientes()
        for cli in clientes:
            if cli["telefono"] == telefono:
                return Cliente(cli["id"], cli["nombre"], cli["telefono"])
        return None
    
    def _leer_clientes(self):
        with open(self.nomA, 'r') as f:
            return json.load(f)

# --- Pruebas ---
if __name__ == "__main__":
    archivo = ArchivoCliente("clientes.json")
    
   
    with open("clientes.json", 'w') as f:
        json.dump([], f)
    
    # Guardar clientes
    archivo.guardaCliente(Cliente(1, "Ana Pérez", 5551234))
    archivo.guardaCliente(Cliente(2, "Luis Gómez", 5555678))
    archivo.guardaCliente(Cliente(3, "Carlos Ruiz", 5559012))
    
    # Buscar por ID
    print("--- Buscar ID 2 ---")
    print(archivo.buscarCliente(2) or "No encontrado")
    
    # Buscar por teléfono
    print("\n--- Buscar teléfono 5559012 ---")
    print(archivo.buscarCelularCliente(5559012) or "No encontrado")