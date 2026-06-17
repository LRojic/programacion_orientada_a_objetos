"""En una hash table con un arreglo asociado de tamaño 11, vamos insertando las 
siguientes keys en este orden: 9, 26, 50, 15, 2, 21, 36, 22 y 32. Para cada uno 
de los métodos de resolución de colisiones que están acá abajo, mostrá cómo queda 
la estructura interna de la tabla después de hacer todas las inserciones.
Exploración lineal (linear probing). Suponé que el arreglo nunca se redimensiona.
Encadenamiento separado (separate chaining, que es un método de open addressing).
"""

"""
n = 11
# Hash table con separate chaining
tabla = [[] for _ in range(n)]

# Keys a insertar
keys = [9, 26, 50, 15, 2, 21, 36, 22, 32]

# Inserción
for key in keys:
    indice = key % n
    tabla[indice].append(key)

# Mostrar la tabla
for i in range(n):
    print(f"Bucket {i}: {tabla[i]}")"""

###############################################
"""
# 1. Exploración lineal (Linear Probing)
La tabla tiene 11 buckets, por lo que el índice se calcula con:

índice = key % 11

Inserciones

9
9 % 11 = 9
Va al bucket 9.

26

26 % 11 = 4
Va al bucket 4.

50

```text
50 % 11 = 6
```

Va al bucket 6.

15

```text
15 % 11 = 4

El bucket 4 está ocupado por 26.

Se busca el siguiente bucket libre:

```text
4 → ocupado
5 → libre
```

15 se guarda en el bucket 5.

2

```text
2 % 11 = 2
```

Va al bucket 2.

21

```text
21 % 11 = 10
```

Va al bucket 10.

36

```text
36 % 11 = 3
```

Va al bucket 3.

22

```text
22 % 11 = 0
```

Va al bucket 0.

32

```text
32 % 11 = 10
```

El bucket 10 está ocupado por 21.

Se busca el siguiente bucket libre:

```text
10 → ocupado
0 → ocupado
1 → libre
```

32 se guarda en el bucket 1.

Tabla final (Linear Probing)

| Bucket | Contenido |
| ------ | --------- |
| 0      | 22        |
| 1      | 32        |
| 2      | 2         |
| 3      | 36        |
| 4      | 26        |
| 5      | 15        |
| 6      | 50        |
| 7      | Vacío     |
| 8      | Vacío     |
| 9      | 9         |
| 10     | 21        |

# 2. Encadenamiento separado (Separate Chaining)

La tabla también tiene 11 buckets, por lo que el índice se calcula con:

índice = key % 11

En este método, cuando dos claves caen en el mismo bucket, se agregan a una cadena (lista) dentro de ese bucket.

Inserciones

9

```text
9 % 11 = 9
```

Bucket 9:

```text
9
```

26

```text
26 % 11 = 4
```

Bucket 4:

```text
26
```

50

```text
50 % 11 = 6
```

Bucket 6:

```text
50
```

15

```text
15 % 11 = 4
```

El bucket 4 ya contiene el 26, por lo que se agrega a la cadena.

Bucket 4:

```text
26
↓
15
```

2

```text
2 % 11 = 2
```

Bucket 2:

```text
2
```

21

```text
21 % 11 = 10
```

Bucket 10:

```text
21
```

36

```text
36 % 11 = 3
```

Bucket 3:

```text
36
```

22

```text
22 % 11 = 0
```

Bucket 0:

```text
22
```

32

```text
32 % 11 = 10
```

El bucket 10 ya contiene el 21, por lo que se agrega a la cadena.

Bucket 10:

```text
21
↓
32
```

Tabla final (Separate Chaining)

| Bucket | Cadena  |
| ------ | ------- |
| 0      | 22      |
| 1      | Vacío   |
| 2      | 2       |
| 3      | 36      |
| 4      | 26 → 15 |
| 5      | Vacío   |
| 6      | 50      |
| 7      | Vacío   |
| 8      | Vacío   |
| 9      | 9       |
| 10     | 21 → 32 |
"""