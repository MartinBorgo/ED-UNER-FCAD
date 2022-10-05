from clases_abstractas.abstract_linked_stack_ext import LinkedStackExtAbstract
from python_ed_fcad_uner.data_structures.linear.list_node import ListNode
from python_ed_fcad_uner.data_structures.linear.stacks.linked_stack import LinkedStack
from typing import Union, Any

class LinkedStackExt(LinkedStackExtAbstract, LinkedStack):
    def __init__(self) -> None:
        self._head : Union[ListNode,None] = None
        self._foot = None
        self._size : int = 0

    def push(self, elem: Any):
        """Agrega el elemento pasado por parametro en el tope de la pila.

        Args:
            elem (Any): Nuevo elemento que se va agregar a la pila."""

        #nuevo_tope tiene como siguiente al actual tope (self._head)
        nuevo_tope = ListNode(elem, self._head)
        
        # Si la pila esta vacia le asigno ese valor como al foot (el ultimo elemento)
        if self.is_empty():
          self._foot = nuevo_tope

        #hago a nuevo_tope el nuevo nodo cabecera o head
        self._head = nuevo_tope
        self._size += 1
    
    def multi_pop(self, num : int):
        """Quito elementos la cantidad de veces que se me pase como parametro
        
        Args:
            num(int): Cantidad de elementos a sacar de la pila.
            
        Return:
            Una lista con los elementos que se han sacado de la pila"""

        if self.is_empty():
            raise ValueError("La lista ya esta vacia")

        # Creo la lista que va a almacenar los valores que se expulsan de la pila.
        lista_salida = []
        for i in range(num):
            lista_salida.append(self._head.element)
            
            # Se hace head el sigueinte elemento de la pila.
            self._head = self._head.next
            self._size -= 1
        
        return f"{lista_salida}"

    def replace_all(self, param1: Any , param2: Any):
        """Reemplaza todos los elementos indicados (param1) por un segundo parametro que se indique(param2)
        
        Args:
            param1(Any): El elemento que se desea reemplazar.
            param2(Any): El elemento por el que sera reemplazado param1."""

        actual = self._head

        while actual:
            if actual.element == param1:
                actual.element = param2
            
            actual = actual.next


    def exchange(self):
        """Intercambia el primer elemento de la pila(head) con el ultimo(foot)"""
        
        self._head.element ,self._foot.element = self._foot.element, self._head.element