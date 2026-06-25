from jugador import Entrenador
import os, time

def mostrar_menu(pokemones, medallas):
    ash = Entrenador() # es mas corto
    while True:
        
        os.system("cls") # Limpiar la terminal 

        print("\n===== MENÚ =====")
        print("1. Ver Pokédex")
        print("2. Mostrar medallas")
        print("3. capturar pokemon")
        print("4. Ver equipo principal")
        print("5. Ver PC")
        print("6. ir al centro pokemon ")
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

        elif opcion == "4":
            ash.mostrar_equipo()


        elif opcion == "5":
            ash.mostrar_pc()

        elif opcion == "3":
            ash.intento_de_captura(pokemones)

        elif opcion == "6":
            ash.sanar_equipo()


        elif opcion == "0":
            print(pokemones)
            break

        else:
            print("Opción inválida.")
        
        input("\n precione enter para volver al menu ")