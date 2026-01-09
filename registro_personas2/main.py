"Programa: Que gestiona el registro de personas"
"Descripción: Aplicativo desarrollado con POO"

from controlador.controlador_persona import ControladorPersona

def main():
    app = ControladorPersona()
    app.ejecutar()
    
if __name__ == "__main__":
    main()
    
    