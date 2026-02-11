# Clase de servicio
# Aquí se maneja la lógica del sistema

class GestorEmpleados:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def mostrar_pagos(self):
        for empleado in self.empleados:
            print(
                f"Empleado: {empleado.get_nombre()} - Pago: {empleado.calcular_pago()}"
            )
