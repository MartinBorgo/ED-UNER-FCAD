
class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return "Nombre de categoria: %s" %(self.nombre)

    def __eq__(self, otro):
        if isinstance(otro, Categoria):
            return self.__nombre == otro.nombre
        else:
            print("Este objeto no es una instancia de la clase Categoria")