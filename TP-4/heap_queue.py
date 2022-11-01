from python_ed_fcad_uner.data_structures import ArrayHeap
from typing import Any

class HeapQueue():
    """Esta clase enmascara a todos los metodos privados de la clase PriorityHeap"""
    def __init__(self):
        self._heap = ArrayHeap()

    def __len__(self):
        """Devuelve la logitud de la estructura
        
        Returns:
            int: tamaño de la estructura"""

        return len(self._heap)

    def is_empty(self):
        """Indica si la estructura esta vacia o no
        
        Returns:
            bool: True si la estructura esta vacia, de lo contrario False """

        return len(self._heap) == 0

    def enqueue(self, key: Any, value: Any):
        """Agrega un nodo a la estructura
        
        Param:
            key (Any): clave del nodo.
            value (Any): valor del nodo. """

        self._heap.add(key, value)

    def dequeue(self):
        """Remueve el nodo de menor prioridad de la estructura
        
        Raises:
            Exception: arroja una excepcion si la estructura esta vacia. """

        del_node = self._heap.remove_min()

        return del_node[1]

    def first(self):
        """Devuelve (sin eliminar), la nodo de menor prioridad de la estructura
        
        Returns:
            Any: devuelve el valor de menor prioridad de la estructura"""
        
        min_prio = self._heap.min()

        return min_prio[1]