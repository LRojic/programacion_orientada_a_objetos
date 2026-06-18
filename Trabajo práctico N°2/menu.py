def mostrar_menu(pokemones, medallas):
    while True:
        print("\n===== MENÚ =====")
        print("1. Mostrar pokémones")
        print("2. Mostrar medallas")
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

        else:
            print("Opción inválida.")