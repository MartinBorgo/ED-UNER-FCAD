from heap_queue import HeapQueue

queue_heap = HeapQueue()

queue_heap.enqueue("Norma")
queue_heap.enqueue("Pedro")
queue_heap.enqueue("Ariael")
queue_heap.enqueue("Emond")
queue_heap.enqueue("David")
queue_heap.enqueue("Sancho")

print("tamaño de la estructura:", len(queue_heap))

print("Elemento de menor prioridad:", queue_heap.first())

print("Valor eliminado:", queue_heap.dequeue())
print("Valor eliminado:", queue_heap.dequeue())
print("Valor eliminado:", queue_heap.dequeue())

print("Elemento de menor prioridad actual", queue_heap.first())

