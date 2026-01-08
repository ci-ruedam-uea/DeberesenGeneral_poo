"""
Programa: Gestión básica de un registro de persona
Descripción: Este programa permite ingresar datos básicos de una persona,
como nombre, edad, estatura y estado civil. Luego muestra la información
y verifica si la persona es mayor de edad.
"""

# Entrada de datos
nombre_persona = input("Ingrese el nombre de la persona: ")  # string
edad_persona = int(input("Ingrese la edad: "))               # integer
estatura_persona = float(input("Ingrese la estatura en metros: "))  # float
estado_civil = input("¿Está casado/a? (si/no): ").lower()    # string

# Conversión a boolean
es_casado = estado_civil == "si"  # boolean

# Proceso lógico
es_mayor_edad = edad_persona >= 18  # boolean

# Salida de información
print("\n--- DATOS REGISTRADOS ---")
print(f"Nombre: {nombre_persona}")
print(f"Edad: {edad_persona} años")
print(f"Estatura: {estatura_persona} m")

if es_casado:
    print("Estado civil: Casado/a")
else:
    print("Estado civil: Soltero/a")

if es_mayor_edad:
    print("La persona es mayor de edad.")
else:
    print("La persona es menor de edad.")
