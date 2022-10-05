from clase_genero import Genero
from clase_plataforma import Plataforma
from clase_empresa import Empresa
from clase_videojuego import VideoJuego
from clase_VideojuegoAdmin import VideoJuegoAdmin
from datetime import datetime

v1 = VideoJuego("assassins creed", Genero.ACCION_AVENTURA, [Plataforma("PC", False), Plataforma("xbox", True), Plataforma("playstation", True)], "esta bien el jueguito", 33.99, Empresa("Ubisoft"), Empresa("Ubisoft"), datetime(2004, 5, 20), 8.65)
v2 = VideoJuego("enter the gungeon", Genero.OTRO, [Plataforma("PC", False), Plataforma("switch", True), Plataforma("playstation", True)], "mejor dungeon crowler", 5.99, Empresa("Dodge Roll"), Empresa("Devolver Digital"), datetime(2016, 7, 14), 9.00)
v3 = VideoJuego("dark souls", Genero.ACCION_AVENTURA, [Plataforma("PC", False), Plataforma("xbox", True), Plataforma("playstation", True)], "te quiero miyasaki", 30, Empresa("From Software"), Empresa("From Software"), datetime(2016, 9, 10), 8.95)
v4 = VideoJuego("albion online", Genero.RPG, [Plataforma("PC", False), Plataforma("xbox", True), Plataforma("playstation", True), Plataforma("movil", True)], "si te gusta farmear es para vos", 0, Empresa("SandBox Games"), Empresa("SandBox Games"), datetime(2015, 5, 20), 6.22)
v5 = VideoJuego("dota 2", Genero.OTRO, [Plataforma("PC", False)], "el primer moba de todos", 0, Empresa("Valve"), Empresa("Valve"), datetime(2009, 1, 16), 7.98)
v6 = VideoJuego("assassins creed origin", Genero.ACCION_AVENTURA, [Plataforma("PC", False), Plataforma("xbox", True), Plataforma("playstation", True)], "esta bien el jueguito", 60.00, Empresa("Ubisoft"), Empresa("Ubisoft"), datetime(2021, 5, 20), 7.26)

# ================================ #

lista = VideoJuegoAdmin()

lista.agregar(v1)
lista.agregar(v2)
lista.agregar(v3)
lista.agregar(v4)
lista.agregar(v5)
lista.agregar(v6)

# ================================= #

# Este metodo lo cree porque a la hora de usar el str algunas cosas no se mostraban como tenian que ser
# intente corregirlo de muchas formas pero sino me saltaba error
def imprimir(lista : list):
    for element in lista:
        print(element.__str__())

    print("# ============ #")

print("USO DEL METODO __str__")
print(lista.__str__())

print("LISTA DE VIDEOJUEGOS FILTRADO POR DESARROLLADORA")
lista1 = lista.filtrar_por_desarrolladora(Empresa("Ubisoft"))
imprimir(lista1)

print("LISTA DE VIDEOJUEGOS FILTRADO POR DISTRIBUIDORA")
lista2 = lista.filtrar_por_distribuidora(Empresa("Valve"))
imprimir(lista2)

print("LISTA DE VIDEOJUEGOS FILTRADA POR GENERO")
lista3 = lista.filtrar_por_genero(Genero.ACCION_AVENTURA)
imprimir(lista3)

print("CANTIDAD DE JUEGOS PARA CADA PLATAFORMA")
lista4 = lista.cantidad_por_plataforma()
imprimir(lista4)

print("LISTA DE VIDEOJUEGOS ORDENADO POR RANKING (DESCENDENTE)")
lista.ordenar_mejores_primero()
print(lista.__str__())

print("LISTA DE VIDEOJUEGOS ORDENADOS POR TITULO")
lista.ordenar_titulo()
print(lista.__str__())

print("USO METODO __len__")
print(lista.__len__())

print("USO METODO __getitem__")
print(lista.__getitem__(3).__str__())

print("USO METODO __delitem__")
lista.__delitem__(5)
print("LONGITUD CON EL ELEMENTO BORRADO")
print(lista.__len__())