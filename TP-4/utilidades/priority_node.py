from typing import Any

class PriorityNode():
        """ Clase interna que sirve para repesentar los pares <clave, valor> """

        def __init__(self, key : Any, value : Any):
            self._key = key
            self._value = value

        def __lt__(self, o):
            if isinstance(o, self.__class__):
                return self._key < o._key

        def __eq__(self, o):
            if isinstance(o, self.__class__):
                return self._key == self._key

        def __repr__(self):
            return f"<key:{self._key}, value:{self._value}>"

        def __str__(self):
            return self.__repr__()