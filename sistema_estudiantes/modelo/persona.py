# Clase base Persona
# Aquí aplicamos ENCAPSULACIÓN

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre   # atributo privado
        self.__edad = edad       # atributo privado

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    # Setter
    def set_edad(self, edad):
        if edad > 0:
            self.__edad = edad
        else:
            print("Edad inválida")

    # Método que será sobrescrito (polimorfismo)
    def mostrar_info(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}"
