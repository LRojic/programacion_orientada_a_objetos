"""Implementá en python utilizando clases un hash set. 
Acordate de utilizar buckets, de que cada key sea única,
 de definir una función hash dentro de tu clase, 
 y de resolver correctamente posibles colisiones. 
 Asegurate de agregar los siguientes métodos:
Agregar un elemento
Eliminar un elemento
Buscar un elemento
Muestre en pantalla el hash set entero
"""

class HashSet:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash_function(self, key):
        # Calcula el índice del bucket
        return sum(ord(char) for char in key) % self.size

    def agregar(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]

        # Solo agrega si la key no existe
        if key not in bucket:
            bucket.append(key)
            print(f"'{key}' agregado correctamente.")
        else:
            print(f"'{key}' ya existe en el Hash Set.")

    def eliminar(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]

        if key in bucket:
            bucket.remove(key)
            print(f"'{key}' eliminado.")
        else:
            print(f"'{key}' no se encontró.")

    def buscar(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]

        if key in bucket:
            print(f"'{key}' SI está en el Hash Set.")
            return True
        else:
            print(f"'{key}' NO está en el Hash Set.")
            return False

    def mostrar(self):
        print("\n----- HASH SET -----")
        for i, bucket in enumerate(self.buckets):
            print(f"Bucket {i}: {bucket}")


# ------------------------------------


hash_set = HashSet(10)
# Agregar elementos
hash_set.agregar("Rojic")
hash_set.agregar("Eduardito")
hash_set.agregar("Felipe")
hash_set.agregar("Ian Dav")
hash_set.agregar("Moretti")
hash_set.agregar("Nachito")
hash_set.agregar("TTT Sahur")
hash_set.agregar("Joao")

# Intentar agregar un elemento repetido
hash_set.agregar("Felipe")

# Mostrar el Hash Set
hash_set.mostrar()

# Buscar elementos
hash_set.buscar("Rojic")
hash_set.buscar("tralaloro")

# Eliminar un elemento
hash_set.eliminar("Moretti")

# Mostrar nuevamente
hash_set.mostrar()

# Buscar otra vez
hash_set.buscar("Moretti")