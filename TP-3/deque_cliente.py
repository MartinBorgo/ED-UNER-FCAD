from deque import Deque

test = Deque()

test.add_first(2)
test.add_first(1)
test.add_first(3)
test.add_first("front")
test.add_last(3)
test.add_last("back")

print("Elementos de la estructura -> ",test)

print("Primer elemento de la cola -> ", test.first())
print("Ultimo elemento de la cola -> ", test.last())

test.delete_first()
print("Se elimina el primer elemento de la estructura -> ",test)

test.delete_last()
print("Se elimino el ultimo elemento de la estructura -> ",test)