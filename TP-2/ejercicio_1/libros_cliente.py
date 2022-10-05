from clases_libro import Libro
from clase_autor import Autor
from clase_categoria import Categoria

def imprimir(lista_libros : list) -> None:
    for libro in lista_libros:
        print(libro.__str__())

    print("=========== O ===========")


def filtrar_por_categoria(lista_libros : list, cat : Categoria) -> list:
    lista_categoria = []
    for libro in lista_libros:
        if libro.categoria.nombre == cat.nombre:
            lista_categoria.append(libro)

    return lista_categoria

def filtrar_por_autor(lista_libros : list, autor : Autor) -> list:
    lista_autor = []
    for libro in lista_libros:
        if libro.autor.nombre == autor.nombre and libro.autor.apellido == autor.apellido:
            lista_autor.append(libro)

    return lista_autor

def filtrat_por_anio(lista_libros : list, anio : int) -> list:
    lista_anio = []
    for libro in lista_libros:
        if libro.anio_publicacion == anio:
            lista_anio.append(libro)

    return lista_anio

lista = []

libro1 = Libro(10, "analisis matematico", "carlos", "stuward", "matematicas", 2016)
libro2 = Libro(3, "termodinamica", "albert", "heinstain", "fisica", 2002)
libro3 = Libro(40, "caos y orden", "antonio", "escohotado", "filosofia", 2010)
libro4 = Libro(2, "relidad y substancia", "antonio", "escohotado", "filosofia", 2002)

lista.append(libro1)
lista.append(libro2)
lista.append(libro3)
lista.append(libro4)

print("IMPRIME LA LISTA")
imprimir(lista)

print("FILTRAR POR AUTOR")
autor = Autor("escohotado", "antonio")
lista_obra_por_autor = filtrar_por_autor(lista, autor)
imprimir(lista_obra_por_autor)

print("FILTRAR POR CATEGORIA")
categoria = Categoria("fisica")
lista_por_categoria = filtrar_por_categoria(lista, categoria)
imprimir(lista_por_categoria)

print("FILTRAR POR AÑO")
lista_por_anio = filtrat_por_anio(lista, 2002)
imprimir(lista_por_anio)