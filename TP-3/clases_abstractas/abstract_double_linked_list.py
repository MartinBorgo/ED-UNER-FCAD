from abc import ABC, abstractmethod
from typing import Any, Iterator

class DoubleLinkedListAbstract(ABC):
    """ Representa una lista doblemente enlazada en la cada nodo tienen referencia a su
        antecesor y sucesor. """

    @abstractmethod
    def __len__(self) -> int:
        """ Devuelve la cantidad de elementos que tiene actualmente la lista.

            Returns:
                int: entero que indica a longitud de la lista. 0 si está vacía."""
        pass

    @abstractmethod
    def __getitem__(self, key: int) -> Any:
        """ Devuelve el elemento ubicado en la posición indicada por key.
            
            Args:
                key (int): posición de la que se va a retornar el elemento de la lista.

            Raises:
                Exception: Arroja excepción si el índice está fuera de rango.

            Returns:
                Any: Devuelve el valor ubicado en la posición indicada por key."""
        pass

    @abstractmethod
    def __setitem__(self, key: int, value: Any) -> None:
        """ En la posición indicada por key se va a colocar value.

            Args:
                key (int): posición que se va a actualizar.
                value (Any): nuevo valor que se va a colocar.

            Raises:
                Exception: Arroja excepción si el índice está fuera de rango. """
        pass

    @abstractmethod
    def __delitem__(self, key: int) -> None:
        """ Elimina de la estructura el elemento ubicado en la posición key.

            Args:
                key (int): posición cuyo nodo se va a quitar de la estructura.
            
            Raises:
                Exception: Arroja excepción si el índice está fuera de rango. """
        pass

    @abstractmethod
    def __iter__(self) -> Iterator[Any]:
        """ Visita desde el principio hacia el final todos los nodos de la lista y
            retorna sus elementos.

            Yields:
                Iterator[Any]: Cada uno de los elementos de los nodos de lista. """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """ Concatena en un único string todos los elementos de la lista.

            Returns:
                str: string con todos los elementos de la lista convertidos en str. """
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """ Indica si la estructura está vacía.

            Returns:
                bool: True si la lista está vacía, caso contrario, False. """
        pass

    @abstractmethod
    def append(self, elem: Any) -> None:
        """ Agrega el elemento pasado por parámetro al final de la lista.

            Args:
                elem (Any): elemento que va a quedar ubicado en la última posición """
        pass