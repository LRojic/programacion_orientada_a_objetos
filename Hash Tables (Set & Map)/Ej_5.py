class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash_function(self, key):
        # Calcula el índice del bucket
        return sum(ord(char) for char in key) % self.size

    def agregar(self, key, value):
        index = self.hash_function(key)
        bucket = self.buckets[index]

        # Verifica que la key no exista
        for elemento in bucket:
            if elemento[0] == key:
                print(f"La key '{key}' ya existe.")
                return

        bucket.append((key, value))
        print(f"('{key}', '{value}') agregado correctamente.")

    def eliminar(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]

        for elemento in bucket:
            if elemento[0] == key:
                bucket.remove(elemento)
                print(f"'{key}' eliminado.")
                return

        print(f"'{key}' no se encontró.")

    def buscar(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]

        for elemento in bucket:
            if elemento[0] == key:
                print(f"'{key}' encontrado. Value = {elemento[1]}")
                return elemento[1]

        print(f"'{key}' no existe.")
        return None

    def modificar(self, key, nuevo_value):
        index = self.hash_function(key)
        bucket = self.buckets[index]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i] = (key, nuevo_value)
                print(f"'{key}' actualizado correctamente.")
                return

        print(f"'{key}' no existe.")

    def mostrar(self):
        print("\n------ HASH MAP ------")
        for i, bucket in enumerate(self.buckets):
            print(f"Bucket {i}: {bucket}")


# ---------------- PROGRAMA PRINCIPAL ----------------

hash_map = HashMap(10)

# Agregar elementos
hash_map.agregar("Rojic", "Capitan")
hash_map.agregar("Eduardito", "Delantero")
hash_map.agregar("Felipe", "Arquero")
hash_map.agregar("Ian Dav", "Defensor")
hash_map.agregar("Moretti", "Mediocampista")
hash_map.agregar("Nachito", "Suplente")
hash_map.agregar("TTT Sahur", "DT")
hash_map.agregar("Joao", "Ayudante")

# Intentar agregar una key repetida
hash_map.agregar("Felipe", "Otro")

# Mostrar Hash Map
hash_map.mostrar()

# BuscarC:\Users\Usuario\Desktop\programacion_orientada_a_objetos\Hash Tables (Set & Map)\Ej_5.py
hash_map.buscar("Rojic")
hash_map.buscar("Tralalero")

# Modificar un value
hash_map.modificar("Joao", "Capitán suplente")

# Buscar nuevamente
hash_map.buscar("Joao")

# Eliminar
hash_map.eliminar("Moretti")

# Mostrar nuevamente
hash_map.mostrar()