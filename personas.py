import json
import os
import random
from datetime import datetime

# Archivos para guardar los registros
ARCHIVO_ESTUDIANTES = "estudiantes.json"
ARCHIVO_PROFESORES = "profesores.json"

# Solo las 3 carreras disponibles y sus codigos
CARRERAS = {
    "1": ("5646", "Mecanica Automotriz"),
    "2": ("6583", "Administracion de Empresas"),
    "3": ("2309", "Informatica")
}


# Cargar datos guardados
def cargar_datos(archivo):
    if os.path.exists(archivo):
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)

            if isinstance(datos, dict):
                return datos

            print("Error: formato incorrecto en el archivo.")

        except (json.JSONDecodeError, OSError):
            print("Error al leer el archivo:", archivo)

    return {}


# Guardar datos permanentemente
def guardar_datos(archivo, datos):
    try:
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)
        return True

    except OSError:
        print("Error: no se pudieron guardar los datos.")
        return False


# Validar nombres y especialidades
def validar_texto(texto):
    return (
        bool(texto)
        and all(
            letra.isalpha() or letra.isspace()
            for letra in texto
        )
        and any(letra.isalpha() for letra in texto)
    )


# Generar codigo automatico para estudiantes
def generar_codigo_estudiante(codigo_carrera):
    codigos_existentes = set(estudiantes) | set(profesores)
    anio = datetime.now().strftime("%y")

    while True:
        ultimo_numero = random.randint(1, 99999)
        codigo = f"{codigo_carrera}-{anio}-{ultimo_numero}"

        if codigo not in codigos_existentes:
            return codigo


# Generar codigo automatico para profesores
def generar_codigo_profesor():
    codigos_existentes = set(estudiantes) | set(profesores)
    anio = datetime.now().strftime("%y")

    while True:
        primeros_digitos = f"{random.randint(0, 9999):04d}"
        ultimo_numero = random.randint(1, 99999)
        codigo = f"{primeros_digitos}-{anio}-{ultimo_numero}"

        if codigo not in codigos_existentes:
            return codigo


# Mostrar y seleccionar una carrera
def seleccionar_carrera():
    print("\n--- CARRERAS DISPONIBLES ---")

    for opcion, (codigo, carrera) in CARRERAS.items():
        print(f"{opcion}. {carrera} (Codigo: {codigo})")

    while True:
        opcion = input("Seleccione la carrera (1-3): ").strip()

        if opcion in CARRERAS:
            return CARRERAS[opcion]

        print("Error: seleccione una opcion del 1 al 3.")


# Registrar estudiantes
def registrar_estudiante():
    print("\n--- REGISTRAR ESTUDIANTE ---")

    nombre = input("Nombre del estudiante: ").strip()

    if not validar_texto(nombre):
        print("Error: el nombre solo debe contener letras y espacios.")
        return

    codigo_carrera, carrera = seleccionar_carrera()
    codigo = generar_codigo_estudiante(codigo_carrera)

    estudiantes[codigo] = {
        "nombre": nombre,
        "carrera": carrera
    }

    if guardar_datos(ARCHIVO_ESTUDIANTES, estudiantes):
        print("\nEstudiante registrado correctamente.")
        print("Codigo generado:", codigo)
        print("Nombre:", nombre)
        print("Carrera:", carrera)
    else:
        del estudiantes[codigo]


# Registrar profesores
def registrar_profesor():
    print("\n--- REGISTRAR PROFESOR ---")

    nombre = input("Nombre del profesor: ").strip()

    if not validar_texto(nombre):
        print("Error: el nombre solo debe contener letras y espacios.")
        return

    especialidad = input("Especialidad del profesor: ").strip()

    if not validar_texto(especialidad):
        print("Error: la especialidad solo debe contener letras y espacios.")
        return

    codigo = generar_codigo_profesor()

    profesores[codigo] = {
        "nombre": nombre,
        "especialidad": especialidad
    }

    if guardar_datos(ARCHIVO_PROFESORES, profesores):
        print("\nProfesor registrado correctamente.")
        print("Codigo generado:", codigo)
        print("Nombre:", nombre)
        print("Especialidad:", especialidad)
    else:
        del profesores[codigo]


# Consultar estudiantes
def consultar_estudiantes():
    print("\n--- ESTUDIANTES REGISTRADOS ---")

    if not estudiantes:
        print("No hay estudiantes registrados.")
        return

    for codigo, datos in estudiantes.items():
        print("Codigo:", codigo)
        print("Nombre:", datos["nombre"])
        print("Carrera:", datos["carrera"])
        print("-" * 35)


# Consultar profesores
def consultar_profesores():
    print("\n--- PROFESORES REGISTRADOS ---")

    if not profesores:
        print("No hay profesores registrados.")
        return

    for codigo, datos in profesores.items():
        print("Codigo:", codigo)
        print("Nombre:", datos["nombre"])
        print("Especialidad:", datos["especialidad"])
        print("-" * 35)


# Menu principal
def menu_personas():
    while True:
        print("\n===== GESTION DE PERSONAS =====")
        print("1. Registrar estudiante")
        print("2. Registrar profesor")
        print("3. Consultar estudiantes")
        print("4. Consultar profesores")
        print("5. Consultar todas las personas")
        print("6. Salir")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_estudiante()

        elif opcion == "2":
            registrar_profesor()

        elif opcion == "3":
            consultar_estudiantes()

        elif opcion == "4":
            consultar_profesores()

        elif opcion == "5":
            consultar_estudiantes()
            consultar_profesores()

        elif opcion == "6":
            print("Los registros estan guardados.")
            print("Saliendo del modulo.")
            break

        else:
            print("Error: seleccione una opcion del 1 al 6.")


# Cargar los registros al iniciar
estudiantes = cargar_datos(ARCHIVO_ESTUDIANTES)
profesores = cargar_datos(ARCHIVO_PROFESORES)


# Ejecutar el menu
if __name__ == "__main__":
    menu_personas()