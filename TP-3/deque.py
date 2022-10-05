from clases_abstractas.abstract_deque import DequeAbstract
from python_ed_fcad_uner.data_structures.linear.list_node import ListNode
from typing import Any

class Deque(DequeAbstract):
    def __init__(self) -> None:
        self._front: Union[ListNode, None] = None
        self._back: Union[ListNode, None] = None
        self._size : int = 0


    def __len__(self):
        """Devuelve la cantidad de elementos que tiene la estructura
        
        Return:
            int: Cantidad de elementos, 0 si esta vacia"""

        return self._size

    def __str__(self):
        """ Concatena un unico String con todos los elementos de los nodos
            de la estructura.
        
        Return:
            str: Representacion de los elementos de la estructura en String"""

        #Si la estructura está vacía entonses devuelve siempre esto.
        if self.is_empty():
            return "Deque()"
        
        resultado = "" # Inicializo resultado con el string vacío para ir concatenando

        #Inicializo actual con el elemento que esta en el frente de la cola
        actual = self._front
        while actual != None:
            # Se convieerte el elemento del nodo a String.
            resultado += str(actual.element) + ", "
            
            # Actual ahora va a ser el proximo nodo al que ya teniamos
            actual = actual.next 
        
        #Le quito los dos ultimos caracteres para que no aparezca con un ", " al final del String    
        resultado = resultado[:len(resultado)-2]
        
        return f"Deque({resultado})"

    def is_empty(self):
        """Indica si la estructura esta vacia o no.
        
            Return:
                True: Si la lista esta vacia.
                False: Si la lista tiene elementos. """

        return self._size == 0

    def first(self) -> Any:
        """Devuelve el elemento ubicado en el frente de la estructura.
        
        Raise:
            Exeption: Error porque la estructura no posee ningun elemento.
            
        Return:
            Any: Elemento correspondiente al frente de la estructura."""

        # Si la estructura esta vacia arroja una excepcion
        if self.is_empty():
            raise Exception("La estructura esta vacia")

        return self._front.element

    def last(self):
        """Devuelve el elemento correspondiente al ultimo nodo de la estructura.
        
        Raise:
            Exception: Arroja una excepcion si la estructura esta vacia
            
        Return:
            Any: Elemento correspondiente al ultimo nodo de la cola"""

        # Si la estructura esta vacia arroja una excepcion
        if self.is_empty():
            raise Exception("La estructura esta vacia")

        return self._back.element

    def add_first(self, element: Any) -> None:
        """Agrega un elemento al principio de la estructura
        
        Args:
            element(Any): elemento que se agregara al principio de la fila"""

        # Creo un nuevo nodo que tenga de elemento = element y next = front actual
        nuevo_nodo = ListNode(element, self._front)

        # Si la estructura esta vacia inicializo front y back en ese nodo
        if self.is_empty():
            self._front = nuevo_nodo
            self._back = nuevo_nodo
        else:
            # Si la estructura ya tiene elementos, el nuevo nodo pasa a ser el nuevo front
            self._front = nuevo_nodo

        self._size +=1

    def add_last(self, element : Any) -> None:
        """Agrega un elemento al final de la estructura.
        
        Args:
            element(Any): elemento que va a ser agregado al final de la estructura"""

        nuevo_nodo = ListNode(element, None)
        
        if self.is_empty():
            self._front = nuevo_nodo
            self._back = nuevo_nodo
        else:
            self._back.next = nuevo_nodo
            self._back = self._back.next
            
        self._size += 1

    def delete_first(self) -> None:
        """Quita el elemento ubicado en el frente de la estructura
        
        Raise:
            Exception: Arroja una excepcion cuando esta vacia"""

        if self.is_empty():
            raise Exception("La estructura esta vacia")

        anterior_front = self._front

        self._front = self._front.next
        del anterior_front

        self._size -= 1

    def delete_last(self) -> None:
        """Quita el elemento ubicado al final de la estructura.
        
        Raise:
            Exception: Arroja una excepcion si la estructura esta vacia"""

        if self.is_empty():
            raise Exception("La estructura esta vacia")
        
        nuevo_back = self._front

        #Recorro toda la estructura hasta llegar al anteultimo nodo
        while nuevo_back.next.next:
            nuevo_back = nuevo_back.next

        # Asigno el nuevo back y seteo su siguiente como None
        self._back = nuevo_back
        self._back.next = None

        self._size -= 1