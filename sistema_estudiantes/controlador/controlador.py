# Controlador: coordina modelo y vista

from modelo.estudiante import Estudiante
from vista.vista import VistaEstudiante

class ControladorEstudiante:

    def __init__(self):
        self.vista = VistaEstudiante()

    def iniciar(self):
        # Pedir datos a la vista
        nombre, edad, carrera = self.vista.pedir_datos_estudiante()

        # Crear objeto Estudiante (POO)
        estudiante = Estudiante(nombre, edad, carrera)

        # Mostrar información
        self.vista.mostrar_estudiante(estudiante.mostrar_info())

        # Actualizar edad (encapsulación)
        nueva_edad = int(input("\nIngrese nueva edad: "))
        estudiante.set_edad(nueva_edad)
        self.vista.mostrar_mensaje("Edad actualizada correctamente")
        self.vista.mostrar_estudiante(estudiante.mostrar_info())
