"""
GLOSARIO - HASH TABLES

Hash Table (Tabla Hash):
→ Estructura de datos que almacena pares (clave, valor) y permite buscarlos muy rápido.

Clave (Key):
→ Dato que identifica un elemento (ej.: "Juan", 25, "abc123").

Valor (Value):
→ Información asociada a una clave.

Hash:
→ Número entero generado por la función hash a partir de una clave. Para una misma clave, siempre devuelve el mismo hash durante una misma ejecución del programa.

Función Hash:
→ Función que transforma una clave en un número entero (hash).

Bucket:
→ Cada posición de la tabla donde se almacenan los elementos.

Índice:
→ Posición final del bucket donde se guarda el elemento.
Se calcula generalmente como:
    hash(clave) % n

n:
→ Cantidad total de buckets de la tabla.

Colisión:
→ Ocurre cuando dos claves distintas generan el mismo índice.

Separate Chaining:
→ Método para resolver colisiones usando una lista (o lista enlazada) dentro de cada bucket.

Linear Probing:
→ Método para resolver colisiones buscando el siguiente bucket libre.

Insertar:
→ Guardar un elemento en la tabla.

Buscar:
→ Encontrar un elemento usando su clave.

Eliminar:
→ Quitar un elemento de la tabla.

Complejidad promedio:
→ Insertar: O(1)
→ Buscar: O(1)
→ Eliminar: O(1)

#$######################################

Clave
   │
   ▼
Función hash
   │
   ▼
Número hash (puede ser enorme)
   │
   ▼
hash(clave) % n
   │
   ▼
Índice del bucket
   │
   ▼
Se guarda o se busca el elemento

"""

