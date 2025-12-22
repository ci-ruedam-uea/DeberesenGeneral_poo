from modelos.curso import Curso

# Clase Instituto
class Instituto:
    def __init__(self):
        self.cursos = []

    def agregar_curso(self, curso):
        self.cursos.append(curso)

    def mostrar_cursos(self):
        print("\n📘 Cursos disponibles:")
        for i, curso in enumerate(self.cursos, start=1):
            print(f"{i}. ", end="")
            curso.mostrar_info()

    def obtener_curso(self, indice):
        if 0 <= indice < len(self.cursos):
            return self.cursos[indice]
        return None
