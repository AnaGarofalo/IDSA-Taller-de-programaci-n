# Pilas y Colas

## ¿Para qué sirven?

Son formas de organizar datos donde importa el orden en que entran y salen los elementos. Las usamos todo el tiempo sin darnos cuenta:

- **Pila**: Como una pila de platos. El último que ponés es el primero que sacás.
- **Cola**: Como la cola del supermercado. El primero que llega es el primero en ser atendido.

---

## Pilas (Stack) - LIFO

**LIFO** = Last In, First Out (Último en entrar, primero en salir)

### Analogía del mundo real

Pensá en una pila de libros sobre una mesa. Solo podés:
- Agregar un libro arriba de todo
- Sacar el libro de arriba

No podés sacar el de abajo sin sacar los de arriba primero.

### Operaciones básicas

- **push**: Agregar un elemento arriba de la pila
- **pop**: Sacar el elemento de arriba
- **peek/top**: Ver el elemento de arriba (sin sacarlo)

### Ejemplo visual

```
Operación          Pila (el de arriba es el último)
---------          ----
inicial            []
push(1)            [1]
push(2)            [1, 2]
push(3)            [1, 2, 3]
pop() → 3          [1, 2]
pop() → 2          [1]
push(4)            [1, 4]
```

### Implementación simple en Python

```python
pila = []
pila.append(1)      # push
pila.append(2)
elemento = pila.pop()  # saca el 2
```

### ¿Cuándo usar pilas?

- Deshacer/rehacer en editores de texto
- El botón "atrás" del navegador
- Verificar paréntesis balanceados
- Evaluar expresiones matemáticas

---

## Colas (Queue) - FIFO

**FIFO** = First In, First Out (Primero en entrar, primero en salir)

### Analogía del mundo real

Una cola en el banco: el primero que llegó es el primero en ser atendido. No podés saltearte la fila.

### Operaciones básicas

- **enqueue** (encolar): Agregar un elemento al final
- **dequeue** (desencolar): Sacar el elemento del frente
- **front**: Ver el elemento del frente (sin sacarlo)

### Ejemplo visual

```
Operación          Cola [frente ... final]
---------          ----
inicial            []
enqueue(1)         [1]
enqueue(2)         [1, 2]
enqueue(3)         [1, 2, 3]
dequeue() → 1      [2, 3]
dequeue() → 2      [3]
enqueue(4)         [3, 4]
```

### Implementación simple en Python

```python
from collections import deque

cola = deque()
cola.append(1)      # enqueue (agregar al final)
cola.append(2)
elemento = cola.popleft()  # dequeue (sacar del frente) → 1
```

### ¿Cuándo usar colas?

- Sistema de turnos
- Procesar tareas en orden de llegada
- Cola de impresión
- Mensajes pendientes de enviar

---

## Comparación rápida

| Característica | Pila (Stack) | Cola (Queue) |
|----------------|--------------|--------------|
| Orden          | LIFO         | FIFO         |
| Agregar        | Por arriba   | Por el final |
| Sacar          | Por arriba   | Por el frente|
| Analogía       | Pila de platos | Fila de personas |

---

## Ejercicios

1. **ejercicio_simple.py**: Verificar paréntesis balanceados (usa pila)
2. **ejercicio_complejo.py**: Implementar un sistema de cola de atención
