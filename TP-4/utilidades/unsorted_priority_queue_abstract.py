from abc import ABC, abstractmethod
from typing import Any, Tuple

class UnsortedPriorityQueueAbstract(ABC):
    """Cola de prioridad mínima no ordenada utilzando representación posicional."""

    @abstractmethod
    def __len__(self) -> int:
        """ Devuelve la cantidad de elementos en la estructura.

        Returns:
            int: Cantidad de elementos en la estructura. 0 en caso que esté vacía. """
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """ Indica si la estructura está vacía o no.

        Returns:
            bool: True si está vacía. False en caso contrario. """
        pass

    @abstractmethod
    def add(self, k: Any, v: Any) -> None:
        """ Inserta un nuevo ítem al final de la estructura.

        Args:
            k (Any): Clave que determina la prioridad del ítem.
            v (Any): Valor del ítem. """
    pass

    @abstractmethod
    def min(self) -> Tuple[Any]:
        """ Devuelve una tupla conformada por la clave y valor del ítem con menor valor de clave.

        Raises:
            Exception: Arroja excepción si se invoca cuando la estructura está vacía.

        Returns:
            Tuple[Any]: Tupla de dos elementos: Clave y Valor del ítem. """
        pass

    @abstractmethod
    def remove_min(self) -> Tuple[Any]:
        """ Quita de la estructura el ítem con menor valor de clave.

        Raises:
            Exception: Arroja excepción si se invoca cuando la estructura está vacía.

        Returns:
            Tuple[Any]: Tupla de dos elementos: Clave y Valor del ítem. """
        pass