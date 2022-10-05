from abc import ABC, abstractmethod
from typing import Any, List

class LinkedStackExtAbstract(ABC):
    """Representa un conjunto de métodos para extender la implementación original
    de LinkedStack.
        Args:
            ABC (_type_): _description_ """
    @abstractmethod
    def multi_pop(self, num: int) -> List[Any]:
        """Realiza la cantidad de operaciones pop() indicada por num.
            Args:
                num (int): número de veces que se va a ejecutar pop().
            Raises:
                Exception: Arroja excepción si se invoca a pop() por cuando la estructura está vacía.
            Returns:
                List[Any]: lista formada por todos los topes que se quitaron de la pila"""
        pass

    @abstractmethod
    def replace_all(self, param1: Any, param2: Any) -> None:
        """Reemplaza todas las ocurrencias de param1 en la pila por param2.
            Args:
                param1 (Any): Valor a buscar/reemplazar.
                param2 (Any): Nuevo valor."""
        pass

    @abstractmethod
    def exchange(self) -> None:
        """Intercambia el elemento ubicado en el tope con el más antigüo o último.
            Raises:
                Exception: Arroja excepción si la estructura está vacía."""
        pass