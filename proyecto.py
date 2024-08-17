class Libro: 
    def __init__(self, titulo, autor, genero, año):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.año = año
        self.prestado = False

    def prestar(self):
        self.prestado = True
    
    def devolver(self): 
        self.prestado = False
    
    def __str__(self):
        if self.prestado == True:
            estado = "Prestado"

        else:
            estado = "Disponible"

        return f"{self.titulo} de {self.autor} ({self.año}) - Genero: {self.genero} - Estado: {estado}"

class Biblioteca:
    def __init__(self):
        self.libros = []
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
    
    def eliminar_libro(self, titulo):
        nueva_lista_libros = [] 
        for libro in self.libros:
            if libro.titulo != titulo:
                nueva_lista_libros.append(libro)
        self.libros = nueva_lista_libros
    
    def buscar_por_titulo(self, titulo):
        libros_encontrados = []
        for libro in self.libros: 
            if libro.titulo == titulo:
                libros_encontrados.append(libro)
        return libros_encontrados
    
    def buscar_por_autor(self, autor):
        autor_encontrados = []
        for nombre in self.libros: 
            if nombre.autor == autor:
                autor_encontrados.append(nombre)
        return autor_encontrados
    
    def buscar_por_genero(self, genero):
        generos_encontrados = []
        for nombre in self.libros: 
            if nombre.genero == nombre:
                generos_encontrados.append(genero)
        return generos_encontrados
    
    def listar_libros(self):
        return self.libros
    
    def guardar_datos(self, archivo):
        with open(archivo, "w") as f:
            for libro in self.libros:
                f.write(f"{libro.titulo}, {libro.autor}, {libro.genero}, {libro. año}, {libro.prestado}")


def mostrar_menu():
    print(" 1. Agregar libro \n 2. Eliminar libro \n 3. Buscar libro por titulo \n 4. Buscar libro por autor \n 5. Buscar libro por genero \n 6. Listar todos los libros \n 7. Prestar libro \n 8. Devolver libro \n 9. Guardar y salir")


biblioteca = Biblioteca()

while True:
    mostrar_menu()
    opcion = input("Ingrese una opcion:")

    if opcion == "1":
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        genero = input("Genero: ")
        año = int(input("Año: "))
        libro = Libro(titulo, autor, genero, año)
        biblioteca.agregar_libro(libro)

    elif opcion == "2":
        titulo = input("Titulo del Libro a eliminar: ")
        biblioteca.eliminar_libro(titulo)
    
    elif opcion == "3":
        titulo = input("Titulo del Libro a buscar: ")
        libros = biblioteca.buscar_por_titulo(titulo)
        for libro in libros:
                print(libro)

    elif opcion == "4":
        autor = input("Autor del Libro a buscar: ")
        libros = biblioteca.buscar_por_autor(autor)
        for libro in libros:
                print(libros)

    elif opcion == "5":
        autor = input("Genero del Libro a buscar: ")
        libros = biblioteca.buscar_por_genero(autor)
        for libro in libros:
                print(libro)

    elif opcion == "6":
        libros = biblioteca.listar_libros()
        for libro in libros:
            print(libro)

    elif opcion == "7":
        titulo = input("Titulo del libro a prestar: ")
        resultados = biblioteca.buscar_por_titulo(titulo)
        if resultados:
            resultados[0].prestar()
            print(f"El libro {titulo} ha sido prestado")
        else:
            print(f"No se encontro el libro {titulo}")
    
    elif opcion == "8":
        titulo = input("Titulo del libro a devolver: ")
        resultados = biblioteca.buscar_por_titulo(titulo)
        if resultados:
            resultados[0].devolver()
            print(f"El libro {titulo} ha sido devuelto")
        else:
            print(f"No se encontro el libro {titulo}")