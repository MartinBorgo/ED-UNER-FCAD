from linked_stack_ext import LinkedStackExt


pila = LinkedStackExt()

pila.push("ultimo")
pila.push(2)
pila.push(3)
pila.push(1)
pila.push(1)
pila.push("tope")

print(pila)

pila.replace_all(1, 10)
print("Reemplazo todos los 1 por 10:",pila)

pila.exchange()
print("Intercambia el primer valor de la pila con el ultimo:",pila)

# la clase ListNode no tiene str asi que me imprime las posiciones de memoria
print("Elementos sacados de la pila:", pila.multi_pop(2))
print(pila)