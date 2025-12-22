# Ejemplos del Mundo Real con Programación Orientada a Objetos

## Caso: Sistema de una Tienda Interactiva

Este proyecto representa un ejemplo del mundo real utilizando Programación Orientada a Objetos (POO) en Python, donde el usuario puede interactuar con el sistema mediante un menú en consola.

### Descripción del caso

Se modela el funcionamiento básico de una tienda.  
La tienda administra una lista de productos con nombre, precio y stock disponible.  
El usuario, representado como un cliente, puede visualizar los productos y realizar compras ingresando datos por teclado.  
El sistema controla el inventario y valida las compras realizadas.

### Funcionamiento general

- El usuario ingresa su nombre.
- Se muestra un menú interactivo en consola.
- El usuario puede:
  - Ver los productos disponibles.
  - Seleccionar un producto y la cantidad a comprar.
  - Salir del sistema.
- El stock se actualiza automáticamente después de cada compra.

### Conceptos de Programación Orientada a Objetos aplicados

- **Clases y objetos:** Producto, Tienda y Cliente.
- **Atributos:** nombre, precio, stock, lista de productos.
- **Métodos:** mostrar información, vender productos, realizar compras.
- **Interacción entre objetos:** el cliente interactúa con la tienda y los productos.
- **Encapsulación:** cada clase maneja su propia lógica interna.

### Archivo principal

- `ejemplo_tienda.py`: contiene el código del sistema interactivo de la tienda desarrollado con POO en Python.
