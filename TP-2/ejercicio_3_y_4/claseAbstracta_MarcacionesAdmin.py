from abc import ABC, abstractmethod
from clase_empleado import Empleado
from clase_marcacion import Marcacion

class MarcacionesAdminAbstract(ABC):
    def __init__(self) -> None:
        self.marcaciones = []

    def __len__(self) -> int:
        """Indica la cantidad de marcaciones almacenadas.
        Returns:
        int: cantidad de elementos almacenados actualmente en marcaciones."""
        return len(self.marcaciones)

    def __getitem__(self, key: int) -> Marcacion:
        """Obtiene el elemento en la posición indicada por key."""
        return self.marcaciones[key]

    def __delitem__(self, key: int) -> None:
        """Elimina la marcación ubicada en la posición indicada por key."""
        del self.marcaciones[key]

    def __str__(self) -> str:
        res = ""
        for elem in self.marcaciones:
            res += "{elem}\n".format(elem=str(elem))
        return res

    @abstractmethod
    def agregar(self, marcacion : Marcacion) -> None:
        """Agrega la marcación pasada por parámetro al final de la lista de marcaciones
        Args:
        marcacion (Marcacion): instancia de clase marcación que se
        va a agregar al final de la lista de marcaciones."""
        pass

    @abstractmethod
    def empleados(self) -> list:
        """Devuelve todos los empleados de los que se tiene registro de marcación(no repetir
        resultados).
        Returns:
        list: lista formada por las ocurrencias únicas de
        empleados dentro de la lista de marcaciones"""
        pass

    @abstractmethod
    def filtrar_por_empleado(self, empleado: Empleado) -> list:
        """Devuelve todas las marcaciones de un empleado."""
        pass

    @abstractmethod
    def filtrar_por_tipo(self, tipo: Marcacion) -> list:
        """Devuelve todas las marcaciones del tipo especificado por parámetro."""
        pass

    @abstractmethod
    def llegadas_tarde(self) -> list:
        """Devuelve las marcaciones realizadas fuera del horario de ingreso."""
        pass

    @abstractmethod
    def ordenar_legajo(self) -> None:
        """Ordena las marcaciones por legajo de empleado y luego por fecha/hora."""
        pass

    @abstractmethod
    def ordenar_apellido_nombre(self) -> None:
        """Ordena las marcaciones por apellido y nombre del empleado, luego por fecha/hora."""
        pass