import json
import os

class Medicamento:
    def __init__(self, nombre: str, codMedicamento: int, tipo: str, precio: float):
        self.nombre = nombre
        self.codMedicamento = codMedicamento
        self.tipo = tipo
        self.precio = precio
    
    def leer(self):
        self.nombre = input("Nombre del medicamento: ")
        self.codMedicamento = int(input("Código: "))
        self.tipo = input("Tipo (ej. 'tos', 'dolor'): ")
        self.precio = float(input("Precio: "))
    
    def mostrar(self):
        print(f"Nombre: {self.nombre}, Código: {self.codMedicamento}, Tipo: {self.tipo}, Precio: ${self.precio:.2f}")
    
    def getTipo(self) -> str:
        return self.tipo
    
    def getPrecio(self) -> float:
        return self.precio

class Farmacia:
    def __init__(self):
        self.nombreFarmacia = ""
        self.sucursal = 0
        self.directori = ""
        self.moMedicamentos = 0
        self.m = [None] * 100  # Lista de Medicamentos (máx 100)
    
    def leer(self):
        self.nombreFarmacia = input("Nombre de la farmacia: ")
        self.sucursal = int(input("Número de sucursal: "))
        self.directori = input("Dirección: ")
        self.moMedicamentos = int(input("Cantidad de medicamentos (máx 100): "))
        for i in range(self.moMedicamentos):
            print(f"\nMedicamento {i + 1}:")
            self.m[i] = Medicamento("", 0, "", 0.0)
            self.m[i].leer()
    
    def mostrar(self):
        print(f"\nFarmacia: {self.nombreFarmacia}")
        print(f"Sucursal: {self.sucursal}, Dirección: {self.directori}")
        print("Medicamentos:")
        for i in range(self.moMedicamentos):
            self.m[i].mostrar()
    
    def getPreccion(self) -> str:
        return self.directori
    
    def getSucursal(self) -> int:
        return self.sucursal
    
    def mostraMedicamentos(self):
        for i in range(self.moMedicamentos):
            self.m[i].mostrar()
    
    def buscaMedicamento(self, x: str) -> Medicamento:
        for i in range(self.moMedicamentos):
            if self.m[i].nombre.lower() == x.lower():
                return self.m[i]
        return None

class ArchFarmacia:
    def __init__(self, na: str):
        self.na = na
        if not os.path.exists(self.na):
            self.creatArchivo()
    
    def creatArchivo(self):
        with open(self.na, 'w') as f:
            json.dump([], f)
    
    def adicionar(self, farmacia: Farmacia):
        data = []
        if os.path.getsize(self.na) > 0:
            with open(self.na, 'r') as f:
                data = json.load(f)
        
        farmacia_dict = {
            "nombreFarmacia": farmacia.nombreFarmacia,
            "sucursal": farmacia.sucursal,
            "directori": farmacia.directori,
            "moMedicamentos": farmacia.moMedicamentos,
            "medicamentos": [
                {
                    "nombre": farmacia.m[i].nombre,
                    "codMedicamento": farmacia.m[i].codMedicamento,
                    "tipo": farmacia.m[i].tipo,
                    "precio": farmacia.m[i].precio
                } 
                for i in range(farmacia.moMedicamentos) if farmacia.m[i] is not None
            ]
        }
        data.append(farmacia_dict)
        with open(self.na, 'w') as f:
            json.dump(data, f, indent=4)
    
    def listar(self):
        with open(self.na, 'r') as f:
            data = json.load(f)
            for farmacia in data:
                print(f"\nFarmacia: {farmacia['nombreFarmacia']}")
                print(f"Sucursal: {farmacia['sucursal']}, Dirección: {farmacia['directori']}")
                print("Medicamentos:")
                for med in farmacia['medicamentos']:
                    print(f"  Nombre: {med['nombre']}, Tipo: {med['tipo']}, Precio: ${med['precio']:.2f}")
    
    def mostraMedicamentosRestrios(self, tipo: str = "tos"):
        with open(self.na, 'r') as f:
            data = json.load(f)
            print(f"\nMedicamentos para {tipo}:")
            for farmacia in data:
                for med in farmacia['medicamentos']:
                    if med['tipo'].lower() == tipo.lower():
                        print(f"  Farmacia: {farmacia['nombreFarmacia']}, Sucursal: {farmacia['sucursal']}")
                        print(f"  Medicamento: {med['nombre']}, Precio: ${med['precio']:.2f}")
    
    def preciomedicamentoTos(self) -> float:
        total = 0.0
        with open(self.na, 'r') as f:
            data = json.load(f)
            for farmacia in data:
                for med in farmacia['medicamentos']:
                    if med['tipo'].lower() == "tos":
                        total += med['precio']
        return total
    
    def mostraMedicamentosMerrorTos(self):
        min_precio = float('inf')
        resultado = None
        with open(self.na, 'r') as f:
            data = json.load(f)
            for farmacia in data:
                for med in farmacia['medicamentos']:
                    if med['tipo'].lower() == "tos" and med['precio'] < min_precio:
                        min_precio = med['precio']
                        resultado = {
                            "farmacia": farmacia['nombreFarmacia'],
                            "sucursal": farmacia['sucursal'],
                            "medicamento": med['nombre'],
                            "precio": med['precio']
                        }
        if resultado:
            print(f"\nMedicamento para tos más barato:")
            print(f"  Farmacia: {resultado['farmacia']}, Sucursal: {resultado['sucursal']}")
            print(f"  Medicamento: {resultado['medicamento']}, Precio: ${resultado['precio']:.2f}")
        else:
            print("No hay medicamentos para la tos.")

# --- Pruebas ---
if __name__ == "__main__":
    archivo = ArchFarmacia("farmacias.json")
    
    # Crear y guardar farmacias (ejemplo)
    if not os.path.exists("farmacias.json") or os.path.getsize("farmacias.json") == 0:
        f1 = Farmacia()
        f1.nombreFarmacia = "Farmacia A"
        f1.sucursal = 1
        f1.directori = "Calle 1"
        f1.moMedicamentos = 2
        f1.m[0] = Medicamento("Golpex", 101, "tos", 15.50)
        f1.m[1] = Medicamento("Paracetamol", 102, "dolor", 10.00)
        archivo.adicionar(f1)
        
        f2 = Farmacia()
        f2.nombreFarmacia = "Farmacia B"
        f2.sucursal = 2
        f2.directori = "Calle 2"
        f2.moMedicamentos = 2
        f2.m[0] = Medicamento("Jarabe", 201, "tos", 12.00)
        f2.m[1] = Medicamento("Ibuprofeno", 202, "dolor", 8.50)
        archivo.adicionar(f2)
    
    # a) Listar farmacias
    print("=== Todas las farmacias ===")
    archivo.listar()
    
    # b) Medicamentos para la tos en sucursal X
    print("\n=== Medicamentos para tos en Sucursal 1 ===")
    archivo.mostraMedicamentosRestrios("tos")
    
    # c) Buscar "Golpex"
    print("\n=== Farmacias con Golpex ===")
    with open("farmacias.json", 'r') as f:
        data = json.load(f)
        for farmacia in data:
            for med in farmacia['medicamentos']:
                if med['nombre'].lower() == "golpex":
                    print(f"Sucursal: {farmacia['sucursal']}, Dirección: {farmacia['directori']}")