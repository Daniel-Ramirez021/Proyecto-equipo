
from .datos import cargar_datos, guardar_datos, validar_codigo


def validar_texto(texto):
    return bool(texto.strip()) and any(
        caracter.isalpha() for caracter in texto
    )


def registrar_estudiante():
    datos = cargar_datos()

    print("\n--- REGISTRAR ESTUDIANTE ---")

    codigo = input("Código del estudiante: ").strip().upper()

    if not validar_codigo(codigo):
        print("Código inválido. Use letras, números, - o _.")
        return

    if codigo in datos["estudiantes"]:
        print("Error: el estudiante ya está registrado.")
        return

    nombre = input("Nombre completo: ").strip()
    carrera = input("Carrera: ").strip()

    if not validar_texto(nombre):
        print("Error: nombre inválido.")
        return

    if not validar_texto(carrera):
        print("Error: carrera inválida.")
        return

    datos["estudiantes"][codigo] = {
        "nombre": nombre,
        "carrera": carrera
    }

    guardar_datos(datos)
    print("Estudiante registrado correctamente.")


def registrar_profesor():
    datos = cargar_datos()

    print("\n--- REGISTRAR PROFESOR ---")

    codigo = input("Código del profesor: ").strip().upper()

    if not validar_codigo(codigo):
        print("Error: código inválido.")
        return

    if codigo in datos["profesores"]:
        print("Error: el profesor ya está registrado.")
        return

    nombre = input("Nombre completo: ").strip()
    especialidad = input("Especialidad: ").strip()

    if not validar_texto(nombre):
        print("Error: nombre inválido.")
        return

    if not validar_texto(especialidad):
        print("Error: especialidad inválida.")
        return

    datos["profesores"][codigo] = {
        "nombre": nombre,
        "especialidad": especialidad
    }

    guardar_datos(datos)
    print("Profesor registrado correctamente.")