# Recursividad

## ¿Qué es la recursividad?

Una función recursiva es una función que se llama a sí misma. Parece raro al principio, pero es una forma muy elegante de resolver ciertos problemas.

### Una analogía

Imaginá que querés saber cuántas personas hay en una fila muy larga. Podrías contar una por una (forma iterativa), o podrías preguntarle a la primera persona: "¿Cuántos hay detrás tuyo?", y esa persona le pregunta a la siguiente, y así sucesivamente hasta llegar al último que dice "ninguno". Luego cada persona suma 1 a la respuesta que le dieron.

Eso es recursividad: resolver un problema pidiéndole a alguien que resuelva una versión más pequeña del mismo problema.

## Las dos partes fundamentales

Toda función recursiva necesita:

### 1. Caso base
Es la condición de parada. Sin esto, la función se llamaría infinitamente.

### 2. Caso recursivo
Es donde la función se llama a sí misma con un problema más pequeño.

## Ejemplo: Cuenta regresiva

Queremos imprimir los números del n al 1.

```python
def cuenta_regresiva(n):
    # Caso base: si n es 0, no hay nada que hacer
    if n == 0:
        return

    # Hacer algo con n
    print(n)

    # Caso recursivo: llamar con un problema más chico
    cuenta_regresiva(n - 1)
```

```
cuenta_regresiva(3)
# Imprime: 3, 2, 1
```

### ¿Qué pasa cuando llamamos cuenta_regresiva(3)?

```
cuenta_regresiva(3)
  → print(3)
  → cuenta_regresiva(2)
        → print(2)
        → cuenta_regresiva(1)
              → print(1)
              → cuenta_regresiva(0)
                    → return (caso base)
```

## Tips para pensar recursivamente

1. **Identificá el caso base**: ¿Cuál es el problema más simple que puedo resolver directamente?
2. **Reducí el problema**: ¿Cómo puedo hacer el problema un poco más pequeño?
3. **Confiá en la recursión**: Asumí que la llamada recursiva va a funcionar correctamente

## Cuándo usar recursividad

✅ Problemas que se pueden dividir en subproblemas similares
✅ Estructuras anidadas (listas dentro de listas, árboles)
✅ Cuando la solución recursiva es más clara que la iterativa

❌ Cuando hay muchísimas llamadas (puede ser lento o causar error de memoria)
❌ Si la versión iterativa es igual de simple

## Ejercicios

1. **ejercicio_simple.py**: Implementá factorial recursivo
2. **ejercicio_complejo.py**: Aplaná una lista con sublistas anidadas
