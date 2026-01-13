# Clase derivada Estudiante
# Aquí aplicamos HERENCIA y POLIMORFISMO

from modelo.persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    # Polimorfismo: sobrescritura del método
    def mostrar_info(self):
        return f"Nombre: {self.get_nombre()}, Edad: {self.get_edad()}, Carrera: {self.carrera}"
