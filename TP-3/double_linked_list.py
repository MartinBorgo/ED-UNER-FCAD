from typing import Any, Union
from clases_abstractas.abstract_double_linked_list import DoubleLinkedListAbstract
from clases_abstractas.node import Node

class DoubleLinkedList(DoubleLinkedListAbstract):
    def __init__(self):
        self._head : Union[Node, None] = None
        self._foot : Union[Node, None] = None
        self._size : int = 0

    def __len__(self):
        """ Devuelve la cantidad de elementos que tiene actualmente la lista.
        
            Return:
                int: Numero entero que representa la longitud de la lista. """

        return self._size

    def __getitem__(self, key: int) -> Any:
        """ Devuelve el elemento ubicado en la posicion indicada por el key.
        
            Args:
                key (int): Posicion del elemento que se se va a retornar.
                
            Raise:
                Exception: Arroja una excepcion si la lista se encuentra vacia.
                
            Return:
                Any: Devuelve el elemento de la posicion indicada por el key. """

        if key > self._size or key < 0:
            raise Exception("Valor pasado como argumento fuera de rango.")

        # Inicializo la variable selected_node para recorrer la lista
        selected_node = self._head
        
        # Inicializo i en 1 para poder recorrer la estructura
        i = 1

        # Recorro la lista hasta el valor del key
        while i < key:
            selected_node = selected_node.next
            i += 1

        return selected_node.element

    def __setitem__(self, key: int, value: Any) -> None:
        """ En la posicion indicada por key se coloca el value. 
        
            Args:
                key (int): Posicion en la que se va a colocar el value.
                value (Any): El valor que va a ser colocado en la lista.
                
            Raise:
                Exception: Arroja una excepcion si el key esta fuera de rango. """

        # Controlo que el key este entre los valores validos
        if key > self._size or key < 0:
            raise Exception("Valor del indice fuera de rango.")

        position = self._head
        for i in range(key-1):
            position = position.next
    
        new_node = Node(value, position, position.next)

        # Hago que el nodo previo del siguiente de nodo a position sea el nuevo nodo
        position.next.previous = new_node

        # Hago que el siguiente a position ahora sea el nuevo nodo
        position.next = new_node

        self._size += 1

    def __delitem__(self, key: int) -> None:
        """ Elimina de la estructura el elemento ubicado en la posicion que indica el key.
        
            Args:
                key (int): posicion cuyo nodo se va a quitar de la lista.
                
            Raise:
                Exception: Arroja una excepcion si el indice esta fuera de rango. """

        # Controlo que el key este entre los valores validos
        if key > self._size or key < 0:
            raise Exception("Valor del indice fuera de rango.")

        position = self._head
        for i in range(key):
            position = position.next

        position.next.previous = position.previous
        position.previous.next = position.next

        position.none_pointer()

        self._size -= 1        

    def __iter__(self):
        """ Recorre cada uno de los nodos de la lista y devuelve los elementos de cada uno
            de ellos. 
            
            Yield:
                Iterator[Any]: Cada uno de los elementos de los nodos de la lista. """

        actual = self._head

        while actual:
            #Devuelve el elemento del nodo actual
            yield actual.element
            
            actual = actual.next

    def __str__(self):
        """ Concatena en un único string todos los elementos de la lista.

            Returns:
                str: string con todos los elementos de la lista convertidos en str. """

        #Si la estructura está vacía retorna siempre sesto.
        if self.is_empty():
            return "LinkedList()"
        
        res = ""
        actual = self._head

        while actual:

            res += str(actual.element) + ", "
            actual = actual.next

        # Quito dos elementos al final para que no le quede el ", "
        res = res[:-2]

        return f"LinkedList({res})"

    def is_empty(self) -> bool:
        """ Indica si la lista esta vacia.
        
            Return:
                bool: True si la lista esta vacia, False si existe un elemento o mas. """

        if self._size == 0:
            return True
        else:
            return False

    def append(self, elem : Any) -> None:
        """ Agrega el elemento pasado por parámetro al final de la lista.

            Args:
                elem (Any): Elemento que va a quedar ubicado en la última posición """

        # Creo un nuevo nodo que tenga como elemento al valor pasado por argumento,
        # y como previo al nodo que en ese momento es el foot
        new_node = Node(elem, self._foot)

        if self.is_empty():
            self._head = new_node
            self._foot = new_node
            
            self._size += 1
            return

        # Indico que el siguiente valor del foot es nuestro nuevo nodo 
        self._foot.next = new_node
        # Indico que el foot ahora es el nuevo nodo
        self._foot = new_node

        self._size += 1