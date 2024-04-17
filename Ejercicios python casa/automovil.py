class Vehiculo:
    
    def __init__(self, marca, modelo, anio, precio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio 
        self.precio = precio
        
    def imprimir(self):
        print("Marca:",self.marca,
              "\n","Modelo:",self.modelo,
              "\n","Año:",self.anio,
              "\n","Precio:",self.precio)
        
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, anio, precio, color, puertas):
        super().__init__(marca, modelo, anio, precio)
        self.color = color
        self.puertas = puertas
        
    def impuesto(self):
        return self.precio * 0.10
    
    def descuento(self):
        return (self.precio + self.impuesto()) * 0.05
    
    def preciototal(self):
        return self.precio + self.impuesto() + self.descuento()
    
    def informe(self):
        print("Color:", self.color,
              "\n","Numero de puertas:",self.puertas,
              "\n","Impuesto:",self.impuesto(),
              "\n","Descuento:",self.descuento(),
              "\n","Precio total:",self.preciototal())
        
marca = input("Ingrese la marca: ")
modelo = input("Ingrese el modelo del auto: ")
anio = int(input("Ingrese el año de fabricacion: "))
precio = int(input("Ingrese el precio del auto $: "))
color = input("Ingrese el color del auto: ")
puertas = int(input("Ingrese el numero de puertas: "))

carro = Automovil(marca, modelo, anio, precio, color, puertas)
carro.imprimir()
carro.informe()

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, precio, cilindrada, tipo):
        super().__init__(marca, modelo, anio, precio)
        
        self.cilindrada = cilindrada
        self.tipo = tipo
        
    def cilindradaM(self):
        if self.cilindrada <= 500:
            return 0.05
        elif 700 >= self.cilindrada:
            return 0.07
        
    def impuestoM(self):
        return self.precio * self.cilindradaM()
    
    def precioneto(self):
        return self.precio + self.impuestoM()
    
    def informeM(self):
        print("Cilindrada:",self.cilindrada,
              "\n","Tipo:",self.tipo,
              "\n","Impuesto:",self.impuestoM(),
              "\n","Precio Neto $:",self.precioneto())
        
marca = input("Ingrese la marca: ")
modelo = input("Ingrese el modelo del auto: ")
anio = int(input("Ingrese el año de fabricacion: "))
precio = int(input("Ingrese el precio del auto $: "))
cilindrada = int(input("Ingrese el numero de cilindrada: "))
tipo = input("Ingrese el tipo de motocicleta: ")

moto = Motocicleta(marca, modelo, anio, precio, cilindrada, tipo)
moto.imprimir()
moto.informeM()