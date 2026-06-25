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

    def mostrar(self):
        actual = self.cabeza

        while actual:
            print(actual.pokemon)
            actual = actual.siguiente