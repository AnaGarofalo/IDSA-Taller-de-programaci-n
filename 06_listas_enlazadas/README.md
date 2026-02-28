# Listas Enlazadas

## ¿Qué problema resuelven?

Las listas de Python son muy útiles, pero tienen una limitación: insertar o eliminar elementos al principio o en el medio es lento porque hay que mover todos los demás elementos.

Las listas enlazadas resuelven esto: cada elemento "apunta" al siguiente, así que insertar o eliminar es solo cuestión de cambiar un par de referencias.

---

## La idea: nodos conectados

Imaginá una cadena donde cada eslabón tiene:
1. Un **valor** (el dato que guardamos)
2. Una **referencia al siguiente** eslabón

```
[valor: 5] → [valor: 10] → [valor: 3] → None
```

Cada "eslabón" se llama **nodo**. El último nodo apunta a `None` (no hay más).

---

## Estructura de un nodo

```python
class Nodo:
    def __init__(self, valor):
        self.valor = valor      # El dato
        self.siguiente = None   # Referencia al próximo nodo
```

### Ejemplo visual

Si queremos guardar los números 1, 2, 3:

```
cabeza
  ↓
[1|→] → [2|→] → [3|None]
```

Cada caja `[valor|siguiente]` es un nodo.

---

## Estructura de la lista enlazada

```python
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # El primer nodo
```

La lista solo necesita saber dónde empieza (la "cabeza"). Desde ahí, podemos llegar a cualquier nodo siguiendo las referencias.

---

## Operaciones básicas

### Agregar al final

Para agregar un elemento:
1. Crear un nuevo nodo
2. Si la lista está vacía, el nuevo nodo es la cabeza
3. Si no, recorrer hasta el último nodo y conectar el nuevo

```
Antes: [1|→] → [2|→] → [3|None]

Agregar 4:

[1|→] → [2|→] → [3|→] → [4|None]
                   ↑
                cambiamos el siguiente de 3
```

### Recorrer la lista

Para ver todos los elementos:
1. Empezar en la cabeza
2. Mientras haya nodo: leer valor, pasar al siguiente

```python
actual = self.cabeza
while actual is not None:
    print(actual.valor)
    actual = actual.siguiente
```

---

## Comparación con listas de Python

| Operación | Lista Python | Lista Enlazada |
|-----------|--------------|----------------|
| Acceder por índice | Rápido O(1) | Lento O(n) |
| Agregar al final | Rápido O(1)* | Lento O(n)** |
| Agregar al inicio | Lento O(n) | Rápido O(1) |
| Insertar en medio | Lento O(n) | Rápido O(1)*** |
| Buscar elemento | O(n) | O(n) |

*Amortizado
**Se puede hacer O(1) guardando referencia al último
***Una vez que tenés la posición

### ¿Cuándo usar listas enlazadas?

- Muchas inserciones/eliminaciones al inicio
- No necesitás acceso por índice
- Implementar pilas o colas

### ¿Cuándo usar listas de Python?

- Acceso frecuente por índice
- La mayoría de los casos en Python

---

## Tipos de listas enlazadas

### Simple (la que vemos hoy)
Cada nodo apunta solo al siguiente.

```
[A] → [B] → [C] → None
```

### Doblemente enlazada
Cada nodo apunta al siguiente Y al anterior.

```
None ← [A] ⇄ [B] ⇄ [C] → None
```

### Circular
El último nodo apunta al primero.

```
[A] → [B] → [C] → [A] → ...
```

---

## Sobrecarga de métodos (a la Python)

En lenguajes como Java, podés tener varios métodos con el mismo nombre pero diferentes parámetros (sobrecarga):

```java
// Java - sobrecarga real
void agregar(int valor) { ... }
void agregar(int valor, int posicion) { ... }
```

**Python no tiene sobrecarga real.** Si definís el mismo método dos veces, el segundo sobrescribe al primero. Pero podés simular sobrecarga usando **parámetros con valores por defecto**:

```python
# Python - "sobrecarga" con valores por defecto
def agregar(self, valor, posicion=0):
    """
    Agrega un valor en la posición indicada.
    Si no se especifica posición, agrega al principio.
    """
    ...
```

Esto permite llamar al método de dos formas:

```python
lista.agregar(5)      # Agrega al principio (posicion=0 por defecto)
lista.agregar(5, 2)   # Agrega en la posición 2
```

Un solo método, múltiples formas de usarlo. ¡Eso es sobrecarga pythónica!

---

## ¿Por qué aprenderlas?

Aunque en Python casi siempre usamos listas normales, entender listas enlazadas:

1. Te ayuda a entender cómo funcionan las estructuras de datos "por dentro"
2. Son la base de otras estructuras (árboles, grafos)
3. Aparecen en entrevistas técnicas
4. Son útiles en lenguajes de bajo nivel (C, C++)

---

## Ejercicios

1. **ejercicio_simple.py**: Implementar `agregar(valor, posicion=0)` con sobrecarga pythónica
2. **ejercicio_complejo.py**: Implementar `invertir()` la lista
