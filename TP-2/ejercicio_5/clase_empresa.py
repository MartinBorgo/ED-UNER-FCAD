class Empresa():
    def __init__(self, nombre: str):
        self.nombre = nombre

    def __str__(self):
        return "Nombre empresa: %s" %(self.nombre)

    def __repr__(self):
        return "Este objeto es de la clase {}".format(self.__class__.__name__)

    def __eq__(self, other):
        if isinstance(other, Empresa):
            return self.nombre == other.nombre