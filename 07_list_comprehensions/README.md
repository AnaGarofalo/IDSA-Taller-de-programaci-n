# List Comprehensions, Map y Filter

## ¿Qué problema resuelven?

Muchas veces necesitamos transformar o filtrar datos de una lista. En lugar de escribir varios líneas con loops, Python ofrece formas más concisas y eficientes.

---

## List Comprehensions

Es una forma compacta de crear listas basadas en otras listas.

### Sintaxis básica

```python
nueva_lista = [expresión for elemento in lista]
```

### Ejemplo: convertir a mayúsculas

```python
# Con loop tradicional
nombres = ["ana", "luis", "maría"]
mayusculas = []
for nombre in nombres:
    mayusculas.append(nombre.upper())

# Con list comprehension (1 línea)
mayusculas = [nombre.upper() for nombre in nombres]
# ["ANA", "LUIS", "MARÍA"]
```

### Ejemplo: calcular cuadrados

```python
numeros = [1, 2, 3, 4, 5]

# Loop tradicional
cuadrados = []
for n in numeros:
    cuadrados.append(n ** 2)

# Comprehension
cuadrados = [n ** 2 for n in numeros]
# [1, 4, 9, 16, 25]
```

---

## Comprehensions con filtro

Podés agregar una condición para incluir solo algunos elementos:

```python
nueva_lista = [expresión for elemento in lista if condición]
```

### Ejemplo: solo números pares

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [n for n in numeros if n % 2 == 0]
# [2, 4, 6, 8, 10]
```

### Ejemplo: palabras largas

```python
palabras = ["sol", "estrella", "luz", "universo"]
largas = [p for p in palabras if len(p) > 4]
# ["estrella", "universo"]
```

### Filtrar y transformar

```python
# Cuadrados de los números pares
numeros = [1, 2, 3, 4, 5, 6]
cuadrados_pares = [n ** 2 for n in numeros if n % 2 == 0]
# [4, 16, 36]
```

---

## Map: aplicar función a cada elemento

`map(función, lista)` aplica una función a cada elemento.

```python
numeros = [1, 2, 3, 4, 5]

# Usando map
cuadrados = list(map(lambda x: x ** 2, numeros))
# [1, 4, 9, 16, 25]

# Equivalente con comprehension
cuadrados = [x ** 2 for x in numeros]
```

### Con funciones existentes

```python
numeros = ["1", "2", "3"]
enteros = list(map(int, numeros))
# [1, 2, 3]

palabras = ["hola", "mundo"]
mayusculas = list(map(str.upper, palabras))
# ["HOLA", "MUNDO"]
```

---

## Filter: seleccionar elementos

`filter(función, lista)` mantiene los elementos donde la función devuelve `True`.

```python
numeros = [1, 2, 3, 4, 5, 6]

# Usando filter
pares = list(filter(lambda x: x % 2 == 0, numeros))
# [2, 4, 6]

# Equivalente con comprehension
pares = [x for x in numeros if x % 2 == 0]
```

### Filtrar valores "truthy"

```python
datos = [0, 1, "", "hola", None, 42, [], [1, 2]]
validos = list(filter(None, datos))
# [1, "hola", 42, [1, 2]]  # Solo valores "truthy"
```

---

## Lambda: funciones pequeñas en una línea

Las funciones lambda son funciones anónimas (sin nombre) para casos simples:

```python
# Función normal
def doble(x):
    return x * 2

# Lambda equivalente
doble = lambda x: x * 2
```

### Uso con map y filter

```python
# Sumar 10 a cada elemento
list(map(lambda x: x + 10, [1, 2, 3]))
# [11, 12, 13]

# Filtrar mayores a 5
list(filter(lambda x: x > 5, [3, 6, 9, 2, 8]))
# [6, 9, 8]
```

---

## Comparación: ¿Cuándo usar cada uno?

| Situación | Recomendación |
|-----------|---------------|
| Transformar y filtrar | List comprehension |
| Solo transformar | Comprehension o map |
| Solo filtrar | Comprehension o filter |
| Función ya existente | map/filter |
| Muy complejo | Loop tradicional |

### Regla general

- **List comprehension**: Cuando la lógica es simple y clara
- **map/filter**: Cuando ya tenés una función definida
- **Loop**: Cuando necesitás lógica más compleja

---

## Dictionary comprehension (bonus)

También funciona para crear diccionarios:

```python
numeros = [1, 2, 3, 4, 5]
cuadrados = {n: n**2 for n in numeros}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

## Ejercicios

1. **ejercicio_simple.py**: Obtener cuadrados de números pares
2. **ejercicio_complejo.py**: Procesar y filtrar una lista de diccionarios
