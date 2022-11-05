from abstract_linked_binary_tree_ext import LinkedBinaryTreeExtAbstract
from python_ed_fcad_uner.data_structures import LinkedBinaryTree, BinaryTreeNode

class LinkedBinaryTreeExt(LinkedBinaryTreeExtAbstract,LinkedBinaryTree):
    
    def hermanos(self, nodo1 : BinaryTreeNode, nodo2 : BinaryTreeNode) -> bool:
        """ Indica si node1 y node2 son hermanos.
        
        Args:
            nodo1 (BinaryTreeNode): nodo que debe pertenecer al árbol.
            nodo2 (BinaryTreeNode): nodo que debe pertenecer al árbol.

        Returns:
            bool: True si los nodos tienen el mismo padre, False en caso contrario. """
        
        padre_nodo1 = self._search_parent(nodo1)
        padre_nodo2 = self._search_parent(nodo2)

        if padre_nodo1.element == padre_nodo2.element:
            return True
        else:
            return False

    def hojas(self) -> list:
        """ Devuelve los elementos de los nodos que no tienen ningún hijo.
        
        Returns:
            List[Any]: lista formada por los elementos de los nodos hoja. """

        lista_hojas = []

        for nodo in self.__iter__():
            if nodo.children_count() == 0:
                lista_hojas.append(nodo.element)

        return lista_hojas

    def internos(self) -> list:
        """ Devuelve los elementos de los nodos que tienen padre y algún hijo.

        Returns:
            List[Any]: lista formada por los elementos de los nodos internos. """

        internos = []
        for nodo in self.__iter__():

            if self._search_parent(nodo):
                if nodo.right_child or nodo.left_child:
                    internos.append(nodo.element)

        return internos

    def profundidad(self, nodo : BinaryTreeNode) -> int:
        """ Devuelve la longitud del camino entre la raíz y un nodo.

        Args:
            nodo (BinaryTreeNode): nodo del que se quiere conocer la profundidad.

        Returns:
            int: devuelve el número de arcos entre la raíz y nodo. 0 si nodo es la raíz. """

        deep = self._search_parent(nodo)
        profundidad = 1

        # Si el padre del nodo es None entonses es la raiz -> la profundidad es 0
        if not deep:
            return 0

        while deep:
            deep = self._search_parent(deep)
            
            # Si el padre de deep es None estonses es la raiz, por lo tanto retorno la profundidad
            # de lo contrario sumo uno a la profundidad y sigo el bucle
            if not deep:
                return profundidad
            else:
                profundidad += 1

    def altura(self, nodo : BinaryTreeNode) -> int:
        """ Retorna la longitud del camino entre nodo y la hoja más lejana.
        Args:
            nodo (BinaryTreeNode): nodo del que se quiere conocer la altura.

        Returns:
            int: Devuelve 0 en caso que nodo sea hoja, caso contrario, la cantidad de arcos
            entre nodo y la hoja más lejana. """
        
        if nodo.children_count() == 0:
            return 0

        # Inicializo la lista con todas las hojas
        hojas = self._nodos_hoja()
        contador = 0
        altura = 0

        while len(hojas) != 0:
            # tomo la ultima hoja de la hoja
            mi_nodo = hojas.pop()

            while mi_nodo:
                mi_nodo = self._search_parent(mi_nodo)

                if nodo == mi_nodo:
                    if altura < contador:
                        altura = contador
                else:
                    contador += 1
                
                if mi_nodo == None:
                    pass
            
            contador = 1

        return altura

    def _nodos_hoja(self) -> list:
        """ Devuelve los nodos que no tienen ningún hijo.
        
        Returns:
            List[_Item]: lista formada por los nodos hoja. """

        lista_nodos_hoja = []

        for nodo in self.__iter__():
            if nodo.children_count() == 0:
                lista_nodos_hoja.append(nodo)

        return lista_nodos_hoja