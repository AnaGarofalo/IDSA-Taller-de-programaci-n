# Complejidad Algorítmica

## ¿Por qué importa?

¿Por qué un programa tarda 1 segundo y otro tarda 3 horas haciendo "lo mismo"? La respuesta está en la complejidad algorítmica: cómo crece el tiempo de ejecución cuando crece la cantidad de datos.

Entender esto te permite:
- Elegir la solución más eficiente
- Predecir si tu código va a funcionar con datos grandes
- Identificar cuellos de botella

## Notación Big O

Usamos **O(algo)** para describir cómo crece el tiempo de ejecución. Nos importa el peor caso y cómo escala, no el tiempo exacto.

### Las complejidades más comunes

| Notación | Nombre | Ejemplo | ¿Escala bien? |
|----------|--------|---------|---------------|
| O(1) | Constante | Acceder a lista[0] | Excelente |
| O(log n) | Logarítmica | Búsqueda binaria | Muy bueno |
| O(n) | Lineal | Recorrer una lista | Bueno |
| O(n log n) | Linearítmica | Ordenar con sorted() | Aceptable |
| O(n²) | Cuadrática | Doble loop anidado | Malo |
| O(n³) | Cúbica | Triple loop anidado | Muy malo |
| O(2ⁿ) | Exponencial | Fuerza bruta | Terrible |

### ¿Qué significa en la práctica?

Para una lista de **1,000,000 elementos**:

| Complejidad | Operaciones aproximadas |
|-------------|------------------------|
| O(1) | 1 |
| O(log n) | 20 |
| O(n) | 1,000,000 |
| O(n log n) | 20,000,000 |
| O(n²) | 1,000,000,000,000 |

¡La diferencia entre O(n) y O(n²) puede ser de segundos vs días!

---

## Cómo identificar la complejidad

### O(1) - Constante

El tiempo no depende del tamaño de los datos.

```python
def primero(lista):
    return lista[0]  # O(1) - siempre hace 1 operación

def es_par(numero):
    return numero % 2 == 0  # O(1)
```

### O(n) - Lineal

Un loop que recorre todos los elementos.

```python
def sumar(lista):
    total = 0
    for x in lista:  # Se ejecuta n veces
        total += x
    return total
```

### O(n²) - Cuadrática

Un loop dentro de otro loop.

```python
def pares(lista):
    for i in lista:       # n veces
        for j in lista:   # n veces por cada i
            print(i, j)   # Total: n × n = n²
```

### O(log n) - Logarítmica

Cada paso reduce el problema a la mitad.

```python
def busqueda_binaria(lista, objetivo):
    # En cada paso, descartamos la mitad
    # Con 1000 elementos: ~10 pasos
    # Con 1,000,000: ~20 pasos
```

---

## Reglas simples para analizar

1. **Operaciones simples**: O(1)
   - Acceso a índice, asignación, comparación, operación matemática

2. **Un loop sobre n elementos**: O(n)
   - `for x in lista`

3. **Loops anidados**: Multiplicar
   - 2 loops anidados sobre n: O(n × n) = O(n²)
   - 3 loops anidados: O(n³)

4. **Loops secuenciales**: Quedarse con el mayor
   - O(n) + O(n²) = O(n²)

5. **Dividir a la mitad**: O(log n)
   - Búsqueda binaria, árboles balanceados

---

## Ejemplos de optimización

### Malo: O(n²)
```python
def tiene_duplicados_lento(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False
```

### Bueno: O(n)
```python
def tiene_duplicados_rapido(lista):
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return True
        vistos.add(elemento)
    return False
```

La versión rápida usa un `set`, donde buscar es O(1) en promedio.

---

## Tips para código más eficiente

- **Usar sets para búsquedas**: `x in set` es O(1), `x in lista` es O(n)
- **Usar diccionarios para lookups**: Acceso por clave es O(1)
- **Evitar loops anidados innecesarios**: Buscar alternativas con estructuras de datos
- **sorted() es O(n log n)**: Úsalo con confianza
- **Cuidado con operaciones ocultas**: `lista.count(x)` es O(n) cada vez que lo llamás

---

## Ejercicios

1. **ejercicio_simple.py**: Identificar la complejidad de funciones dadas
2. **ejercicio_complejo.py**: Optimizar una función de O(n²) a O(n)
