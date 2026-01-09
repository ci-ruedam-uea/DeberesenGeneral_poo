"Vista: VistaPersona"
"Descripción Manejar la entrada y salida de datos del usuario"

class vista_persona:
    
    def solicitar_datos(self):
        nombre = input("Ingrese el nombre de la persona: ")
        edad = int(input("Ingrese la edad: "))
        estatura = float(input("Ingrese la estatura en metros: "))
        estado_civil = input("¿Está casado/a (si/no): ").lower()
    
    return nombre, edad, estatura, estado_civil

def mostrar_datos(self, persona):
    print("\n--- DATOS REGISTRADOS ---")
    print(f"Nombre: {persona.nombre}")
    print(f"Edad: {persona.edad} años")
    print(f"Estatura: {persona.estatura} m")
    
    if persona.es_casado():
        print("Estado civil: Casado/a")
    else:
        print("Estado civil: Soltero/a")
        
    if persona.es_mayor_edad():
        print("La persona es mayor de edad.")
    else:
        print("La persona es menor de edad.")
        




