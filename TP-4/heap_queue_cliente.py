from heap_queue import HeapQueue

queue_heap = HeapQueue()

queue_heap.enqueue(2, "Norma")
queue_heap.enqueue(21, "Pedro")
queue_heap.enqueue(2, "Ariael")
queue_heap.enqueue(3, "Emond")
queue_heap.enqueue(99, "David")
queue_heap.enqueue(1, "Sancho")

print("tamaño de la estructura:", len(queue_heap))

print("Elemento de menor prioridad:", queue_heap.first())

print("Valor eliminado:",queue_heap.dequeue())
print("Valor eliminado:",queue_heap.dequeue())
print("Valor eliminado:",queue_heap.dequeue())

print("Elemento de menor prioridad actual", queue_heap.first())

