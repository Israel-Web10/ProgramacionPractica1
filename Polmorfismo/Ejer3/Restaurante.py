class Cocinero:
    def __init__(self, nombre, sueldo_mensual, horas_extras, sueldo_por_hora):
        self.nombre = nombre
        self.sueldo_mensual = sueldo_mensual
        self.horas_extras = horas_extras
        self.sueldo_por_hora = sueldo_por_hora

    def calcular_sueldo_total(self):
        sueldo_total = self.sueldo_mensual + (self.horas_extras * self.sueldo_por_hora)
        print(f"{self.nombre} es Cocinero y su sueldo total es: {sueldo_total}")

    def get_sueldo_mensual(self):
        return self.sueldo_mensual

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Sueldo: {self.sueldo_mensual}")


class Mesero:
    def __init__(self, nombre, sueldo_mensual, horas_extras, sueldo_por_hora, propinas):
        self.nombre = nombre
        self.sueldo_mensual = sueldo_mensual
        self.horas_extras = horas_extras
        self.sueldo_por_hora = sueldo_por_hora
        self.propinas = propinas

    def calcular_sueldo_total(self):
        sueldo_total = self.sueldo_mensual + (self.horas_extras * self.sueldo_por_hora) + self.propinas
        print(f"{self.nombre} es Mesero y su sueldo total es: {sueldo_total}")

    def get_sueldo_mensual(self):
        return self.sueldo_mensual

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Sueldo: {self.sueldo_mensual}")


class Administrativo:
    def __init__(self, nombre, sueldo_mensual, cargo):
        self.nombre = nombre
        self.sueldo_mensual = sueldo_mensual
        self.cargo = cargo

    def calcular_sueldo_total(self):
        print(f"{self.nombre} es Administrativo y su sueldo total es: {self.sueldo_mensual}")

    def get_sueldo_mensual(self):
        return self.sueldo_mensual

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Sueldo: {self.sueldo_mensual}, Cargo: {self.cargo}")


if __name__ == "__main__":
    cocinero1 = Cocinero("Carlos", 2500, 10, 15)
    mesero1 = Mesero("Luis", 1800, 5, 12, 200)
    mesero2 = Mesero("Ana", 1700, 8, 12, 150)
    administrativo1 = Administrativo("Marta", 3000, "Gerente")
    administrativo2 = Administrativo("Pedro", 2500, "Supervisor")

    print("----------------Calculo de sueldos totales--------------")
    cocinero1.calcular_sueldo_total()
    mesero1.calcular_sueldo_total()
    mesero2.calcular_sueldo_total()
    administrativo1.calcular_sueldo_total()
    administrativo2.calcular_sueldo_total()

    sueldo_buscado = 2500
    print("--------------------------------------------------------")
    print(f"Empleados con sueldo igual a {sueldo_buscado}:")
    if cocinero1.get_sueldo_mensual() == sueldo_buscado:
        cocinero1.mostrar_informacion()
    if mesero1.get_sueldo_mensual() == sueldo_buscado:
        mesero1.mostrar_informacion()
    if mesero2.get_sueldo_mensual() == sueldo_buscado:
        mesero2.mostrar_informacion()
    if administrativo1.get_sueldo_mensual() == sueldo_buscado:
        administrativo1.mostrar_informacion()
    if administrativo2.get_sueldo_mensual() == sueldo_buscado:
        administrativo2.mostrar_informacion()