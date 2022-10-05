from claseAbstracta_MarcacionesAdmin import MarcacionesAdminAbstract
from clase_marcacion import Marcacion, MarcacionTipo
from clase_empleado import Empleado

class MarcacionesAdmin(MarcacionesAdminAbstract):
    
    def agregar(self, marcacion : Marcacion):
        self.marcaciones.append(marcacion)

    def empleados(self) -> list:
        lista_empleados = []
        for element in self.marcaciones:
            if element.empleado in lista_empleados:
                pass
            else:
                lista_empleados.append(element.empleado)

        return lista_empleados

    def filtrar_por_empleado(self, empleado : Empleado):
        lista_empleados = []
        for element in self.marcaciones:
            if element.empleado == empleado:
                lista_empleados.append(element)
        
        return lista_empleados

    def filtrar_por_tipo(self, tipo : MarcacionTipo):
        lista_tipo = []
        for element in self.marcaciones:
            if element.tipo == tipo:
                lista_tipo.append(element)

        return lista_tipo

    def llegadas_tarde(self):
        lista_tarde = []
        for marcacion in self.marcaciones:
            if marcacion.llega_tarde:
                lista_tarde.append(marcacion)

        return lista_tarde
   

    def ordenar_legajo(self):
        self.marcaciones = sorted(self.marcaciones, key = lambda x : (x.empleado.legajo, x.fecha_hora))

    def ordenar_apellido_nombre(self):
        self.marcaciones = sorted(self.marcaciones, key = lambda x : (x.empleado.apellido, x.empleado.nombre, x.fecha_hora))