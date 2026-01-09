"Modelo: Persona"
"Descripcion: Representa la entidad Persona con sus atributos y metodos de validación"

class Persona: 
    def __init__(self, nombre, edad, estatura, estado_civil):
        self.nombre = nombre   #string 
        self.edad = edad       #int
        self.estatura = estatura  #float
        self.estadado_civil = estado_civil  #string
    def es_mayor_edad(self):
        return self.edad >= 18    #boolean
    
    def es_casado(self):
        return self.estado_civil == "si"  #boolean
        
        