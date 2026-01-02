# Clase Curso
class Curso:
    def __init__(self, nombre, cupos):
        self.nombre = nombre
        self.cupos = cupos

    def hay_cupo(self):
        return self.cupos > 0

    def asignar_cupo(self):
        if self.hay_cupo():
            self.cupos -= 1
            return True
        return False

    def mostrar_info(self):
        print(f"{self.nombre} | Cupos disponibles: {self.cupos}")
