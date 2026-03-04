class Autor():
    
    #constructor
    def __init__(self,nombre,nacionalidad):
        self.nombre=nombre
        self.nacionalidad=nacionalidad
        
class libro():
    #constructor 
    def __init__(self,titulo,genero,autor):
        self.titulo=titulo
        self.genero=genero
        self.autor=autor
        
class biblioteca():
    def __init__(self,nombre):
        self.nombre=nombre
        self.libros=[]
        
    def registrarlibro(self,libro):
        self.libros.append(libro)
        
class usuario():
    def __init__(self,identificacion,nombre,correo):
        self.identificacion=identificacion
        self.nombre=nombre
        self.correo=correo
        
class estudiante(usuario):
    def __init__(self,icfes , identificacion, nombre, correo):
        super().__init__(identificacion, nombre, correo)
        self.icfes=icfes
        
class docente (usuario):
    def __init__(self, especialidad , identificacion, nombre, correo):
        super().__init__(identificacion, nombre, correo)
        self.especialidad=especialidad
        
class prestamo():
    def __init__(self,fechaprestamo, fechadevolucion):
        self.fechaprestamo=fechaprestamo
        self.fechadevolucion=fechadevolucion
        self.usuario=None
        self.librosprestamo=[]
        
    def registrarprestamo(self,libro,usuario):
        self.usuario=usuario
        self.librosprestamo.append(libro)
        
                