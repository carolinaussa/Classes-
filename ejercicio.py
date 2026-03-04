
class Contrato:
    def __init__(self, tipo, fecha_inicio, fecha_fin):
        self.tipo = tipo
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def mostrar_contrato(self):
        return f"Tipo: {self.tipo}, Inicio: {self.fecha_inicio}, Fin: {self.fecha_fin}"



class Empleado:
    def __init__(self, nombre, cedula, salario, contrato):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__salario = salario
        self.contrato = contrato

    # Encapsulamiento 
    def get_nombre(self):
        return self.__nombre

    def get_salario(self):
        return self.__salario

    def set_salario(self, nuevo_salario):
        self.__salario = nuevo_salario

    # Método p
    def calcular_pago(self):
        return self.__salario


# 
class Administrativo(Empleado):
    def calcular_pago(self):
        return self.get_salario() + 500000  # Bono administrativo


# 
class Operativo(Empleado):
    def calcular_pago(self):
        return self.get_salario() + 200000  # Horas extra


# 
class Departamento:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def mostrar_empleados(self):
        for emp in self.empleados:
            print(emp.get_nombre())


# 
class Empresa:
    def __init__(self, nombre, nit, direccion):
        self.nombre = nombre
        self.nit = nit
        self.direccion = direccion
        self.departamentos = []

    def agregar_departamento(self, departamento):
        self.departamentos.append(departamento)

    def mostrar_departamentos(self):
        for dep in self.departamentos:
            print(dep.nombre)






contrato1 = Contrato("Indefinido", "01-01-2024", "No aplica")

emp1 = Administrativo("Carolina", "45678", 2000000, contrato1)
emp2 = Operativo("Julian", "78543", 1500000, contrato1)

dep1 = Departamento("Recursos Humanos", "RH01")
dep1.agregar_empleado(emp1)
dep1.agregar_empleado(emp2)

empresa = Empresa("Mi Empresa SAS", "800524154", "Popayan")
empresa.agregar_departamento(dep1)

print("Pago Administrativo:", emp1.calcular_pago())
print("Pago Operativo:", emp2.calcular_pago())