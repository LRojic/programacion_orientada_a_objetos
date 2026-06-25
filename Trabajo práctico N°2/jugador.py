""" toda la lógica del entrenador:

Equipo activo (lista de máximo 6)
PC (lista enlazada)
Centro Pokémon (queue)
Transferencias (stack)

Después desde main.py importás todo.
"""
import time, random, os
from Estructuras import Queue, Nodo, ListaEnlazada


class Entrenador:
    def __init__(self):
        self.equipo = []
        self.pc = ListaEnlazada()
        self.centro_pokemon = Queue()

    def intento_de_captura(self, todosLosPokemonesLista):
        print("\nBuscando Pokémon salvaje...")

        for i in range(11):
            print(f"\rProgreso: {i * 10}%", end="", flush=True)
            time.sleep(0.5)

        poke = random.choice(todosLosPokemonesLista)

        print(f"\n¡Apareció {poke.nombre}!")
        print("¡Capturado exitosamente!")

        if len(self.equipo) < 6:
            self.equipo.append(poke.nombre)
            print(f"{poke.nombre} agregado al equipo.")
        else:
            self.pc.agregar(poke.nombre)
            print(f"Equipo lleno. {poke.nombre} enviado a la PC.")
            
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

    def sanar_equipo(self):

        if len(self.equipo) == 0:
            print("No hay Pokémon para curar.")
            return

        print("\n--- Centro Pokémon ---")

        # Ingresan a la cola
        for pokemon in self.equipo:
            self.centro_pokemon.encolar(pokemon)
            print(f"{pokemon} ingresó a la cola.")

        print("\nComenzando curación...\n")

        # Se procesan uno por uno
        while not self.centro_pokemon.esta_vacia():

            pokemon = self.centro_pokemon.desencolar()

            print(f"Curando a {pokemon}...")
            time.sleep(1)  # simula tiempo de curación

            print(f"{pokemon} fue curado.\n")

        print("Todos los Pokémon fueron curados.")