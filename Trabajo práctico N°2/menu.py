from jugador import Entrenador
import os, time

def mostrar_menu(pokemones, medallas):
    ash = Entrenador()
    while True:
        
        os.system("cls") # Limpiar la terminal 

        print("\n===== MENÚ =====")
        print("1. Ver Pokédex")
        print("2. Mostrar medallas")
        print("3. Prueba entrenador")
        print("4. Ver equipo principal")
        print("5. Ver PC")
        print("6. capturar pokemon")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- Lista de Pokémones ---")
            for pokemon in pokemones:
                print(pokemon)

        elif opcion == "2":
            print("\n--- Lista de Medallas ---")
            for m in medallas:
                print(m)

        elif opcion == "3":
            print("\n--- Prueba entrenador ---")

            ash.capturar_pokemon("Pikachu")
            ash.capturar_pokemon("Charmander")
            ash.capturar_pokemon("Squirtle")
            ash.capturar_pokemon("Bulbasaur")
            ash.capturar_pokemon("Pidgeotto")
            ash.capturar_pokemon("Snorlax")
            ash.capturar_pokemon("Dragonite")


        elif opcion == "4":
            ash.mostrar_equipo()


        elif opcion == "5":
            ash.mostrar_pc()

        elif opcion == "6":
            ash.intento_de_captura(pokemones)


        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")
        
        x = input("\n precione enter para volver al menu ")