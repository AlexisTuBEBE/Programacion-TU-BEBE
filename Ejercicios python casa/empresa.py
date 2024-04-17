class Empleado():
    def __init__(self, nombre, apellido, salario, antiguedad):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario
        self.antiguedad = antiguedad
    def imprimir(self):
        print("Nombre:",self.nombre,
              "\nApellido:",self.apellido,
              "\nSalario $:",self.salario,
              "\nAntiguedad:",self.antiguedad)
class Gerente(Empleado):
    def __init__(self, nombre, apellido, salario, antiguedad, departamento):
        super().__init__(nombre, apellido, salario, antiguedad)
        self.departamento = departamento
    def bono_anual(self):
        if self.antiguedad > 5:
            return self.salario * 0.10
        else:
            return "Sin bono"
    def total(self):
        return self.salario + self.bono_anual()
    def informe1(self):
        print("\nDepartamento:",self.departamento,
              "\nBono anual:",self.bono_anual(),
              "\nTotal: ",self.total()
              )
        
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
salario = int(input("Ingrese su salario $: "))
antiguedad = int(input("Ingrese su antiguedad: "))
departamento = input("Ingrese su departamento: ")
a1 = Gerente(nombre, apellido, salario, antiguedad, departamento)
a1.imprimir()
a1.informe1()
    
class Analista(Empleado):
    def __init__(self, nombre, apellido, salario, antiguedad, proyecto):
        super().__init__(nombre, apellido, salario, antiguedad)
        self.proyecto = proyecto
        
    def asignacion(self):
        if self.proyecto == "":
            return "Sin proyecto"
        else:
            return "Asignado a un proyecto"
            
    def informe2(self):
        print("Proyecto:", self.asignacion())

        
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
salario = int(input("Ingrese su salario $: "))
antiguedad = int(input("Ingrese su antiguedad: "))
proyecto = input("Ingrese su proyecto: ")
a2 = Analista(nombre, apellido, salario, antiguedad, proyecto)
a2.imprimir()
a2.informe2()