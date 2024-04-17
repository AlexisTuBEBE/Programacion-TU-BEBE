class Animal:
    def __init__(self, nombre, edad, especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        
    def imprimir(self):
        print("Nombre:",self.nombre,
              "\n","Edad:",self.edad,
              "\n","Especie:",self.especie)
        
class Perro(Animal):
    def __init__(self, nombre, edad, especie, raza, tamanio):
        super().__init__(nombre, edad, especie)
        self.raza = raza
        self.tamanio = tamanio
        
    def edadH(self):
        return self.edad * 0.7
    
    def edadtotalP(self):
        return self.edadH() + self.edad
    
    def ladrido(self):
        print("El perro ladra")
        
    def imprimirP(self):
        print("Raza:",self.raza,
              "\n","Tamaño cm :",self.tamanio,
              "\n","Edad Humana:",self.edadtotalP()
              )
        
nombre = input("Ingrese el nombre: ")
edad = int(input("Ingrese la edad: "))
especie = input("Ingrese la especie: ")
raza = input("Ingrese la Raza: ")
tamanio = input("Ingrese su tamaño en cm: ")

perro1 = Perro(nombre, edad, especie, raza, tamanio)
perro1.ladrido()
perro1.imprimirP()

class Gato(Animal):
    
    def __init__(self, nombre, edad, especie, color, comportamiento):
        super().__init__(nombre, edad, especie)
        self.color = color
        self.comportamiento = comportamiento
        
    def edadHG(self):
        return self.edad * 0.05
    
    def edadtotalG(self):
        return self.edad + self.edadHG()
    
    def maullido(self):
        print("El Gato Maulla")
        
    def imprimirG(self):
        print("Color:",self.color,
              "\n","Comportamiento:",self.comportamiento,
              "\n","Edad Humana",self.edadtotalG()
              )
        
nombre = input("Ingrese el nombre: ")
edad = int(input("Ingrese la edad: "))
especie = input("Ingrese la especie: ")
color = input("Ingrese el color: ")
comportamiento = input("Ingrese el comportamiento: ")

gato1 = Gato(nombre, edad, especie, color, comportamiento)
gato1.maullido()
gato1.imprimirG