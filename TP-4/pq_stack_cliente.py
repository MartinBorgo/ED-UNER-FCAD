from priority_queue_stack import PriorityQueueStack

stack_queue = PriorityQueueStack()

print("Esta vacia:", stack_queue.is_empty())

stack_queue.push("Norma")
stack_queue.push("Eduardo")
stack_queue.push("Raul")
stack_queue.push("Nikita")
stack_queue.push("Roberto")
stack_queue.push("Estela")

print("Esta vacia:", stack_queue.is_empty())
print(stack_queue)
print("Elemento de menor prioridad de la estructura:", stack_queue.top())
print("Eliminar el elemento de menor prioridad de la estructura:", stack_queue.pop())
print("Elemento de menor prioridad actual:", stack_queue.top())
print(stack_queue)