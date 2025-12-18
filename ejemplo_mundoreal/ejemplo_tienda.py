# Ejemplo del Mundo Real: Sistema de una Tienda
# Programación Orientada a Objetos (POO)

# Clase Producto
class Producto:
    def __init__(self, nombre, precio, stock):
        # Atributos del producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        # Muestra la información del producto
        print(f"{self.nombre} | Precio: ${self.precio} | Stock disponible: {self.stock}")

    def vender(self, cantidad):
        # Método que controla la venta del producto
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        else:
            print("❌ No hay suficiente stock.")
            return False


# Clase Tienda
class Tienda:
    def __init__(self):
        # Lista de productos de la tienda
        self.productos = []

    def agregar_producto(self, producto):
        # Agrega un producto a la tienda
        self.productos.append(producto)

    def mostrar_productos(self):
        # Muestra todos los productos disponibles
        print("\n📦 Productos disponibles:")
        for i, producto in enumerate(self.productos, start=1):
            print(f"{i}. ", end="")
            producto.mostrar_info()

    def obtener_producto(self, indice):
        # Retorna un producto según la opción elegida
        if 0 <= indice < len(self.productos):
            return self.productos[indice]
        else:
            return None


# Clase Cliente
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

    def comprar(self, tienda):
        # Proceso de compra interactivo
        tienda.mostrar_productos()

        try:
            opcion = int(input("\nSeleccione el número del producto: ")) - 1
            producto = tienda.obtener_producto(opcion)

            if producto is None:
                print("❌ Producto inválido.")
                return

            cantidad = int(input("Ingrese la cantidad a comprar: "))

            if producto.vender(cantidad):
                total = producto.precio * cantidad
                print(f"✅ Compra realizada. Total a pagar: ${total}")

        except ValueError:
            print("❌ Error: Ingrese valores numéricos válidos.")


# Programa principal
if __name__ == "__main__":
    print("🛒 Bienvenido al sistema de la tienda\n")

    # Crear la tienda
    tienda = Tienda()

    # Agregar productos a la tienda
    tienda.agregar_producto(Producto("Arroz", 1.50, 20))
    tienda.agregar_producto(Producto("Azúcar", 1.20, 15))
    tienda.agregar_producto(Producto("Aceite", 3.00, 10))

    # Crear cliente
    nombre_cliente = input("Ingrese su nombre: ")
    cliente = Cliente(nombre_cliente)

    # Menú simple
    while True:
        print("\n📋 MENÚ")
        print("1. Ver productos")
        print("2. Comprar producto")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tienda.mostrar_productos()
        elif opcion == "2":
            cliente.comprar(tienda)
        elif opcion == "3":
            print("👋 Gracias por su visita.")
            break
        else:
            print("❌ Opción no válida.")
