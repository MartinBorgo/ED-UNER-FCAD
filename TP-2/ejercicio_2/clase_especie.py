class Especie():
    def __init__(self, nombre : str):
        self.nombre = nombre

    def __str__(self):
        return "Nombre de especie: %s" %(self.nombre)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, Especie):
            return self.nombre == other.nombre