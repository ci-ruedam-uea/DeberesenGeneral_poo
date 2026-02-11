# Archivo principal para ejecutar el sistema

from modelos.empleado_tiempo_completo import EmpleadoTiempoCompleto
from servicios.gestor_empleados import GestorEmpleados

def main():
    gestor = GestorEmpleados()

    # Crear instancias de empleados
    empleado1 = EmpleadoTiempoCompleto("Ana", 500, 100)
    empleado2 = EmpleadoTiempoCompleto("Luis", 500, 150)

    # Agregar empleados al gestor
    gestor.agregar_empleado(empleado1)
    gestor.agregar_empleado(empleado2)

    # Mostrar pagos (polimorfismo en acción)
    gestor.mostrar_pagos()

if __name__ == "__main__":
    main()
