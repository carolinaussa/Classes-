from clases import *
from datetime import datetime as dt, timedelta

mibiblioteca = biblioteca ("SENA-CTPI")

autor1 = Autor("Gabriel Garcia Marquez", "Colombiano")
autor2 = Autor("Jose Eustacio Rivera", "Colombiano")

libro1 = libro("Cien Años de Soledad","Novela", autor1)

print(f"Libro: {libro1.titulo}")
print(f"autor: {libro1.autor.nombre}")
print(f"Nacionalidad Autor: {libro1.autor.nacionalidad}")

mibiblioteca.registrarlibro(libro1)

autor3 = Autor("Robert Greene","Estadounidense")
libro2 = libro ("las cuarentayocho leyes del poder","economia", autor3)

mibiblioteca.registrarlibro(libro2)

print("lista de libros de la biblioteca")
for libro in mibiblioteca.libros:
    print(f"titulo Libro: {libro.titulo}")
    print(f"autor: {libro.autor.nombre}")
    print ("*"*20)
    
docente1 = docente("software",11, "Pablo Rojas", "projas@sena.edu.co")
estudiante1 = estudiante(290,12,"Juan Lozano", "jlozano@gmail.com")

fechahoy = dt.now() # fecha actual
print(fechaprestamo)

dias_prestamo= timedelta(days=5)
fechadevolucion = fechaprestamo + dias_prestamo
print(fechadevolucion)
prestamo1 = prestamo(fechaprestamo,fechadevolucion)
prestamo1.registrarprestamo(libro1,estudiante1)

