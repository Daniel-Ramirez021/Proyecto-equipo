
import json
import os
import re

CARPETA = os.path.dirname(os.path.abspath(__file__))
ARCHIVO = os.path.join(CARPETA, "datos_academicos.json")


def validar_codigo(codigo):
    return bool(re.fullmatch(r"[A-Za-z0-9_-]+", codigo))


def datos_iniciales():
    return {
        "estudiantes": {},
        "profesores": {},
        "cursos": {},
        "inscripciones": [],
        "calificaciones": {}
    }


def cargar_datos():
    if not os.path.exists(ARCHIVO):
        return datos_iniciales()

    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        try:
            datos = json.load(archivo)
        except json.JSONDecodeError:
            raise ValueError(
                "El archivo de datos está dañado o no es JSON válido."
            )

    if not isinstance(datos, dict):
        raise ValueError("La estructura de datos es incorrecta.")

    estructura = datos_iniciales()

    for clave, valor in estructura.items():
        if clave not in datos:
            raise ValueError("Falta la sección: " + clave)

        if not isinstance(datos[clave], type(valor)):
            raise ValueError("Tipo incorrecto en: " + clave)

    return datos


def guardar_datos(datos):
    temporal = ARCHIVO + ".tmp"

    try:
        with open(temporal, "w", encoding="utf-8") as archivo:
            json.dump(
                datos,
                archivo,
                indent=4,
                ensure_ascii=False,
                allow_nan=False
            )

        os.replace(temporal, ARCHIVO)

    except (OSError, TypeError, ValueError):
        if os.path.exists(temporal):
            os.remove(temporal)

        raise
