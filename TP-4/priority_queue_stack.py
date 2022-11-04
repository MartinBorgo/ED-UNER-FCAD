from utilidades.priority_node import PriorityNode
from typing import Any

class PriorityQueueStack():
    def __init__(self):
        self._content = []
        self._cont : int = 0

    def __len__(self):
        """ Devuelve la longitud de la estructura
            
        Returns:
            int: la longitud de la estructura. """
        return len(self._content)

    def __str__(self):
        """Esta funcion solo me sirve a mi para poder comprobar de que todo anda bien """

        if self.is_empty():
            return "PriorityQueueStack()"
        else:
            return f"PriorityQueueStack{str(self._content)}"

    def is_empty(self) -> bool:
        """ Devuelve si la estructura esta vacia o no
        
        Returns:
            bool: True si la estructura esta vacia, de lo contrario false """
        
        return len(self._content) == 0

    def push(self, value: Any) -> None:
        """ Introduce una nueva entrada al final de la estructura
        
        Param:
            value Any: el valor que se va a introducir en la estructura """

        self._content.append(PriorityNode(self._cont, value))
        self._cont += -1

    def pop(self) -> Any:
        """ Elimina de la estructura el nodo de menor prioridad.
            
        Raises:
            Exception: si la estructura esta vacia arroja una excepcion.

        Reurns:
            Any: el elemento de menor prioridad de la estructura. """

        if self.is_empty():
            raise Exception("No se puede eliminar un elemento si la estructura esta vacia")

        self._cont += 1
        return self._content.pop()
        
    def top(self) -> Any:
        """ Devuelve el elemento de menor prioridad de la estructura..

        Raises:
            exception: si la estructura esta vacia arroja una excepcion.
            
        Return:
            Any: el valor con menor prioridad en la estructura. """
        
        if self.is_empty():
            raise Exception("No se puede buscar un elementos porque la estructura esta vacia")

        return self._content[-1]
