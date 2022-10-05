class Persona():
    def __init__(self, apellido : str, nombre : str, documento: int):
        self.apellido = apellido
        self.nombre = nombre
        self.documento = documento

    def __str__(self):
        return "Apellido: %s, Nombre: %s, Documento: %d" %(self.apellido, self.nombre, self.documento)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, Persona):
            return self.documento == other.documento
