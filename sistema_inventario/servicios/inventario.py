from modelos.producto import Producto

class Inventario:
    """
    Clase encargada de gestionar los productos.
    """

    def __init__(self):
        # Lista principal de almacenamiento
        self.productos = []

    def añadir_producto(self, id_producto, nombre, cantidad, precio):
        # Validar que el ID no esté repetido
        for producto in self.productos:
            if producto.get_id() == id_producto:
                print("Error: Ya existe un producto con ese ID.")
                return

        nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        print("Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                self.productos.remove(producto)
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
