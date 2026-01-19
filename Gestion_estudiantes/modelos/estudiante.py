# Clase Estudiante que hereda de Persona
# Aplicamos herencia y polimorfismo

from modelos.persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, codigo):
        super().__init__(nombre, edad)  # herencia
        self.__codigo = codigo          # encapsulación

    def get_codigo(self):
        return self.__codigo

    # Polimorfismo: sobrescribimos el método descripcion
    def descripcion(self):
        return f"Estudiante: {self.get_nombre()}, Edad: {self.get_edad()}, Código: {self.__codigo}"
