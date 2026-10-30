
import math
from datos import cargar_datos, guardar_datos

EVALUACIONES = {
    "1": ("Tareas", 35),
    "2": ("Primer parcial", 15),
    "3": ("Segundo parcial", 15),
    "4": ("Examen final", 35)
}

NOTA_MINIMA = 61


def verificar_inscripcion(datos, estudiante, curso):
    for inscripcion in datos["inscripciones"]:
        if (inscripcion["estudiante"] == estudiante
                and inscripcion["curso"] == curso):
            return True

    return False


def pedir_estudiante_curso(datos):
    estudiante = input("Código del estudiante: ").strip().upper()
    curso = input("Código del curso: ").strip().upper()

    if estudiante not in datos["estudiantes"]:
        print("Error: el estudiante no existe.")
        return None

    if curso not in datos["cursos"]:
        print("Error: el curso no existe.")
        return None

    if not verificar_inscripcion(datos, estudiante, curso):
        print("Error: el estudiante no está inscrito en el curso.")
        return None

    return estudiante, curso


def seleccionar_evaluacion():
    print("\n--- EVALUACIONES ---")

    for numero, (nombre, maximo) in EVALUACIONES.items():
        print(f"{numero}. {nombre} (máximo {maximo})")

    opcion = input("Seleccione una evaluación: ").strip()

    if opcion not in EVALUACIONES:
        print("Error: opción inválida.")
        return None

    return EVALUACIONES[opcion]


def pedir_nota(maximo):
    try:
        nota = float(input(f"Ingrese puntos obtenidos (0-{maximo}): "))

        if not math.isfinite(nota):
            print("Error: la nota debe ser un número válido.")
            return None

        if nota < 0 or nota > maximo:
            print(f"Error: la nota debe estar entre 0 y {maximo}.")
            return None

        return nota

    except ValueError:
        print("Error: debe ingresar un número.")
        return None


def obtener_resultado(datos, estudiante, curso):
    clave = estudiante + "|" + curso
    notas = datos["calificaciones"].get(clave, {})

    for nombre, maximo in EVALUACIONES.values():
        if nombre not in notas:
            return None

        nota = notas[nombre]

        if (not isinstance(nota, (int, float))
                or isinstance(nota, bool)
                or not math.isfinite(nota)
                or nota < 0
                or nota > maximo):
            return None

    total = sum(
        notas[nombre]
        for nombre, maximo in EVALUACIONES.values()
    )

    return total


def mostrar_resultado(datos, estudiante, curso):
    clave = estudiante + "|" + curso
    notas = datos["calificaciones"].get(clave, {})

    print("\n--- RESULTADO ACADÉMICO ---")

    for nombre, maximo in EVALUACIONES.values():
        if nombre in notas:
            print(f"{nombre}: {notas[nombre]:.2f}/{maximo}")
        else:
            print(f"{nombre}: PENDIENTE/{maximo}")

    total = obtener_resultado(datos, estudiante, curso)

    if total is None:
        print("Nota final: PENDIENTE")
        print("Faltan evaluaciones o existen notas inválidas.")
        return

    print(f"\nNota final: {total:.2f}/100")

    if total >= NOTA_MINIMA:
        print("Estado: APROBADO")
    else:
        print("Estado: REPROBADO")


def registrar_calificaciones():
    datos = cargar_datos()

    print("\n--- REGISTRAR CALIFICACIONES ---")

    resultado = pedir_estudiante_curso(datos)

    if resultado is None:
        return

    estudiante, curso = resultado

    evaluacion = seleccionar_evaluacion()

    if evaluacion is None:
        return

    nombre, maximo = evaluacion
    clave = estudiante + "|" + curso

    notas = datos["calificaciones"].get(clave, {})

    if nombre in notas:
        print("Error: la evaluación ya está registrada.")
        print("Use la opción de modificar calificaciones.")
        return

    nota = pedir_nota(maximo)

    if nota is None:
        return

    notas[nombre] = nota
    datos["calificaciones"][clave] = notas

    guardar_datos(datos)

    print("Calificación registrada correctamente.")
    mostrar_resultado(datos, estudiante, curso)


def modificar_calificaciones():
    datos = cargar_datos()

    print("\n--- MODIFICAR CALIFICACIONES ---")

    resultado = pedir_estudiante_curso(datos)

    if resultado is None:
        return

    estudiante, curso = resultado

    evaluacion = seleccionar_evaluacion()

    if evaluacion is None:
        return

    nombre, maximo = evaluacion
    clave = estudiante + "|" + curso

    notas = datos["calificaciones"].get(clave, {})

    if nombre not in notas:
        print("Error: esta evaluación no está registrada.")
        return

    print("Nota anterior:", notas[nombre])

    nueva_nota = pedir_nota(maximo)

    if nueva_nota is None:
        return

    notas[nombre] = nueva_nota

    guardar_datos(datos)

    print("Calificación modificada correctamente.")
    mostrar_resultado(datos, estudiante, curso)


def calcular_promedio():
    datos = cargar_datos()

    print("\n--- CALCULAR NOTA FINAL ---")

    resultado = pedir_estudiante_curso(datos)

    if resultado is None:
        return

    estudiante, curso = resultado
    mostrar_resultado(datos, estudiante, curso)


def determinar_aprobacion():
    datos = cargar_datos()

    print("\n--- APROBACIÓN O REPROBACIÓN ---")

    resultado = pedir_estudiante_curso(datos)

    if resultado is None:
        return

    estudiante, curso = resultado
    mostrar_resultado(datos, estudiante, curso)


def consultar_historial():
    datos = cargar_datos()

    print("\n--- HISTORIAL ACADÉMICO ---")

    estudiante = input("Código del estudiante: ").strip().upper()

    if estudiante not in datos["estudiantes"]:
        print("Error: estudiante no encontrado.")
        return

    print("\nEstudiante:", datos["estudiantes"][estudiante]["nombre"])
    print("Carrera:", datos["estudiantes"][estudiante]["carrera"])

    encontrados = 0

    for inscripcion in datos["inscripciones"]:
        if inscripcion["estudiante"] == estudiante:
            curso = inscripcion["curso"]
            informacion = datos["cursos"].get(curso)

            if informacion is None:
                continue

            encontrados += 1

            print("\nCurso:", informacion["nombre"])
            print("Código:", curso)

            mostrar_resultado(datos, estudiante, curso)

    if encontrados == 0:
        print("El estudiante no tiene cursos inscritos.")
