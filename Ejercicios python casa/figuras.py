import math


class Figurageometrica:
    
    def __init__(self, tipo, color):
        self.tipo = tipo
        self.color = color
        
    def imprimir(self):
        print("Tipo:",self.tipo,
              "\n","Color:",self.color)
        
class Rectangulo(Figurageometrica):
    
    def __init__(self, tipo, color, base, altura):
        super().__init__(tipo, color)
        
        self.base = base
        self.altura = altura
        
    def areaR(self):
        return self.base * self.altura
    
    def perimetroR(self):
        return (self.base * 2 ) + (self.altura * 2 )
    
    def imprimirR(self):
        print("Area:",self.areaR(),
              "\n","Perimetro:",self.perimetroR()
              )
        
tipo = input("Ingrese el tipo de figura: ")
color = input("Ingrese el color: ")
base = int(input("Ingrese la base: "))
altura = int(input("Ingrese la altura: "))

Rectangulo1 = Rectangulo(tipo, color, base, altura)
Rectangulo1.imprimir()
Rectangulo1.imprimirR()

class Circulo(Figurageometrica):
        
    def __init__(self, tipo, color, atributos, radio):
        super().__init__(tipo, color)
        
        self.atributos = atributos
        self.radio = radio
        
    def area(self):
        return (math.pi * self.radio ) ** 2
    
    def perimetro(self):
        return (math.pi * 2 ) * self.radio
    
    def imprimirC(self):
        print("Area:",self.area(),
              "\n","Perimetro",self.perimetro())

tipo = input("Ingrese el tipo de figura: ")
color = input("Ingrese el color: ")
atributos = int(input("Ingrese los atributos: "))
radio = int(input("Ingrese el radio: "))

Circulo1 = Circulo(tipo, color, atributos, radio)
Circulo1.imprimir()
Circulo1.imprimirC()