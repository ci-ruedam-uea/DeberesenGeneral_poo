import json
import os
from modelos.producto import Producto


class Inventario:

    def __init__(self, archivo="inventario.json"):
        # Diccionario principal: {id: Producto}
        self.productos = {}
        self.archivo = archivo
        self.cargar_desde_archivo()

    # ==========================
    # MÉTODOS DE ARCHIVO
    # ==========================

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                datos = {id_: prod.to_dict() for id_, prod in self.productos.items()}
                json.dump(datos, f, indent=4)
            print("Inventario guardado correctamente.")
        except PermissionError:
            print("Error: No hay permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error inesperado al guardar: {e}")

    def cargar_desde_archivo(self):
        try:
            if not os.path.exists(self.archivo):
                with open(self.archivo, "w") as f:
                    json.dump({}, f)
                return

            with open(self.archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)
                for id_, info in datos.items():
                    self.productos[id_] = Producto.from_dict(info)

        except json.JSONDecodeError:
            print("Error: Archivo corrupto. Se iniciará vacío.")
            self.productos = {}
        except Exception as e:
            print(f"Error al cargar archivo: {e}")

    # ==========================
    # MÉTODOS DE GESTIÓN
    # ==========================

    def añadir_producto(self, id_producto, nombre, cantidad, precio):
        if id_producto in self.productos:
            print("Error: ID ya existente.")
            return

        self.productos[id_producto] = Producto(id_producto, nombre, cantidad, precio)
        self.guardar_en_archivo()
        print("Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        producto = self.productos.get(id_producto)

        if producto:
            if nueva_cantidad is not None:
                producto.set_cantidad(nueva_cantidad)

            if nuevo_precio is not None:
                producto.set_precio(nuevo_precio)

            self.guardar_en_archivo()
            print("Producto actualizado.")
        else:
            print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        resultados = [
            producto
            for producto in self.productos.values()
            if nombre.lower() in producto.get_nombre().lower()
        ]
        return resultados

    def mostrar_todos(self):
        if not self.productos:
            print("Inventario vacío.")
            return

        for producto in self.productos.values():
            print(producto)

    # ==========================
    # MÉTODO AVANZADO (TUPLA)
    # ==========================

    def resumen_inventario(self):
        """
        Devuelve una tupla con:
        (cantidad_total_productos, valor_total_inventario)
        """
        total_productos = len(self.productos)
        valor_total = sum(
            p.get_cantidad() * p.get_precio()
            for p in self.productos.values()
        )
        return (total_productos, valor_total)