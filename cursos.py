class Estudiante:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def __str__(self):
        return f"Codigo: {self.codigo} | Nombre: {self.nombre}"


class Profesor:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def __str__(self):
        return f"Codigo: {self.codigo} | Nombre: {self.nombre}"


class Curso:
    def __init__(self, codigo, nombre, profesor):
        self.codigo = codigo
        self.nombre = nombre
        self.profesor = profesor
        self.estudiantes_inscritos = {}

    def __str__(self):
        return f"Curso: [{self.codigo}] {self.nombre} | Profesor: {self.profesor.nombre} | Inscritos: {len(self.estudiantes_inscritos)}"


class SistemaCursos:
    def __init__(self):
        self.estudiantes = {}
        self.profesores = {}
        self.cursos = {}
        self.precargar_datos()

    def precargar_datos(self):
        self.estudiantes["101"] = Estudiante("101", "Ana Perez")
        self.estudiantes["102"] = Estudiante("102", "Carlos Gomez")
        self.estudiantes["103"] = Estudiante("103", "Maria Rodriguez")

        self.profesores["201"] = Profesor("201", "Martinez")
        self.profesores["202"] = Profesor("202", "Fernandez")

        self.cursos["301"] = Curso("301", "Matematicas", self.profesores["201"])
        self.cursos["302"] = Curso("302", "Historia", self.profesores["202"])

    def codigo_existe_general(self, codigo):
        return codigo in self.estudiantes or codigo in self.profesores or codigo in self.cursos

    def registrar_curso(self, codigo_curso, nombre_curso, codigo_profesor):
        if self.codigo_existe_general(codigo_curso):
            return "Error: El codigo del curso ya existe en el sistema."
        if codigo_profesor not in self.profesores:
            return "Error: El profesor responsable no esta registrado en el sistema."

        nombre_normalizado = nombre_curso.strip().title()
        for curso in self.cursos.values():
            if curso.nombre == nombre_normalizado:
                return "Error: Ya existe un curso registrado con este mismo nombre."

        profesor = self.profesores[codigo_profesor]
        self.cursos[codigo_curso] = Curso(codigo_curso, nombre_normalizado, profesor)
        return f"Curso '{nombre_normalizado}' registrado y asignado al profesor {profesor.nombre} con exito."

    def inscribir_estudiante(self, codigo_estudiante, codigo_curso):
        if codigo_estudiante not in self.estudiantes:
            return "Error: El estudiante no esta registrado en el sistema."
        if codigo_curso not in self.cursos:
            return "Error: El curso no existe en el sistema."

        curso = self.cursos[codigo_curso]
        estudiante = self.estudiantes[codigo_estudiante]

        if codigo_estudiante in curso.estudiantes_inscritos:
            return f"Error: El estudiante '{estudiante.nombre}' ya se encuentra inscrito en el curso '{curso.nombre}'."

        curso.estudiantes_inscritos[codigo_estudiante] = estudiante
        return f"Estudiante '{estudiante.nombre}' inscrito correctamente en el curso '{curso.nombre}'."

    def consultar_cursos_de_estudiante(self, codigo_estudiante):
        if codigo_estudiante not in self.estudiantes:
            return "Error: El estudiante no existe en el sistema."

        estudiante = self.estudiantes[codigo_estudiante]
        cursos_encontrados = [c for c in self.cursos.values() if codigo_estudiante in c.estudiantes_inscritos]

        if not cursos_encontrados:
            return f"El estudiante {estudiante.nombre} no esta inscrito en ningun curso."

        resultado = f"\n--- Cursos de {estudiante.nombre} ---\n"
        for c in cursos_encontrados:
            resultado += f"- [{c.codigo}] {c.nombre} (Prof. {c.profesor.nombre})\n"
        return resultado

    def consultar_estudiantes_de_curso(self, codigo_curso):
        if codigo_curso not in self.cursos:
            return "Error: El curso no existe en el sistema."

        curso = self.cursos[codigo_curso]
        if not curso.estudiantes_inscritos:
            return f"El curso '{curso.nombre}' no tiene estudiantes inscritos actualmente."

        resultado = f"\n--- Estudiantes inscritos en {curso.nombre} ---\n"
        for est in curso.estudiantes_inscritos.values():
            resultado += f"- {est}\n"
        return resultado


def pedir_codigo(mensaje):
    while True:
        codigo = input(mensaje).strip()
        if not codigo:
            print("Error: El campo no puede estar vacio.")
            continue
        if any(c.isalpha() or c.isspace() or not c.isalnum() for c in codigo):
            print("Error: Los codigos no pueden contener letras, espacios ni simbolos, unicamente numeros.")
            continue
        return codigo


def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if not texto:
            print("Error: El campo no puede estar vacio.")
            continue
        if any(c.isdigit() for c in texto):
            print("Error: Este campo no puede contener numeros.")
            continue
        if not all(x.isalpha() or x.isspace() for x in texto):
            print("Error: Este campo solo debe contener letras (sin simbolos especiales).")
            continue
        return texto


def pausar():
    input("\nPresione Enter para continuar...")


def main():
    sistema = SistemaCursos()

    while True:
        print("\n========================================")
        print("      GESTION DE CURSOS E INSCRIPCIONES ")
        print("========================================")
        print("1. Registrar curso (Asignar profesor)")
        print("2. Inscribir estudiante en curso")
        print("3. Consultar cursos de un estudiante")
        print("4. Consultar estudiantes inscritos en un curso")
        print("5. Salir")

        opcion = input("\nSeleccione una opcion (1-5): ").strip()

        if opcion == "1":
            print("\n--- Registrar Curso ---")
            cod_curso = pedir_codigo("Ingrese el codigo del curso (solo numeros): ")
            nom_curso = pedir_texto("Ingrese el nombre del curso (solo letras): ")
            cod_prof = pedir_codigo("Ingrese el codigo numerico del profesor responsable: ")
            print(sistema.registrar_curso(cod_curso, nom_curso, cod_prof))
            pausar()

        elif opcion == "2":
            print("\n--- Inscribir Estudiante en Curso ---")
            cod_est = pedir_codigo("Ingrese el codigo del estudiante: ")
            cod_cur = pedir_codigo("Ingrese el codigo del curso: ")
            print(sistema.inscribir_estudiante(cod_est, cod_cur))
            pausar()

        elif opcion == "3":
            print("\n--- Consultar Cursos de Estudiante ---")
            cod_est = pedir_codigo("Ingrese el codigo del estudiante: ")
            print(sistema.consultar_cursos_de_estudiante(cod_est))
            pausar()

        elif opcion == "4":
            print("\n--- Consultar Estudiantes de un Curso ---")
            cod_cur = pedir_codigo("Ingrese el codigo del curso: ")
            print(sistema.consultar_estudiantes_de_curso(cod_cur))
            pausar()

        elif opcion == "5":
            print("\nSaliendo del sistema...")
            break
        else:
            print("\nOpcion no valida. Ingrese un numero del 1 al 5.")
            pausar()


if __name__ == "__main__":
    main()