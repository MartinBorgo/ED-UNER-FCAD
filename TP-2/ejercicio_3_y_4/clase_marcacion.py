from datetime import datetime
from clase_empleado import Empleado
from clase_marcacion_tipo import MarcacionTipo

class Marcacion():
    __numero_registro = 0

    def __init__(self, empleado: Empleado, fecha_hora: datetime, tipo: MarcacionTipo):
        self.__num_registro = self.__class__.__numero_registro
        self.empleado = empleado
        self.fecha_hora = fecha_hora
        self.tipo = tipo

        self.__class__.__numero_registro += 1

    @property
    def num_registro(self):
        return self.__num_registro

    @num_registro.setter
    def num_registro(self, numero):
        raise Exception("No se puede modificar esta variable")

    @property
    def llega_tarde(self):
        if self.tipo == MarcacionTipo.ENTRADA:
            if self.fecha_hora.time() > self.empleado.oficina.hora_entrada:
                return True
            else:
                return False

    def __str__(self):
        return "Numero de Registro: %s, Empleado -> %s, Fecha y Hora: %s, Tipo: %s" %(self.num_registro, self.empleado.__str__(), self.fecha_hora, self.tipo)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, Marcacion):
            return self.empleado == other.empleado

