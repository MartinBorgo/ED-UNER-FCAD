from clase_especie import Especie

class Raza():
    def __init__(self, nombre : str, especie : Especie):
        self.nombre = nombre
        self.especie = especie

    def __str__(self):
        return "Nombre de raza -> %s, Especie -> %s" %(self.nombre, self.especie.__str__())

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, Raza):
            return self.nombre == other.nombre