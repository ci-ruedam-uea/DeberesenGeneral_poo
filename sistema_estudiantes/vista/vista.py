# Vista: interacción con el usuario (entrada y salida)

class VistaEstudiante:

    def pedir_datos_estudiante(self):
        print("=== Ingreso de Datos del Estudiante ===")
        nombre = input("Ingrese el nombre: ")
        edad = int(input("Ingrese la edad: "))
        carrera = input("Ingrese la carrera: ")
        return nombre, edad, carrera

    def mostrar_estudiante(self, informacion):
        print("\n=== Información del Estudiante ===")
        print(informacion)

    def mostrar_mensaje(self, mensaje):
        print(mensaje)
