
from datos import cargar_datos, guardar_datos, validar_codigo


def registrar_curso():
    datos = cargar_datos()

    print("\n--- REGISTRAR CURSO ---")

    codigo = input("Código del curso: ").strip().upper()

    if not validar_codigo(codigo):
        print("Error: código inválido.")
        return

    if codigo in datos["cursos"]:
        print("Error: el curso ya existe.")
        return

    nombre = input("Nombre del curso: ").strip()

    if not nombre or not any(c.isalpha() for c in nombre):
        print("Error: nombre inválido.")
        return

    datos["cursos"][codigo] = {
        "nombre": nombre,
        "profesor": None
    }

    guardar_datos(datos)
    print("Curso registrado correctamente.")
    print("Recuerde asignarle un profesor.")


def asignar_profesor():
    datos = cargar_datos()

    print("\n--- ASIGNAR PROFESOR ---")

    curso = input("Código del curso: ").strip().upper()
    profesor = input("Código del profesor: ").strip().upper()

    if curso not in datos["cursos"]:
        print("Error: el curso no existe.")
        return

    if profesor not in datos["profesores"]:
        print("Error: el profesor no existe.")
        return

    actual = datos["cursos"][curso]["profesor"]

    if actual == profesor:
        print("Este profesor ya está asignado.")
        return

    datos["cursos"][curso]["profesor"] = profesor

    guardar_datos(datos)
    print("Profesor asignado correctamente.")


def inscribir_estudiante():
    datos = cargar_datos()

    print("\n--- INSCRIBIR ESTUDIANTE ---")

    estudiante = input("Código del estudiante: ").strip().upper()
    curso = input("Código del curso: ").strip().upper()

    if estudiante not in datos["estudiantes"]:
        print("Error: el estudiante no existe.")
        return

    if curso not in datos["cursos"]:
        print("Error: el curso no existe.")
        return

    if datos["cursos"][curso]["profesor"] is None:
        print("Error: primero debe asignar un profesor.")
        return

    for inscripcion in datos["inscripciones"]:
        if (inscripcion["estudiante"] == estudiante
                and inscripcion["curso"] == curso):
            print("Error: el estudiante ya está inscrito.")
            return

    datos["inscripciones"].append({
        "estudiante": estudiante,
        "curso": curso
    })

    guardar_datos(datos)
    print("Inscripción realizada correctamente.")


def consultar_cursos_estudiante():
    datos = cargar_datos()

    print("\n--- CURSOS DE UN ESTUDIANTE ---")

    estudiante = input("Código del estudiante: ").strip().upper()

    if estudiante not in datos["estudiantes"]:
        print("Error: estudiante no encontrado.")
        return

    print("Estudiante:", datos["estudiantes"][estudiante]["nombre"])

    encontrados = 0

    for inscripcion in datos["inscripciones"]:
        if inscripcion["estudiante"] == estudiante:
            codigo = inscripcion["curso"]
            curso = datos["cursos"].get(codigo)

            if curso:
                print(codigo, "-", curso["nombre"])
                encontrados += 1

    if encontrados == 0:
        print("No tiene cursos inscritos.")


def consultar_estudiantes_curso():
    datos = cargar_datos()

    print("\n--- ESTUDIANTES DE UN CURSO ---")

    curso = input("Código del curso: ").strip().upper()

    if curso not in datos["cursos"]:
        print("Error: curso no encontrado.")
        return

    print("Curso:", datos["cursos"][curso]["nombre"])

    encontrados = 0

    for inscripcion in datos["inscripciones"]:
        if inscripcion["curso"] == curso:
            codigo = inscripcion["estudiante"]
            estudiante = datos["estudiantes"].get(codigo)

            if estudiante:
                print(codigo, "-", estudiante["nombre"])
                encontrados += 1

    if encontrados == 0:
        print("No hay estudiantes inscritos.")
