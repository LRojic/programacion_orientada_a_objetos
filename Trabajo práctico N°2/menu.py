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
        print("7. Transferir Pokémon al Profesor Oak")
        print("8. Deshacer última transferencia")
        print("9: Desafiar gimnasio")
        print("10. Ordenar PC ")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- Lista de Pokémones ---")
            for pokemon in pokemones:
                print(pokemon)

        elif opcion == "2":
            medallas.mostrar()

        elif opcion == "4":
            ash.mostrar_equipo()


        elif opcion == "5":
            if ash.pc.esta_vacia():
                print("La PC está vacía.")
            else:
                ash.mostrar_pc()

        elif opcion == "3":
            ash.intento_de_captura(pokemones)

        elif opcion == "6":
            ash.sanar_equipo()
        
        elif opcion == "7":

            if ash.pc.esta_vacia():
                print("La PC está vacía.")
            else:

                pokemones_pc = ash.pc.obtener_lista()

                print("\n--- PC ---")
                for i, pokemon in enumerate(pokemones_pc, start=1):
                    print(f"{i}. {pokemon}")

                try:
                    opcion_pokemon = int(input("\nSeleccione un Pokémon: "))

                    if 1 <= opcion_pokemon <= len(pokemones_pc):
                        nombre = pokemones_pc[opcion_pokemon - 1]
                        ash.transferir_pokemon(nombre)
                    else:
                        print("Opción inválida.")

                except ValueError:
                    print("Ingrese un número.")

        elif opcion == "8":
            ash.deshacer_transferencia()

        elif opcion == "9":
            ash.desafiar_gimnasio(medallas)
            
        elif opcion == "10":
            if ash.pc.esta_vacia():
                print("La PC está vacía.")
            else:
                while True:
                    print("\n--- Ordenar PC ---")
                    print("1. Por nombre")
                    print("2. Por tipo")
                    print("3. Por poder de combate")
                    print("0. Volver al menú principal")

                    opcion_orden = input("Seleccione una opción: ")

                    if opcion_orden == "1":
                        ash.ordenar_pc_nombre()
                        break
                    elif opcion_orden == "2":
                        ash.ordenar_pc_tipo()
                        break
                    elif opcion_orden == "3":
                        ash.ordenar_pc_poder()
                        break
                    elif opcion_orden == "0":
                        break
                    else:
                        print("Opción inválida.")


        elif opcion == "0":
            print(pokemones)
            break

        else:
            print("Opción inválida.")
        
        input("\n precione enter para volver al menu ")