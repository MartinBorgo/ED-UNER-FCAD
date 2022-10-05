from clase_raza import Raza
from clase_persona import Persona

class Mascota():
    ANIO_ACTUAL = 2022

    def __init__(self, num_registro : int, nombre : int, raza : Raza, anio_nacimiento : int, duenio : Persona):
        self.num_registro = num_registro
        self.nombre = nombre
        self.raza = raza
        self.anio_nacimiento = anio_nacimiento
        self.duenio = duenio

    @property
    def calcular_edad(self):
        return self.__class__.ANIO_ACTUAL - self.anio_nacimiento

    def __str__(self):
        return "Numero de registro: %d, Nombre: %s, Raza: %s, Año de naciemiento: %d, Dueño: %s" %(self.num_registro, self.nombre, self.raza.__str__(), self.anio_nacimiento, self.duenio.__str__())

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, Mascota):
            return self.raza == other.raza

