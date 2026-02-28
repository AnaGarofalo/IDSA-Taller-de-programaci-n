# Árboles Binarios de Búsqueda

## ¿Qué es un árbol binario?

Un árbol binario es una estructura de datos donde cada nodo tiene como máximo dos hijos: izquierdo y derecho.

```
        5
       / \
      3   8
     / \   \
    1   4   9
```

## ¿Qué es un árbol binario de búsqueda (BST)?

Es un árbol binario con una regla especial:
- Los valores **menores** van a la **izquierda**
- Los valores **mayores** van a la **derecha**

Esta regla se aplica en cada nodo, recursivamente.

### Ejemplo paso a paso

Insertando los valores: 5, 3, 8, 1, 4, 9

```
Insertar 5:     5

Insertar 3:     5       (3 < 5, va a la izquierda)
               /
              3

Insertar 8:     5       (8 > 5, va a la derecha)
               / \
              3   8

Insertar 1:     5       (1 < 5, izq; 1 < 3, izq)
               / \
              3   8
             /
            1

Insertar 4:     5       (4 < 5, izq; 4 > 3, der)
               / \
              3   8
             / \
            1   4

Insertar 9:     5       (9 > 5, der; 9 > 8, der)
               / \
              3   8
             / \   \
            1   4   9
```

---

## Estructura en código

```python
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None
```

---

## ¿Por qué usar árboles binarios de búsqueda?

### Búsqueda eficiente

En una lista, buscar un elemento es O(n) - hay que revisar todos.

En un BST balanceado, buscar es O(log n) - en cada paso eliminamos la mitad.

```
Buscar 4 en el árbol:
    5  → 4 < 5, voy a la izquierda
   /
  3   → 4 > 3, voy a la derecha
   \
    4  → ¡Encontrado! (solo 3 pasos)
```

### Comparación de complejidad

| Operación | Lista | BST (balanceado) |
|-----------|-------|------------------|
| Buscar    | O(n)  | O(log n)         |
| Insertar  | O(1)* | O(log n)         |
| Eliminar  | O(n)  | O(log n)         |

*Insertar al final de una lista es O(1), pero insertar ordenado es O(n).

---

## Recorridos del árbol

Hay tres formas clásicas de recorrer un árbol:

### Inorden (izquierda → raíz → derecha)
Visita los nodos en **orden ascendente**.

```
        5
       / \
      3   8
     / \   \
    1   4   9

Inorden: 1, 3, 4, 5, 8, 9  ← ¡Ordenado!
```

### Preorden (raíz → izquierda → derecha)
Útil para copiar el árbol.

```
Preorden: 5, 3, 1, 4, 8, 9
```

### Postorden (izquierda → derecha → raíz)
Útil para eliminar el árbol.

```
Postorden: 1, 4, 3, 9, 8, 5
```

---

## Casos especiales

### Árbol vacío
```python
arbol = ArbolBinario()
arbol.raiz  # None
```

### Árbol desbalanceado
Si insertamos valores ya ordenados, el árbol se convierte en una lista:

```
Insertar: 1, 2, 3, 4, 5

1
 \
  2
   \
    3
     \
      4
       \
        5

¡Esto es básicamente una lista enlazada!
Búsqueda vuelve a ser O(n).
```

Por eso existen los árboles balanceados (AVL, Red-Black), pero eso es tema avanzado.

---

## Ejercicios

1. **ejercicio_simple.py**: Implementar `agregar(valor)` y `contiene(valor)`
2. **ejercicio_complejo.py**: Implementar `recorrido_inorden()` que devuelve los valores ordenados
