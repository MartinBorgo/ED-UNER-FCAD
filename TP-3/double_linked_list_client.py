from double_linked_list import DoubleLinkedList

lista = DoubleLinkedList()

lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)
lista.append(5)
lista.append(6)
lista.append(7)
lista.append(8)

print("Tamaño de la lista:", lista.__len__())

print(lista)

print("Elemeton en posicion 3 ->", lista.__getitem__(3))

lista.__setitem__(4, "valor de prueba")
print("Se agrego un nuevo nodo en la posicion 4", lista, "Longitud: ", lista.__len__())

lista.__delitem__(4)
print("Se elimino el nodo de la posicion 4 de la lista ->", lista)
