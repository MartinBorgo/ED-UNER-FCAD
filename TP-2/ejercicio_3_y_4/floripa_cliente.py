from clase_empleado import Empleado
from clase_marcacion import Marcacion, MarcacionTipo
from clase_oficina import Oficina
from clase_MarcacionesAdmin import MarcacionesAdmin
from datetime import time, datetime

empleado1 = Empleado(12, 23141341, "Gutierres", "Agustin", Oficina("contaduria", time(7), time(20)))
empleado2 = Empleado(1, 2314435345, "Gutierres", "Esteban", Oficina("compras", time(8), time(18)))
empleado3 = Empleado(112, 23675, "Fernandez", "Federico", Oficina("contaduria", time(7), time(20)))
empleado4 = Empleado(987, 231465341, "Blass", "Martin", Oficina("ventas", time(7), time(18)))
empleado5 = Empleado(104, 2314168, "Percara", "Olivia", Oficina("publicidad", time(9), time(20)))
empleado6 = Empleado(110, 231879671, "Smith", "Soledad", Oficina("administracion", time(7), time(19)))

# =============================== #

marcacion1 = Marcacion( empleado1, datetime(2022, 4, 12, 8), MarcacionTipo.ENTRADA)
marcacion2 = Marcacion( empleado2, datetime(2022, 3, 12, 9), MarcacionTipo.SALIDA)
marcacion3 = Marcacion( empleado3, datetime(2022, 10, 12, 8), MarcacionTipo.ENTRADA)
marcacion4 = Marcacion( empleado4, datetime(2022, 4, 12, 8), MarcacionTipo.ENTRADA)
marcacion5 = Marcacion( empleado5, datetime(2022, 2, 12, 8), MarcacionTipo.SALIDA)
marcacion6 = Marcacion( empleado6, datetime(2022, 6, 16, 8), MarcacionTipo.SALIDA)
marcacion7 = Marcacion( empleado3, datetime(2022, 1, 16, 8), MarcacionTipo.ENTRADA)
marcacion8 = Marcacion( empleado1, datetime(2022, 4, 12, 8), MarcacionTipo.SALIDA)
marcacion9 = Marcacion( empleado5, datetime(2022, 7, 15, 11), MarcacionTipo.ENTRADA)
marcacion10 = Marcacion( empleado2, datetime(2022, 4, 5, 8), MarcacionTipo.ENTRADA)
marcacion11 = Marcacion( empleado4, datetime(2022, 1, 3, 8), MarcacionTipo.SALIDA)
marcacion12 = Marcacion( empleado2, datetime(2022, 4, 10, 8), MarcacionTipo.ENTRADA)
marcacion13 = Marcacion( empleado5, datetime(2022, 4, 11, 8), MarcacionTipo.SALIDA)
marcacion14 = Marcacion( empleado3, datetime(2022, 4, 14, 8), MarcacionTipo.SALIDA)
marcacion15 = Marcacion( empleado3, datetime(2022, 4, 22, 8), MarcacionTipo.ENTRADA)
marcacion16 = Marcacion( empleado1, datetime(2022, 4, 13, 10), MarcacionTipo.ENTRADA)

# =============================== #

lista_marcaciones = MarcacionesAdmin()

lista_marcaciones.agregar(marcacion1)
lista_marcaciones.agregar(marcacion2)
lista_marcaciones.agregar(marcacion3)
lista_marcaciones.agregar(marcacion4)
lista_marcaciones.agregar(marcacion5)
lista_marcaciones.agregar(marcacion6)
lista_marcaciones.agregar(marcacion7)
lista_marcaciones.agregar(marcacion8)
lista_marcaciones.agregar(marcacion9)
lista_marcaciones.agregar(marcacion10)
lista_marcaciones.agregar(marcacion11)
lista_marcaciones.agregar(marcacion12)
lista_marcaciones.agregar(marcacion13)
lista_marcaciones.agregar(marcacion14)
lista_marcaciones.agregar(marcacion15)
lista_marcaciones.agregar(marcacion16)

# ===============Prueba de los metodos de la clase MarcacionesAdmin================ #

# este metodo lo hice para que se pueda ver mejor por pantalla
def imprimir(lista : list):
    for element in lista:
        print(element.__str__())

    print("# ============ #")

print("LISTA DE EMPLEADOS REGISTRADOS EN LAS MARCACIONES")
lista1 = lista_marcaciones.empleados()
imprimir(lista1)

print("FILTRADO POR EMPLEADO")
lista2 = lista_marcaciones.filtrar_por_empleado(empleado1)
imprimir(lista2)

print("FILTRADO POR TIPO")
lista3 = lista_marcaciones.filtrar_por_tipo(MarcacionTipo.ENTRADA)
imprimir(lista3)

print("LISTA DE PERSONAS QUE LLEGARON TARDE")
lista4 = lista_marcaciones.llegadas_tarde()
imprimir(lista4)

print("ORDENAR POR APELLIDO-NOMBRE-FECHA")
lista_marcaciones.ordenar_apellido_nombre()
imprimir(lista_marcaciones)

print("ORDEN POR LEGAJO-FECHA")
lista_marcaciones.ordenar_legajo()
imprimir(lista_marcaciones)

print("LONGITUD DE LA LISTA")
print(lista_marcaciones.__len__())

print("BORRAR UN ELEMENTO")
lista_marcaciones.__delitem__(2)
imprimir(lista_marcaciones)

print("LONGITUD CON EL ELEMENTO BORRADO DE LA LISTA")
print(lista_marcaciones.__len__())

print("DEVUELVE EL OBJETO DE LA POCISION INDICADA")
print(lista_marcaciones.__getitem__(5).__str__())
print("*"*30)

print("SE USA EL METODO __str__")
print(lista_marcaciones.__str__())