
import os
from personas import registrar_estudiante, registrar_profesor
from cursos import (
    registrar_curso,
    asignar_profesor,
    inscribir_estudiante,
    consultar_cursos_estudiante,
    consultar_estudiantes_curso
)
from calificaciones import (
    registrar_calificaciones,
    modificar_calificaciones,
    calcular_promedio,
    determinar_aprobacion,
    consultar_historial
)


def limpiar_pantalla():
    os.system("clear")


def mostrar_caratula():
    limpiar_pantalla()

    ancho = 76

    print("=" * ancho)
    print("UNIVERSIDAD MARIANO GÁLVEZ DE GUATEMALA".center(ancho))
    print("CENTRO UNIVERSITARIO COATEPEQUE".center(ancho))
    print("=" * ancho)

    print("\n" + "CARRERA".center(ancho))
    print("Ingeniería en Sistemas".center(ancho))

    print("\n" + "CURSO".center(ancho))
    print("Algoritmos".center(ancho))

    print("\n" + "CATEDRÁTICO".center(ancho))
    print("Ingeniero Demsshill Sandoval".center(ancho))

    print("\n" + "INTEGRANTES DEL GRUPO 4".center(ancho))
    print("Abner Daniel de León Ramírez".center(ancho))
    print("Julio Andrés Cárdenas Barrios".center(ancho))
    print("Herberth Iván Alay Cifuentes".center(ancho))
    print("Yoselin Yasmín Orozco Cabrera".center(ancho))

    print("\n" + "PROYECTO FINAL".center(ancho))
    print("Sistema de Gestión Académica Universitaria".center(ancho))
    print("Guatemala, 30 de octubre de 2026".center(ancho))

    print("=" * ancho)

    input("\nPresione Enter para continuar...")
    limpiar_pantalla()


def mostrar_menu():
    print("\n" + "=" * 55)
    print("SISTEMA DE GESTIÓN ACADÉMICA UNIVERSITARIA")
    print("=" * 55)

    print("1. Registrar estudiante")
    print("2. Registrar profesor")
    print("3. Registrar curso")
    print("4. Asignar profesor a un curso")
    print("5. Inscribir estudiante")
    print("6. Registrar calificaciones")
    print("7. Modificar calificaciones")
    print("8. Calcular promedio final")
    print("9. Consultar aprobación o reprobación")
    print("10. Consultar cursos de un estudiante")
    print("11. Consultar estudiantes de un curso")
    print("12. Consultar historial académico")
    print("0. Salir")
    print("=" * 55)


def main():
    opciones = {
        "1": registrar_estudiante,
        "2": registrar_profesor,
        "3": registrar_curso,
        "4": asignar_profesor,
        "5": inscribir_estudiante,
        "6": registrar_calificaciones,
        "7": modificar_calificaciones,
        "8": calcular_promedio,
        "9": determinar_aprobacion,
        "10": consultar_cursos_estudiante,
        "11": consultar_estudiantes_curso,
        "12": consultar_historial
    }

    mostrar_caratula()

    while True:
        mostrar_menu()

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "0":
            print("\nGracias por utilizar el sistema.")
            break

        if opcion in opciones:
            try:
                opciones[opcion]()
            except (OSError, ValueError) as error:
                print("\nError al procesar los datos:", error)
        else:
            print("\nOpción incorrecta. Intente nuevamente.")

        input("\nPresione Enter para volver al menú...")
        limpiar_pantalla()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nPrograma finalizado.")
