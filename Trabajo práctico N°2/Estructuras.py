class Queue:
    def __init__(self):
        self.cola = []

    def encolar(self, pokemon):
        self.cola.append(pokemon)

    def desencolar(self):
        if not self.esta_vacia():
            return self.cola.pop(0)

    def esta_vacia(self):
        return len(self.cola) == 0

    def mostrar(self):
        print(self.cola)


class Nodo:
    def __init__(self, pokemon):
        self.pokemon = pokemon
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, pokemon):
        nuevo = Nodo(pokemon)

        if self.cabeza is None:
            self.cabeza = nuevo
            return

        actual = self.cabeza

        while actual.siguiente:
            actual = actual.siguiente

        actual.siguiente = nuevo
            
    def esta_vacia(self):
        return self.cabeza is None
    
    def eliminar(self, pokemon):

        if self.cabeza is None:
            return False

        if self.cabeza.pokemon == pokemon:
            self.cabeza = self.cabeza.siguiente
            return True

        anterior = self.cabeza
        actual = self.cabeza.siguiente

        while actual is not None:

            if actual.pokemon == pokemon:
                anterior.siguiente = actual.siguiente
                return True

            anterior = actual
            actual = actual.siguiente

        return False
    
    def obtener_lista(self):
        lista = []

        actual = self.cabeza

        while actual is not None:
            lista.append(actual.pokemon)
            actual = actual.siguiente

        return lista
    
    def limpiar(self):
        self.cabeza = None
        
    def mostrar(self):

        actual = self.cabeza

        while actual is not None:
            print(actual.pokemon.nombre)
            actual = actual.siguiente

class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
