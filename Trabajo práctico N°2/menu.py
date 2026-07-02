from jugador import Entrenador
import os, time, json

def importar_json():
    
    ruta = os.path.join(os.path.dirname(__file__), "pokemones.json")
    ruta2 = os.path.join(os.path.dirname(__file__), "medallas.json")
    try:
        with open(ruta, "r") as file:
            pokemones_data = json.load(file)
    except FileNotFoundError:
        print(f"Archivo pokemones.json no encontrado en {ruta}.")
        exit(1)
    except json.JSONDecodeError:
        print(" Error: El archivo 'pokemones.json' está dañado o tiene un formato JSON inválido.")
        exit()
    except Exception as e:
        print(f"Error al leer el archivo {ruta}: {e}")
        exit(1)
        
    try:
        with open(ruta2, "r") as file2:
            medallas_data = json.load(file2)
    except FileNotFoundError:
        print(f"Archivo medallas.json no encontrado en {ruta2}.")
        exit(1)
    except json.JSONDecodeError:
        print(" Error: El archivo 'medallas.json' está dañado o tiene un formato JSON inválido.")
        exit()
    except Exception as e:
        print(f"Error al leer el archivo {ruta2}: {e}")
        exit(1)
        
    return pokemones_data, medallas_data
    

def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print(" Debe ingresar un número.")
            
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
        print("11. Buscar Pokémon por nombre")
        print("12. Buscar Pokémon por ID en la Pokedex")
        print("0. Salir")
        print("")
        time.sleep(0.4)
        opcion = input("Seleccione una opción: ").strip()

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

                    opcion_pokemon = pedir_entero("\nSeleccione un Pokémon: ")

                    if 1 <= opcion_pokemon <= len(pokemones_pc):
                        nombre = pokemones_pc[opcion_pokemon - 1]
                        ash.transferir_pokemon(nombre)
                        break
                    else:

                        print(" Opción inválida.")

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

                    opcion_orden = input("Seleccione una opción: ").strip()

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
                        
        elif opcion == "11":
            nombre = input("Nombre del Pokémon: ").strip().lower().title()
            ash.buscar_pokemon_equipo(nombre)
            
        elif opcion == "12":
            
            id = pedir_entero("Ingrese ID: ")
            pokemon_buscado = ash.buscar_pokedex(pokemones, id)

            if pokemon_buscado:
                print(f"Encontrado: {pokemon_buscado.nombre}")
            else:
                print("No existe ese Pokémon.")

        elif opcion == "0":
            print("Saliendo del programa...")
            time.sleep(1)
            break

        else:
            print("Opción inválida.")
        
        input("\nEnter para volver al menu...")