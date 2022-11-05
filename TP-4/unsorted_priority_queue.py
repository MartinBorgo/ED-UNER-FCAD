from utilidades.unsorted_priority_queue_abstract import UnsortedPriorityQueueAbstract
from python_ed_fcad_uner.data_structures import PriorityQueueBase
from typing import Any, Tuple

class UnsortedPriorityQueue(UnsortedPriorityQueueAbstract, PriorityQueueBase):

    def __init__(self):
        self._content = []

    def __len__(self) -> int:
        """ Devuelve la cantidad de elementos en la estructura.

        Returns:
            int: Cantidad de elementos en la estructura. 0 en caso que esté vacía. """

        return len(self._content)

    def __str__(self) -> str:
        if self.is_empty():
            return "UnsortedPriorityQueue()"
        else:
            return f"UnsortedPriorityQueue({str(self._content)})"

    def is_empty(self):
        """ Indica si la estructura está vacía o no.
        
        Returns:
            bool: True si está vacía. False en caso contrario. """

        return self.__len__() == 0

    def add(self, k : Any, v : Any) -> None:
        """ Inserta un nuevo ítem al final de la estructura.

        Args:
            k (Any): Clave que determina la prioridad del ítem.
            v (Any): Valor del ítem. """

        self._content.append(self._Item(k, v))
    
    def min(self) -> Tuple[Any]:
        """ Devuelve una tupla conformada por la clave y valor del ítem con menor valor de clave.

        Raises:
            Exception: Arroja excepción si se invoca cuando la estructura está vacía.

        Returns:
            Tuple[Any]: Tupla de dos elementos: Clave y Valor del ítem. """

        if self.is_empty():
            raise Exception("La estructura esta vacia")

        menor = self._content[0]
        for elem in self._content:
            if elem._key < menor._key:
                menor = elem

        return (menor._key,menor._value)


    def remove_min(self) -> Tuple[Any]:
        """ Quita de la estructura el ítem con menor valor de clave.
        
        Raises:
            Exception: Arroja excepción si se invoca cuando la estructura está vacía.

        Returns:
            Tuple[Any]: Tupla de dos elementos: Clave y Valor del ítem. """

        if self.is_empty():
            raise Exception("La estructura esta vacia")

        lower_priority = self._content[0]

        for elem in self._content:
            if elem < lower_priority:
                lower_priority = elem

        tupla = (lower_priority._key,lower_priority._value)
        
        self._content.remove(lower_priority)

        return tupla