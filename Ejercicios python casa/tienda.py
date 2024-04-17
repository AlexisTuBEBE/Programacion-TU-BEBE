import datetime

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def imprimir(self):
        print("Nombre:", self.nombre,
              "\nPrecio:", self.precio,
              "\nCantidad:", self.cantidad)

class Comestible(Producto):
    def __init__(self, nombre, precio, cantidad, fecha_caducidad):
        super().__init__(nombre, precio, cantidad)
        self.fecha_caducidad = fecha_caducidad

    def verificar_vencimiento(self):
        fecha_actual = datetime.date.today()
        if self.fecha_caducidad < fecha_actual:
            print("El producto '{}' está vencido.".format(self.nombre))
        else:
            print("El producto '{}' no está vencido.".format(self.nombre))

nombre = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad en stock: "))
fecha_caducidad = input("Ingrese la fecha de caducidad (YYYY-MM-DD): ")

comestible = Comestible(nombre, precio, cantidad, datetime.datetime.strptime(fecha_caducidad, "%Y-%m-%d").date())
comestible.imprimir()
comestible.verificar_vencimiento()
