"""
Implementá una función que invierta una lista de elementos 
apilándolos en un stack en un orden, y volviéndolos a escribir 
en la lista en orden inverso.
"""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, numero):
        self.stack.append(numero)

    def isEmpty(self):
        return len(self.stack) == 0
    
    def peek(self):
        if self.isEmpty():
            return "List is empty"
        return self.stack[len(self.stack)-1]
    
    def pop(self):
        if self.isEmpty():
            return "List is empty"
        return self.stack.pop()

    def size(self):
        return len(self.stack)
    
    def final(self):
        return self.stack

def invertir_lista(lista, mi_stack):
    for elemento in lista:
        mi_stack.push(elemento)
    
    lista.clear()
    
    while not mi_stack.isEmpty():
        lista.append(mi_stack.pop())

miLista = [10, 20, 30, 40]
stack = Stack()

print("original:", miLista)

"""La queue tiene actualmente 22 elementos."""

invertir_lista(miLista, stack)


print("invertida:", miLista)