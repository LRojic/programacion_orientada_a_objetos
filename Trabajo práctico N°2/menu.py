from jugador import Entrenador
def mostrar_menu(pokemones, medallas):
    while True:
        print("\n===== MENÚ =====")
        print("1. Ver Pokédex")
        print("2. Mostrar medallas")
        print("3. **Prueba entrenador")
        print("4. Ver equipo Principal")
        print("5. Ver PC")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- Lista de Pokémones ---")
            for pokemon in pokemones:
                print(pokemon)

        elif opcion == "0":
            print("Saliendo...")
            break
        
        elif opcion == "2":
            print("\n--- Lista de Medallas ---")
            for m in medallas:
                print(m)
        elif opcion == "3":
            print("\n--- Prueba entrenador ---")
            ash = Entrenador()

            ash.capturar_pokemon("Pikachu")
            ash.capturar_pokemon("Charmander")
            ash.capturar_pokemon("Squirtle")
            ash.capturar_pokemon("Bulbasaur")
            ash.capturar_pokemon("Pidgeotto")
            ash.capturar_pokemon("Snorlax")

            ash.capturar_pokemon("Dragonite")
                    

        else:
            print("Opción inválida.")



