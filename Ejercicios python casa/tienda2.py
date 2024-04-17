class Producto():
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
class Electrodomesticos(Producto):
    def __init__(self, codigo, nombre, precio, marca, modelo, consumo):
        super().__init__(codigo, nombre, precio)
        self.marca = marca
        self.modelo = modelo
        self.consumo = consumo
class Telefono(Producto):
    def __init__(self, codigo, nombre, precio, marca, modelo, sistema, ram, sistemainterno):
        super().__init__(codigo, nombre, precio)
        self.marca = marca
        self.modelo = modelo
        self.sistema = sistema
        self.ram = ram
        self.sistemainterno = sistemainterno
class Tablet(Producto):
    def __init__(self, codigo, nombre, precio, sistemaoperativo, tamaño, ram, memoria):
        super().__init__(codigo, nombre, precio)
        self.sistemaoperativo = sistemaoperativo
        self.tamaño = tamaño
        self.ram = ram
        self.memoria = memoria