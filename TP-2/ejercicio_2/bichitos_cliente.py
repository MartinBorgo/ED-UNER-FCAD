from clase_persona import Persona
from clase_mascota import Mascota
from clase_raza import Raza
from clase_especie import Especie

def imprimir(lista_mascotas : list) -> None:
    for mascota in lista_mascotas:
        print(mascota.__str__())

    print("=========== O ===========")

def filtrar_geronte(lista_mascotas : list, anio_actual : int) -> list:
    lista_gerontes = []
    for mascota in lista_mascotas:
        if mascota.calcular_edad >= 13:
            lista_gerontes.append(mascota)

    return lista_gerontes

def filtrar_por_especie(lista_mascotas : list, especie : Especie) -> list:
    lista_especie = []
    for mascota in lista_mascotas:
        if mascota.raza.especie == especie:
            lista_especie.append(mascota)

    return lista_especie

def max_mascotero(lista_mascotas : list) -> Persona:
    contador = 0
    maximo = 0
    for mascota in lista_mascotas:
        persona = mascota.duenio
        for i in lista_mascotas:
            if persona == i.duenio:
                contador += 1
                aux_persona = persona

        if maximo < contador:
            maximo = contador
            mascotero = aux_persona
        
        contador = 0

    return mascotero


# =================== #

lista = []

mascota1 = Mascota(10, "Rockcy", Raza("galgo", Especie("perro")), 2021 , Persona("Ellen", "Rodrigo", 120120))
mascota2 = Mascota(10, "Michi", Raza("Tigre", Especie("gato")), 2010 , Persona("Ellen", "Rodrigo", 120120))
mascota3 = Mascota(10, "Toby", Raza("policia", Especie("perro")), 2003 , Persona("Ellen", "Rodrigo", 120120))
mascota4 = Mascota(10, "Roco", Raza("doguerman", Especie("perro")), 2002 , Persona("Prey", "Juan", 111000))
mascota5 = Mascota(10, "Cachito", Raza("carpincho", Especie("carpincho")), 2020 , Persona("Prey", "Juan", 111000))
mascota6 = Mascota(10, "Cachilo", Raza("galgo", Especie("perro")), 2019 , Persona("Sosa", "Eustaqui", 127789))
mascota7 = Mascota(10, "Colita", Raza("coli", Especie("perro")), 2021 , Persona("Rojas", "Nahuel", 123409))

lista.append(mascota1)
lista.append(mascota2)
lista.append(mascota3)
lista.append(mascota4)
lista.append(mascota5)
lista.append(mascota6)
lista.append(mascota7)

print("IMPRECION DE LA LISTA")
imprimir(lista)

print("LISTADO DE MASCOTAS DE 13 AÑOS O MAS")
filtro1 = filtrar_geronte(lista, 2022)
imprimir(filtro1)

print("LISTADO DE MASCOTAS FILTRADO POR ESPECIE")
filtro2 = filtrar_por_especie(lista, Especie("perro"))
imprimir(filtro2)

print("PERSONA CON MAYOR CANTIDAD DE MASCOTAS")
filtro3 = max_mascotero(lista)
print(filtro3.__str__())