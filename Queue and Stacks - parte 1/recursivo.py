"""Armá un método recursivo para sacar todos los elementos de un stack."""

def vaciar(stack):

    if len(stack) == 0:
        return

    print("Sacando:", stack.pop())

    vaciar(stack)


pila = [1, 2, 3, 4]

vaciar(pila)

print(pila)