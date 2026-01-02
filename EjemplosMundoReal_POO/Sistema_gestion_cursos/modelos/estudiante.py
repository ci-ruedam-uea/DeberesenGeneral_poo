<<<<<<< HEAD
# Clase Estudiante
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

    def matricular(self, curso):
        if curso.asignar_cupo():
            print(f"✅ {self.nombre} se matriculó en '{curso.nombre}'")
        else:
            print(f"❌ No hay cupos disponibles en '{curso.nombre}'")
=======
# Clase Estudiante
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

    def matricular(self, curso):
        if curso.asignar_cupo():
            print(f"✅ {self.nombre} se matriculó en '{curso.nombre}'")
        else:
            print(f"❌ No hay cupos disponibles en '{curso.nombre}'")
>>>>>>> 6d8b9f39c4f9eba5a22d6bc2cb0effce649a2790
