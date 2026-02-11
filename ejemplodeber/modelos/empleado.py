# Clase base Empleado
# Aquí aplicamos encapsulación y definimos atributos y métodos comunes

class Empleado:
    def __init__(self, nombre, salario):
        self.__nombre = nombre     # Atributo privado (encapsulación)
        self.__salario = salario

    # Métodos getter para acceder a los atributos privados
    def get_nombre(self):
        return self.__nombre

    def get_salario(self):
        return self.__salario

    # Método que será sobrescrito (polimorfismo)
    def calcular_pago(self):
        return self.__salario
