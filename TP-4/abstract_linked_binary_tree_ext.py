from abc import ABC, abstractmethod
from typing import Any, List, Union
from python_ed_fcad_uner.data_structures import BinaryTreeNode

class LinkedBinaryTreeExtAbstract(ABC):
    """ Conjunto de métodos adicionales a LinkedBinaryTree"""

    @abstractmethod
    def hermanos(self, nodo1 : BinaryTreeNode, nodo2: BinaryTreeNode) -> bool:
        """ Indica si node1 y node2 son hermanos.
        
        Args:
            nodo1 (BinaryTreeNode): nodo que debe pertenecer al árbol.
            nodo2 (BinaryTreeNode): nodo que debe pertenecer al árbol.

        Returns:
            bool: True si los nodos tienen el mismo padre, False en caso contrario. """
        pass

    @abstractmethod
    def hojas(self) -> List[Any]:
        """ Devuelve los elementos de los nodos que no tienen ningún hijo.

        Returns:
            List[Any]: lista formada por los elementos de los nodos hoja. """
        pass

    @abstractmethod
    def internos(self) -> List[Any]:
        """ Devuelve los elementos de los nodos que tienen padre y algún hijo.

        Returns:
            List[Any]: lista formada por los elementos de los nodos internos. """
        pass

    @abstractmethod
    def profundidad(self, nodo : BinaryTreeNode) -> int:
        """ Devuelve la longitud del camino entre la raíz y un nodo.

        Args:
            nodo (BinaryTreeNode): nodo del que se quiere conocer la profundidad.

        Returns:
            int: devuelve el número de arcos entre la raíz y nodo. 0 si nodo es la raíz. """
        pass

    @abstractmethod
    def altura(self, nodo : BinaryTreeNode) -> int:
        """ Retorna la longitud del camino entre nodo y la hoja más lejana.
        Args:
            nodo (BinaryTreeNode): nodo del que se quiere conocer la altura.

        Returns:
            int: Devuelve 0 en caso que nodo sea hoja, caso contrario, la cantidad de arcos
            entre nodo y la hoja más lejana. """
        pass