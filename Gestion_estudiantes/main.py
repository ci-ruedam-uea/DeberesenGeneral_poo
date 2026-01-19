# Archivo principal para ejecutar la aplicación

from modelos.estudiante import Estudiante
from servicios.gestor_estudiantes import GestorEstudiantes

def main():
    gestor = GestorEstudiantes()

    # Crear instancias de Estudiante
    estudiante1 = Estudiante("Carlos", 20, "E001")
    estudiante2 = Estudiante("María", 22, "E002")

    # Agregar estudiantes al gestor
    gestor.agregar_estudiante(estudiante1)
    gestor.agregar_estudiante(estudiante2)

    # Mostrar información (polimorfismo en acción)
    gestor.mostrar_estudiantes()

if __name__ == "__main__":
    main()
