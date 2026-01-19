# Clase base Persona
# Aquí aplicamos encapsulación y definición de atributos y métodos

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre     # atributo privado (encapsulación)
        self.__edad = edad

    # Métodos getter
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    # Método que será sobrescrito (polimorfismo)
    def descripcion(self):
        return f"Persona: {self.__nombre}, Edad: {self.__edad}"
