import os
from modelos.producto import Producto

class Inventario:
    """
    Clase encargada de gestionar los productos.
    Ahora incluye almacenamiento en archivo y manejo de excepciones.
    """

    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_desde_archivo()

    # ===============================
    # MÉTODOS DE ARCHIVO
    # ===============================

    def cargar_desde_archivo(self):
        """
        Carga los productos desde el archivo al iniciar el programa.
        """
        try:
            if not os.path.exists(self.archivo):
                # Si no existe, lo crea vacío
                open(self.archivo, "w").close()
                return

            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    try:
                        id_producto, nombre, cantidad, precio = linea.strip().split(",")
                        producto = Producto(
                            id_producto,
                            nombre,
                            int(cantidad),
                            float(precio)
                        )
                        self.productos.append(producto)
                    except ValueError:
                        print("Advertencia: línea corrupta ignorada.")

        except PermissionError:
            print("Error: No hay permisos para leer el archivo.")
        except Exception as e:
            print(f"Error inesperado al cargar archivo: {e}")

    def guardar_en_archivo(self):
        """
        Guarda todos los productos actuales en el archivo.
        """
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for producto in self.productos:
                    linea = f"{producto.get_id()},{producto.get_nombre()},{producto.get_cantidad()},{producto.get_precio()}\n"
                    f.write(linea)
            print("Cambios guardados en archivo correctamente.")

        except PermissionError:
            print("Error: No hay permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error inesperado al guardar archivo: {e}")

    # ===============================
    # MÉTODOS DE GESTIÓN
    # ===============================

    def añadir_producto(self, id_producto, nombre, cantidad, precio):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                print("Error: Ya existe un producto con ese ID.")
                return

        nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        self.guardar_en_archivo()
        print("Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                self.productos.remove(producto)
                self.guardar_en_archivo()
                print("Producto eliminado correctamente.")
                return

        print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for producto in self.productos:
            if producto.get_id() == id_producto:

                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)

                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)

                self.guardar_en_archivo()
                print("Producto actualizado correctamente.")
                return

        print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        resultados = []
        for producto in self.productos:
            if nombre.lower() in producto.get_nombre().lower():
                resultados.append(producto)
        return resultados

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
            return

        print("\n--- Inventario ---")
        for producto in self.productos:
            print(producto)