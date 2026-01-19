# Clase de servicio
# Aquí va la lógica del sistema (NO es MVC)

class GestorEstudiantes:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def mostrar_estudiantes(self):
        for estudiante in self.estudiantes:
            print(estudiante.descripcion())
