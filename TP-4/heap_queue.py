from python_ed_fcad_uner.data_structures import ArrayHeap
from typing import Any, Tuple

class HeapQueue():
    """Esta clase enmascara a todos los metodos privados de la clase PriorityHeap"""
    def __init__(self):
        self._heap = ArrayHeap()
        self._prio = 0

    def __len__(self) -> int:
        """Devuelve la logitud de la estructura
        
        Returns:
            int: tamaño de la estructura"""

        return len(self._heap)

    def is_empty(self) -> bool:
        """Indica si la estructura esta vacia o no
        
        Returns:
            bool: True si la estructura esta vacia, de lo contrario False """

        return len(self._heap) == 0

    def enqueue(self, value: Any) -> None:
        """Agrega un nodo a la estructura
        
        Param:
            key (Any): clave del nodo.
            value (Any): valor del nodo. """

        self._heap.add(self._prio, value)
        self._prio += 1

    def dequeue(self) -> Tuple[Any]:
        """Remueve el nodo de menor prioridad de la estructura
        
        Raises:
            Exception: arroja una excepcion si la estructura esta vacia. 
            
        Returns: 
            Tuple[Any]: una tupla con la (clave, valor) del nodo de menor prioridad"""

        self._prio -= 1
        return self._heap.remove_min()

    def first(self) -> Tuple[Any]:
        """Devuelve (sin eliminar), la nodo de menor prioridad de la estructura
        
        Returns:
            Tuple[Any]: devuelve una tupla con la (calve, valor) del nodo de menor prioridad. """

        return self._heap.min()