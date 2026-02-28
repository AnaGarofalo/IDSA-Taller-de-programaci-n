# Tips para los ejercicios

## Ejercicio simple (Coleccion y Pila)

### Clase abstracta Coleccion

Usá `ABC` y `@abstractmethod` del módulo `abc`:

```python
from abc import ABC, abstractmethod

class Coleccion(ABC):
    @abstractmethod
    def agregar(self, elemento):
        pass
```

Con `@abstractmethod`, Python no deja instanciar la clase directamente ni crear subclases que no implementen todos los métodos.

### Clase Pila

Usá una lista interna para guardar los elementos. Recordá que es LIFO (el último en entrar es el primero en salir).

Métodos útiles de lista:
- `append(x)` → agrega al final
- `pop()` → saca del final y lo devuelve
- `lista[-1]` → accede al último elemento

Para `sacar()` y `primero()`, verificá primero si está vacía para devolver `None`.

### El método `__iter__`

Este método permite usar `for elemento in pila:`. Usá `yield` para devolver elementos uno por uno.

Para una pila, querés recorrer del tope (último) hacia la base (primero):

```python
def __iter__(self):
    for i in range(len(self.elementos) - 1, -1, -1):
        yield self.elementos[i]
```

---

## Ejercicio complejo (Cola)

### Heredar de Coleccion

Acordate de importar Coleccion del ejercicio simple:

```python
from ejercicio_simple import Coleccion

class Cola(Coleccion):
    ...
```

### Diferencia con Pila

La Cola es FIFO: el primero en entrar es el primero en salir.

- `append(x)` → agrega al final (igual que pila)
- `pop(0)` → saca del **principio** (diferente a pila)
- `lista[0]` → accede al **primer** elemento

### El método `__iter__`

Para una cola, recorrés del frente hacia el final (orden normal):

```python
def __iter__(self):
    for elemento in self.elementos:
        yield elemento
```

---

## Sobre polimorfismo

Una vez que tengas las dos clases, probá este código:

```python
def vaciar(coleccion):
    while not coleccion.esta_vacia():
        print(coleccion.sacar())

vaciar(Pila())   # Funciona
vaciar(Cola())   # También funciona!
```

El mismo código funciona con ambas clases porque comparten la misma interfaz (los mismos métodos). ¡Eso es polimorfismo!
