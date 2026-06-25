"""
Tipo de Pokémon	Poder de combate (PC)
Muy débil       50–200
Débil       	200–500
Intermedio	   500–1000
Fuerte	      1000–2000
Muy fuerte    2000–3200
"""
import os
import json
from menu import mostrar_menu
from Estructuras import Queue, Nodo, ListaEnlazada

os.system("cls") # Limpiar la terminal


class Pokemon:
    def __init__(self, id, nombre, tipo, poder_combate):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.poder_combate = poder_combate
        
    def __str__(self):
        return (f"ID: {self.id} |"
            f"Nm: {self.nombre} | "
            f"Tipo: {self.tipo} | "
            f"PC: {self.poder_combate}")
    

if __name__ == "__main__":
    ruta = os.path.join(os.path.dirname(__file__), "pokemones.json")

    with open(ruta, "r") as file:
        pokemones_data = json.load(file)

    pokemones = []

    for p in pokemones_data:
        pokemon = Pokemon(
            p["id"],
            p["nombre"],
            p["tipo"],
            p["poder_combate"]
        )
        pokemones.append(pokemon)
        
    with open(os.path.join(os.path.dirname(__file__), "medallas.json"), "r",) as file2:
        medallas_data = json.load(file2)
        medallas = []
        for m in range(2): # Solo se necesitan 2 medallas para el menú
            medallas.append(medallas_data[m])
            
    mostrar_menu(pokemones, medallas)
