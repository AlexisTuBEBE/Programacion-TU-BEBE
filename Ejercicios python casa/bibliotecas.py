import datetime

class Biblioteca:  # Corrección en el nombre de la clase

    def __init__(self, titulo, autor, fecha):
        self.titulo = titulo
        self.autor = autor
        self.fecha = fecha  # Corrección en el nombre del atributo

class Libro(Biblioteca):

    def __init__(self, titulo, autor, fecha, editorial, numero):
        super().__init__(titulo, autor, fecha)
        self.editorial = editorial
        self.numero = numero

    def informacion(self):
        print("Editorial:", self.editorial,
              "\nNumero de paginas:", self.numero)

titulo = input("Ingrese el titulo: ")
autor = input("Ingrese al autor: ")
fecha = datetime.date(int(input("Ingrese el año: ")), int(input("Ingrese el mes: ")), int(input("Ingrese el día: ")))
editorial = input("Ingrese la editorial: ")
numero = int(input("Numero de paginas: "))

libro1 = Libro(titulo, autor, fecha, editorial, numero)
libro1.informacion()

class Revista(Biblioteca):

    def __init__(self, titulo, autor, fecha, nombre, edicion):
        super().__init__(titulo, autor, fecha)
        self.nombre = nombre
        self.edicion = edicion

    def informacion2(self):
        print("Nombre:", self.nombre,
              "\nEdicion:", self.edicion)

titulo = input("Ingrese el titulo: ")
autor = input("Ingrese al autor: ")
fecha = datetime.date(int(input("Ingrese el año: ")), int(input("Ingrese el mes: ")), int(input("Ingrese el día: ")))
nombre = input("Nombre de la revista: ")
edicion = int(input("Numero de edicion: "))

revista1 = Revista(titulo, autor, fecha, nombre, edicion)
revista1.informacion2()
