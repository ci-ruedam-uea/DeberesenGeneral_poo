"Controlador: ControladorPersona"
"Descripción: Se coordina el flujo entre el modelo y la vista"

from modelo.persona import persona
from vista.vista_persona import vista_persona

class controlador_persona:
    
    def __int__(self):
        self.vista = VistaPersona()
    
def ejecutar(self):
    datos = self.vista.solicitar_datos()
    persona = persona(*datos)
    self.vista.mostrar_datos(persona)
    