from modelos.cuenta_bancaria import CuentaBancaria

class ServicioCuenta:
    def iniciar_menu(self):
        titular = input("Ingrese el nmbre del titular: ")
        saldo_inicial = float(input("Ingrese el saldo inicial: "))

        cuenta = CuentaBancaria(titular, saldo_inicial)

        opcion = 0
        while opcion != 4:
            print("\n--- MENÚ BANCARIO ---")
            print("1. Depositar")
            print("2. Retirar")
            print("3. Consultar saldo")
            print("4. Salir")

            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                monto = float(input("Ingrese el monto a depositar: "))
                cuenta.depositar(monto)

            elif opcion == 2:
                monto = float(input("Ingrese el monto a retirar: "))
                cuenta.retirar(monto)

            elif opcion == 3:
                cuenta.mostrar_saldo()

            elif opcion == 4:
                print("Saliendo del sistema...")

            else:
                print("Opción inválida.")

        # Cuando termina el método, el objeto puede eliminarse
        # y ejecutarse el destructor __del__
