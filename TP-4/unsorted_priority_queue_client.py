from unsorted_priority_queue import UnsortedPriorityQueue

priority_queue = UnsortedPriorityQueue()

priority_queue.add(288, "Martin")
priority_queue.add(16, "Norma")
priority_queue.add(11, "Eduardo")
priority_queue.add(2, "Patricio")
priority_queue.add(2, "Jonatan")
priority_queue.add(5, "Ailin")
priority_queue.add(30, "Marta")

print(priority_queue)
print("Tamaño del UsortedPriorityQueue:", len(priority_queue))
print("True si la Cola esta vacia, de lo contrario false:", priority_queue.is_empty())

print("El elemento de menor prioridad es:", priority_queue.min())

print("Se elimino el elemento:", priority_queue.remove_min())
print("Se elimino el elemento:", priority_queue.remove_min())
print("Se elimino el elemento:", priority_queue.remove_min())
print("Se elimino el elemento:", priority_queue.remove_min())
print(priority_queue)

print("Tamaño actual del UsortedPriorityQueue:", len(priority_queue))
print("El elemento de menor prioridad ahora es es:", priority_queue.min())