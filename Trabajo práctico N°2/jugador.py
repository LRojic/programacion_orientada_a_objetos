""" toda la lógica del entrenador:

Equipo activo (lista de máximo 6)
PC (lista enlazada)
Centro Pokémon (queue)
Transferencias (stack)

Después desde main.py importás todo.
"""

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

class Entrenador:
    def __init__(self):
        self.equipo = []
        self.pc = ListaEnlazada()

    def capturar_pokemon(self, pokemon):
        if len(self.equipo) < 6:
            self.equipo.append(pokemon)
            print(f"{pokemon} agregado al equipo.")
        else:
            self.pc.agregar(pokemon)
            print(f"Equipo lleno. {pokemon} enviado a la PC.")