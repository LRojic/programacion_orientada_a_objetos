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

    def intento_de_captura(self, todosLosPokemonesLista):
        print("\n--- Pokédex ---")

        ids_validos = [poke.id for poke in todosLosPokemonesLista]

        while True:
            respuesta = int(input("ID >>> "))

            if respuesta in ids_validos:
                break

            print("ERROR: ID inexistente. Intente nuevamente.")
            
        for poke in todosLosPokemonesLista:
            if poke.id == respuesta:

                if len(self.equipo) < 6:
                    self.equipo.append(poke.nombre)
                    print(f"{poke.nombre} agregado al equipo.")
                else:
                    self.pc.agregar(poke.nombre)
                    print(f"Equipo lleno. {poke.nombre} enviado a la PC.")

                return

        print("No existe un Pokémon con ese ID.")
        
    def mostrar_equipo(self):

        print(" ")
        print("--- Equipo Principal ---")

        if len(self.equipo) == 0:
            print("No hay Pokémon en el equipo.")
            return

        for pokemon in self.equipo:
            print(pokemon)

    def mostrar_pc(self):
        print("\n--- PC ---")
        self.pc.mostrar()