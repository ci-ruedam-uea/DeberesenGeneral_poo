<<<<<<< HEAD
from modelos.curso import Curso
from modelos.estudiante import Estudiante
from servicios.instituto import Instituto

def main():
    print("🎓 Sistema de Gestión de Cursos\n")

    instituto = Instituto()

    instituto.agregar_curso(Curso("Programación en Python", 3))
    instituto.agregar_curso(Curso("Bases de Datos", 2))
    instituto.agregar_curso(Curso("Redes", 1))

    nombre = input("Ingrese su nombre: ")
    estudiante = Estudiante(nombre)

    while True:
        print("\nMENÚ")
        print("1. Ver cursos")
        print("2. Matricularse")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            instituto.mostrar_cursos()

        elif opcion == "2":
            instituto.mostrar_cursos()
            try:
                num = int(input("Seleccione el número del curso: ")) - 1
                curso = instituto.obtener_curso(num)
                if curso:
                    estudiante.matricular(curso)
                else:
                    print("❌ Curso inválido")
            except ValueError:
                print("❌ Ingrese un número válido")

        elif opcion == "3":
            print("👋 Gracias por usar el sistema")
            break

        else:
            print("❌ Opción no válida")

if __name__ == "__main__":
    main()
=======
from modelos.curso import Curso
from modelos.estudiante import Estudiante
from servicios.instituto import Instituto

def main():
    print("🎓 Sistema de Gestión de Cursos\n")

    instituto = Instituto()

    instituto.agregar_curso(Curso("Programación en Python", 3))
    instituto.agregar_curso(Curso("Bases de Datos", 2))
    instituto.agregar_curso(Curso("Redes", 1))

    nombre = input("Ingrese su nombre: ")
    estudiante = Estudiante(nombre)

    while True:
        print("\nMENÚ")
        print("1. Ver cursos")
        print("2. Matricularse")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            instituto.mostrar_cursos()

        elif opcion == "2":
            instituto.mostrar_cursos()
            try:
                num = int(input("Seleccione el número del curso: ")) - 1
                curso = instituto.obtener_curso(num)
                if curso:
                    estudiante.matricular(curso)
                else:
                    print("❌ Curso inválido")
            except ValueError:
                print("❌ Ingrese un número válido")

        elif opcion == "3":
            print("👋 Gracias por usar el sistema")
            break

        else:
            print("❌ Opción no válida")

if __name__ == "__main__":
    main()
>>>>>>> 6d8b9f39c4f9eba5a22d6bc2cb0effce649a2790
