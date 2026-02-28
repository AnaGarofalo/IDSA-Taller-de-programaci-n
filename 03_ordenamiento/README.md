# Ordenamiento de Listas

## ¿Para qué sirve ordenar?

Imaginate que tenés una lista de nombres y querés encontrar uno específico. Si la lista está desordenada, tenés que revisar uno por uno. Pero si está ordenada alfabéticamente, podés buscarlo mucho más rápido.

Ordenar datos es una de las operaciones más comunes en programación. Sirve para:
- Buscar información más rápido
- Mostrar datos de forma organizada (precios de menor a mayor, fechas cronológicas)
- Detectar duplicados fácilmente

## Bubble Sort (Ordenamiento Burbuja)

Es el algoritmo de ordenamiento más simple de entender. Se llama "burbuja" porque los elementos más grandes van "subiendo" hacia el final de la lista, como burbujas en el agua.

### ¿Cómo funciona?

1. Recorré la lista comparando elementos de a pares (el primero con el segundo, el segundo con el tercero, etc.)
2. Si un elemento es mayor que el siguiente, intercambialos
3. Repetí el proceso hasta que no haya más intercambios

### Ejemplo paso a paso

Lista inicial: `[5, 3, 8, 1]`

**Primera pasada:**
```
[5, 3, 8, 1]  →  5 > 3? Sí, intercambiar  →  [3, 5, 8, 1]
[3, 5, 8, 1]  →  5 > 8? No                →  [3, 5, 8, 1]
[3, 5, 8, 1]  →  8 > 1? Sí, intercambiar  →  [3, 5, 1, 8]
```

**Segunda pasada:**
```
[3, 5, 1, 8]  →  3 > 5? No                →  [3, 5, 1, 8]
[3, 5, 1, 8]  →  5 > 1? Sí, intercambiar  →  [3, 1, 5, 8]
[3, 1, 5, 8]  →  5 > 8? No                →  [3, 1, 5, 8]
```

**Tercera pasada:**
```
[3, 1, 5, 8]  →  3 > 1? Sí, intercambiar  →  [1, 3, 5, 8]
[1, 3, 5, 8]  →  3 > 5? No                →  [1, 3, 5, 8]
[1, 3, 5, 8]  →  5 > 8? No                →  [1, 3, 5, 8]
```

**Cuarta pasada:** No hay intercambios → ¡Lista ordenada!

Resultado final: `[1, 3, 5, 8]`

## Selection Sort (Ordenamiento por Selección)

Otro algoritmo simple. La idea es: buscá el elemento más pequeño y ponelo primero, después buscá el siguiente más pequeño y ponelo segundo, y así sucesivamente.

### Ejemplo paso a paso

Lista inicial: `[5, 3, 8, 1]`

```
Buscar el mínimo en [5, 3, 8, 1] → Es 1, intercambiar con el primero → [1, 3, 8, 5]
Buscar el mínimo en [3, 8, 5]   → Es 3, ya está en su lugar        → [1, 3, 8, 5]
Buscar el mínimo en [8, 5]      → Es 5, intercambiar con 8         → [1, 3, 5, 8]
```

Resultado final: `[1, 3, 5, 8]`

## ¿Cuál usar?

Ambos algoritmos son simples pero lentos para listas grandes. En la práctica, Python tiene `sorted()` y `.sort()` que son mucho más eficientes. Pero entender estos algoritmos te ayuda a pensar cómo funcionan los procesos de ordenamiento.

## Ejercicios

1. **ejercicio_simple.py**: Implementá bubble sort
2. **ejercicio_complejo.py**: Ordená una lista de diccionarios por una clave específica
