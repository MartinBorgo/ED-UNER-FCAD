from datetime import time

class Oficina():

        def __init__(self, nombre: str, hora_entrada: time, hora_salida: time):
                self.nombre = nombre
                self.hora_entrada = hora_entrada
                self.hora_salida = hora_salida

        def __str__(self):
            return "Nombre: %s, Hora de entrada: %s, Hora de salida: %s" %(self.nombre, self.hora_entrada, self.hora_salida)

        def __repr__(self):
            return self.__str__()

        def __eq__(self, other):
                if isinstance(other, Oficina):
                        return self.nombre == other.nombre