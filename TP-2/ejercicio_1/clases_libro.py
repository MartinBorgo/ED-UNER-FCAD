from clase_autor import Autor
from clase_categoria import Categoria

class Libro:
    def __init__(self, num_inventario, titulo, nombre, apellido, nombre_categoria, anio_publicacion):
        self.num_inventario = num_inventario
        self.titulo = titulo
        self.autor = Autor(apellido, nombre)
        self.categoria = Categoria(nombre_categoria)
        self.anio_publicacion = anio_publicacion

    def __str__(self):
        return "Numero de inventario -> %d, Titulo -> %s, Autor -> %s, Categoria -> %s, Año de publicacion -> %d" %(self.num_inventario, self.titulo, self.autor.__str__(), self.categoria.__str__(), self.anio_publicacion)

    def __eq__(self, otro):
        if isinstance(otro, Libro):
            return self.num_inventario == otro.num_inventario
        else:
            print("El objeto que desea comparar no pertenece a una istancia de Libro")

# -------- 0 ---------
