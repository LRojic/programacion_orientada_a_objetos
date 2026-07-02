import os
import json
from menu import mostrar_menu, importar_json
from Estructuras import HashSet

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
    
    pokemones_data, medallas_data = importar_json()
    pokemones = []

    for p in pokemones_data:
        pokemon = Pokemon(
            p["id"],
            p["nombre"],
            p["tipo"],
            p["poder_combate"]
        )
        pokemones.append(pokemon)
        
    medallas = HashSet()
            
    mostrar_menu(pokemones, medallas)
