# Clase Estudiante
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

    def matricular(self, curso):
        if curso.asignar_cupo():
            print(f"✅ {self.nombre} se matriculó en '{curso.nombre}'")
        else:
            print(f"❌ No hay cupos disponibles en '{curso.nombre}'")
