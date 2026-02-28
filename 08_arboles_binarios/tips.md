# Tips para los ejercicios

## Ejercicio simple (agregar y contiene)

Ambos métodos se pueden implementar con recursividad o con un loop while.

### Para agregar:
- Si el árbol está vacío, el nuevo nodo es la raíz
- Si no, compará el valor con el nodo actual:
  - Si es menor, andá a la izquierda
  - Si es mayor o igual, andá a la derecha
- Repetí hasta encontrar un lugar vacío (None)

### Para contiene:
- Si llegás a None, el valor no está
- Si encontrás el valor, devolvé True
- Si el valor es menor, buscá a la izquierda
- Si el valor es mayor, buscá a la derecha

### Tip de recursividad:
Podés crear funciones auxiliares como `_agregar_recursivo(nodo, valor)` que reciben el nodo actual.

## Ejercicio complejo (recorrido_inorden)

El recorrido inorden es recursivo por naturaleza:

```
def inorden(nodo):
    si nodo es None: terminar
    inorden(nodo.izquierdo)   # 1. Recorrer izquierda
    visitar(nodo.valor)        # 2. Procesar raíz
    inorden(nodo.derecho)      # 3. Recorrer derecha
```

Podés usar una lista para acumular los valores, o usar `yield` para hacerlo con un generador.
