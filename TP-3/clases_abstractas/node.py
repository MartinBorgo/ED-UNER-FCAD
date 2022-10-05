from typing import Any, Union

class Node():

    __slots__ = "element", "next", "previous"

    def __init__(self, element: Any, previous = None, next = None):
        self.element = element
        self.next : Union[Node, None] = next
        self.previous : Union[Node, None] = previous

    def none_pointer(self):
        """ Esta funcion simula lo que seria la eliminacion de un nodo. """
        
        self.element = None
        self.next = None
        self.previous = None