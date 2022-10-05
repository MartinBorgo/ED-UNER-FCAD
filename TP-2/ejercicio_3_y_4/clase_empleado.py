from clase_oficina import Oficina

class Empleado():
    def __init__(self, legajo : int, dni : int, apellido : str, nombre : str, oficina : Oficina):
        self.legajo = legajo
        self.dni = dni
        self.apellido = apellido
        self.nombre = nombre
        self.oficina = oficina

    def __str__(self):
        return "Legajo: %d, DNI: %d, Apellido: %s, Nombre: %s, Oficina -> %s" %(self.legajo, self.dni, self.apellido, self.nombre, self.oficina.__str__())

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
       if isinstance(other, Empleado):
          return self.dni == other.dni

    def __lt__(self, other):
        if isinstance(other, Empleado):
            return self.legajo < other.legajo