class Plataforma():
    def __init__(self, nombre: str, es_portatil: bool):
        self.nombre = nombre
        self.es_portatil = es_portatil

    def __str__(self):
        return "Nombre: %s, Portatil: %b" %(self.nombre, self.es_portatil)

    def __repr__(self):
        return "Nombre: {}".format(self.nombre)

    def __eq__(self, other):
        if isinstance(other, Plataforma):
            return self.nombre == other.nombre