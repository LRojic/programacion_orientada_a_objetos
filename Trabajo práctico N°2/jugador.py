""" lógica del entrenador:

Equipo activo (lista de máximo 6)
PC (lista enlazada)
Centro Pokémon (queue)
Transferencias (stack)
"""
import time, random
from Estructuras import Queue, ListaEnlazada, Stack, HashSet
import json, os
with open(os.path.join(os.path.dirname(__file__), "gimnasios.json"), "r") as file:
    gimnasios_data = json.load(file)

def pedir_entero(mensaje, min=None, max=None):
    while True:
        try:
        except ValueError:
            print(" Debe ingresar un número entero.")
            continue
        if (min is not None and valor < min) or (max is not None and valor > max):
            continue
        return valor
    
class Entrenador:
    def __init__(self):
        self.equipo = []
        self.pc = ListaEnlazada()
        self.centro_pokemon = Queue()
        self.transferencias = Stack()

    def intento_de_captura(self, todosLosPokemonesLista):
        print("\nBuscando Pokémon salvaje...")
        
        """  BARRA DE CARGA
        for i in range(11):
            print(f"\rProgreso: {i * 10}%", end="", flush=True)
            time.sleep(0.5)"""

        poke = random.choice(todosLosPokemonesLista)

        print(f"\n¡Apareció {poke.nombre}!")
        print("¡Capturado exitosamente!")

        if len(self.equipo) < 6:
            self.equipo.append(poke)
            print(f"{poke.nombre} agregado al equipo.")
        else:
            self.pc.agregar(poke)
            print(f"Equipo lleno. {poke.nombre} enviado a la PC.")
            
    def mostrar_equipo(self):

        print(" ")
        print("--- Equipo Principal ---")

        if len(self.equipo) == 0:
            print("No hay Pokémon en el equipo.")
            return

        for pokemon in self.equipo:
            print(pokemon.nombre)

    def mostrar_pc(self):
        print("\n--- PC ---")
        self.pc.mostrar()

    def sanar_equipo(self):

        if len(self.equipo) == 0:
            print("\nNo hay Pokémon para curar.")
            return

        print("\n--- Centro Pokémon ---")

        # Ingresan a la cola
        for pokemon in self.equipo:
            self.centro_pokemon.encolar(pokemon)
            print(f"{pokemon.nombre} - {pokemon.tipo} ingresó a la cola.")

        print("\nComenzando curación...\n")

        # Se procesan uno por uno
        while not self.centro_pokemon.esta_vacia():

            pokemon = self.centro_pokemon.desencolar()

            print(f"Curando a {pokemon.nombre} - {pokemon.tipo}...")
            time.sleep(1)  # simula tiempo de curación

            print(f"{pokemon.nombre} - {pokemon.tipo} fue curado.\n")

        print("Todos los Pokémon fueron curados.")

    def desafiar_gimnasio(self, medallas):
            print("\n=== Gimnasios ===")
            for gimnasio in gimnasios_data:
                print(f'{gimnasio["id"]}. {gimnasio["nombre"]} - Líder: {gimnasio["lider"]}')

            opcion = pedir_entero("\nElegi un gimnasio: ", min=1, max=len(gimnasios_data))

            gimnasio = None

                if g["id"] == opcion:
                    break

            if gimnasio is None:
                return

            print(f"\nEntraste al {gimnasio['nombre']}.")
            print(f"¡{gimnasio['lider']} te desafía a una batalla!")


            if random.choice([True, False]):
                print("\n¡Ganaste la batalla!")

                if medallas.agregar(gimnasio["medalla"]):
                    print(f"Obtuviste la {gimnasio['medalla']}.")
                else:
                    print(f"Ya tenías la {gimnasio['medalla']}.")
            else:
                print("\nPerdiste la batalla...")
    # métodos para transferir y deshacer transferencias:

    def transferir_pokemon(self, nombre):

        if self.pc.eliminar(nombre):

            self.transferencias.push(nombre)

            # Mantener solo las últimas 5 transferencias
            if self.transferencias.size() > 5:
                self.transferencias.items.pop(0)

            print(f"{nombre} fue transferido al Profesor Oak.")
        else:
            print("Ese Pokémon no está en la PC.")

    def deshacer_transferencia(self):

        if self.transferencias.isEmpty():
            print("No hay transferencias para deshacer.")
            return

        pokemon = self.transferencias.pop()
        self.pc.agregar(pokemon)

        print(f"{pokemon} volvió a la PC.")
    
    # metodos para ordenar la PC:
    
    def ordenar_pc_nombre(self):

        lista = self.pc.obtener_lista()

        n = len(lista)

        for i in range(n):
            for j in range(n - i - 1):

                if lista[j].nombre > lista[j + 1].nombre:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

        self.pc.limpiar()

        for pokemon in lista:
            self.pc.agregar(pokemon)

        print("\n--- PC ordenada por nombre ---")
        for pokemon in lista:
            print(f"{pokemon.nombre}")

    def ordenar_pc_tipo(self):

        lista = self.pc.obtener_lista()

        n = len(lista)

        for i in range(n):

            minimo = i

            for j in range(i + 1, n):

                if lista[j].tipo < lista[minimo].tipo:
                    minimo = j

            lista[i], lista[minimo] = lista[minimo], lista[i]

        self.pc.limpiar()

        for pokemon in lista:
            self.pc.agregar(pokemon)

        print("\n--- PC ordenada por tipo ---")
        for pokemon in lista:
            print(f"{pokemon.nombre} - {pokemon.tipo}")
    
    def quick_sort_poder(self, lista):
        """Quick Sort (por poder de combate)"""

        if len(lista) <= 1:
            return lista

        pivote = lista[0]

        mayores = []
        menores = []

        for pokemon in lista[1:]:
            if pokemon.poder_combate > pivote.poder_combate:
                mayores.append(pokemon)
            else:
                menores.append(pokemon)
        return self.quick_sort_poder(mayores) + [pivote] + self.quick_sort_poder(menores)

    def ordenar_pc_poder(self):

        lista = self.pc.obtener_lista()
        lista = self.quick_sort_poder(lista)
        self.pc.limpiar()
        for pokemon in lista:
            self.pc.agregar(pokemon)
        print("\n--- PC ordenada por poder de combate ---")
        for pokemon in lista:
            print(f"{pokemon.nombre} - CP: {pokemon.poder_combate}")
            
    # modulo 4:    
        
    def buscar_pokemon_equipo(self, nombre):
        """va 1 por 1, complejidad O(n) wacho"""
        for pokemon in self.equipo:
            if pokemon.nombre.lower() == nombre.lower():
                print(f"{pokemon.nombre} está en el equipo.")
                return pokemon
        print("Ese Pokémon no está en el equipo.")
        return None
    
    def buscar_pokedex(self, lista, id_buscado):
        """elimina la mitad de la lista en cada iteración, complejidad O(log n), mas tranki piola sin berretin"""
        izquierda = 0
        derecha = len(lista) - 1
        while izquierda <= derecha:

            medio = (izquierda + derecha) // 2

            if lista[medio].id == id_buscado:
                return lista[medio]
            elif id_buscado < lista[medio].id:
                derecha = medio - 1
            else:
                izquierda = medio + 1
        return None