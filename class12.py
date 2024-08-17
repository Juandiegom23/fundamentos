class Curso:
    def __init__(self, nombre_curso):
        self.nombre_curso = nombre_curso
        self.estudiantes = []
        self.notas = {}

    def agregar_estudiante(self, nombre_estudiante):
        if nombre_estudiante not in self.estudiantes:
            self.estudiantes.append(nombre_estudiante)
            self.notas[nombre_estudiante] = []
            print(f"El estudiante {nombre_estudiante} ha sido agregado al curso {self.nombre_curso}.")
        else:
            print(f"El estudiante {nombre_estudiante} ya está en el curso.")

    def asignar_nota(self, nombre_estudiante, nota):
        if nombre_estudiante in self.estudiantes:
            self.notas[nombre_estudiante].append(nota)
            print(f"La nota {nota} fue asignada al estudiante {nombre_estudiante}.")
        else:
            print("El estudiante no está en el curso")

    def promedio_estudiante(self, nombre_estudiante):
        if nombre_estudiante in self.estudiantes:
            notas = self.notas[nombre_estudiante]
            if notas:
                promedio = sum(notas) / len(notas)
                return promedio
            else:
                print(f"El estudiante {nombre_estudiante} no tiene notas asignadas.")
                return None
        else:
            print(f"El estudiante {nombre_estudiante} no está en el curso.")
            return None

    def lista_estudiantes(self):
        for estudiante in self.estudiantes:
            promedio = self.promedio_estudiante(estudiante)
            notas = self.notas[estudiante]
            print(f"Estudiante: {estudiante}, Notas: {notas}, Promedio: {promedio:.2f}")


# Ejemplo de uso
curso = Curso("Matemáticas")

# Agregar estudiantes
curso.agregar_estudiante("Juan")
curso.agregar_estudiante("Pablo")

# Asignar notas
curso.asignar_nota("Juan", 80)
curso.asignar_nota("Juan", 50)
curso.asignar_nota("Pablo", 90)
curso.asignar_nota("Pablo", 10)

# Calcular promedios
print(f"Promedio de Juan = {curso.promedio_estudiante('Juan'):.2f}")

# Listar estudiantes
curso.lista_estudiantes()

