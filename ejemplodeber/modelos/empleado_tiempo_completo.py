# Clase derivada que hereda de Empleado
# Aplicamos herencia y polimorfismo

from modelos.empleado import Empleado

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario, bono):
        super().__init__(nombre, salario)  # Herencia
        self.__bono = bono                 # Encapsulación

    def get_bono(self):
        return self.__bono

    # Polimorfismo: sobrescribimos el método calcular_pago
    def calcular_pago(self):
        return self.get_salario() + self.__bono
