from servicios.inventario import Inventario


def menu():
    print("\n=== SISTEMA AVANZADO DE INVENTARIO ===")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Mostrar inventario")
    print("6. Mostrar resumen")
    print("7. Salir")


def main():
    inventario = Inventario()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_ = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                inventario.añadir_producto(id_, nombre, cantidad, precio)
            except ValueError:
                print("Datos inválidos.")

        elif opcion == "2":
            id_ = input("ID a eliminar: ")
            inventario.eliminar_producto(id_)

        elif opcion == "3":
            id_ = input("ID a actualizar: ")
            try:
                cantidad = input("Nueva cantidad (Enter para omitir): ")
                precio = input("Nuevo precio (Enter para omitir): ")

                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None

                inventario.actualizar_producto(id_, cantidad, precio)
            except ValueError:
                print("Datos inválidos.")

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            for r in resultados:
                print(r)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            total, valor = inventario.resumen_inventario()
            print(f"Total productos diferentes: {total}")
            print(f"Valor total del inventario: ${valor:.2f}")

        elif opcion == "7":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()