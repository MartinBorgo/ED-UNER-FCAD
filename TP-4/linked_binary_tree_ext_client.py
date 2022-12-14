from python_ed_fcad_uner.data_structures import BinaryTreeNode
from linked_binary_tree_ext import LinkedBinaryTreeExt

nodo_a = BinaryTreeNode('A')
nodo_b = BinaryTreeNode('B')
nodo_c = BinaryTreeNode('C')
nodo_d = BinaryTreeNode('D')
nodo_f = BinaryTreeNode('F')
nodo_g = BinaryTreeNode('G')
nodo_h = BinaryTreeNode('H')
nodo_i = BinaryTreeNode('I')
nodo_k = BinaryTreeNode('K')
nodo_m = BinaryTreeNode('M')
nodo_n = BinaryTreeNode('N')

arbol = LinkedBinaryTreeExt()

arbol.add_left_child(None, nodo_a)
arbol.add_left_child(nodo_a, nodo_b)
arbol.add_right_child(nodo_a, nodo_f)
arbol.add_left_child(nodo_b, nodo_c)
arbol.add_right_child(nodo_b, nodo_d)
arbol.add_left_child(nodo_f, nodo_g)
arbol.add_right_child(nodo_f, nodo_k)
arbol.add_left_child(nodo_g, nodo_h)
arbol.add_right_child(nodo_g, nodo_i)
arbol.add_left_child(nodo_k, nodo_m)
arbol.add_right_child(nodo_k, nodo_n)

print(arbol)

print("Veo si nodo B y F son hermanos", arbol.hermanos(nodo_b, nodo_f))
print("Veo si nodo B y D son hermanos", arbol.hermanos(nodo_b, nodo_d))
print("Lista de todas las hojas del arbol ->", arbol.hojas())
print("Listado de todos los nodos internos ->", arbol.internos())
print("Profundidad del nodo M:", arbol.profundidad(nodo_m))
print("Profundidad del nodo F:", arbol.profundidad(nodo_f))
print("Profundidad del nodo A:", arbol.profundidad(nodo_a))
print("Altura del nodo A:", arbol.altura(nodo_a))
print("Altura del nodo F:", arbol.altura(nodo_f))
print("Altura del nodo C:", arbol.altura(nodo_c))