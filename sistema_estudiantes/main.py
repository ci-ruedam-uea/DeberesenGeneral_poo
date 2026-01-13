# Punto de entrada del programa

from controlador.controlador import ControladorEstudiante

def main():
    controlador = ControladorEstudiante()
    controlador.iniciar()

if __name__ == "__main__":
    main()
