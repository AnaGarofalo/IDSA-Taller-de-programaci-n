# Búsqueda en Listas

## ¿Para qué sirve buscar?

Buscar un elemento en una lista es algo que hacemos todo el tiempo al programar:
- ¿Está este usuario en la base de datos?
- ¿Existe este producto en el inventario?
- ¿En qué posición está este valor?

Hay dos formas principales de buscar: lineal y binaria.

## Búsqueda Lineal

Es la forma más simple e intuitiva: revisás elemento por elemento hasta encontrar lo que buscás (o hasta llegar al final sin encontrarlo).

### ¿Cómo funciona?

1. Empezá por el primer elemento
2. ¿Es el que buscás? Si sí, ¡listo!
3. Si no, pasá al siguiente
4. Repetí hasta encontrarlo o llegar al final

### Ejemplo paso a paso

Buscar el número `7` en la lista `[3, 1, 7, 4, 9]`

```
Posición 0: ¿3 == 7? No → sigo
Posición 1: ¿1 == 7? No → sigo
Posición 2: ¿7 == 7? ¡Sí! → devuelvo posición 2
```

### Ventajas y desventajas

✅ Funciona con cualquier lista (ordenada o no)
✅ Muy simple de implementar
❌ Lenta para listas grandes (hay que revisar todo)

## Búsqueda Binaria

Es mucho más rápida, pero solo funciona si la lista está ordenada.

### La idea

Pensá en cómo buscás una palabra en el diccionario: no empezás por la A y vas página por página. Abrís por la mitad, ves si te pasaste o te quedaste corto, y vas ajustando.

### ¿Cómo funciona?

1. Mirá el elemento del medio
2. Si es el que buscás, ¡listo!
3. Si el que buscás es menor, descartá la mitad derecha
4. Si el que buscás es mayor, descartá la mitad izquierda
5. Repetí con la mitad que quedó

### Ejemplo paso a paso

Buscar el número `7` en la lista `[1, 3, 4, 7, 9, 12, 15]`

```
Lista completa: [1, 3, 4, 7, 9, 12, 15]
                         ↑
                  Medio = 7

¿7 == 7? ¡Sí! → devuelvo posición 3
```

Otro ejemplo: buscar `9` en la misma lista

```
Paso 1: [1, 3, 4, 7, 9, 12, 15]
                 ↑
          Medio = 7
        ¿9 == 7? No, 9 > 7 → busco en la mitad derecha

Paso 2: [9, 12, 15]
            ↑
       Medio = 12
       ¿9 == 12? No, 9 < 12 → busco en la mitad izquierda

Paso 3: [9]
         ↑
    ¿9 == 9? ¡Sí! → encontrado
```

### Ventajas y desventajas

✅ Muy rápida (en cada paso descartás la mitad)
✅ Ideal para listas grandes
❌ Solo funciona con listas ordenadas
❌ Un poco más compleja de implementar

## Comparación de velocidad

Para una lista de 1,000,000 elementos:
- **Búsqueda lineal**: hasta 1,000,000 comparaciones
- **Búsqueda binaria**: máximo 20 comparaciones

¡La diferencia es enorme!

## Ejercicios

1. **ejercicio_simple.py**: Implementá búsqueda lineal
2. **ejercicio_complejo.py**: Implementá búsqueda binaria (versión iterativa)
