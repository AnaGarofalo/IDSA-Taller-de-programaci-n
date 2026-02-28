# Pilas y Colas - Herencia y Polimorfismo

## Programación Orientada a Objetos (POO)

Antes de ver pilas y colas, necesitamos entender algunos conceptos de POO.

### Herencia

La herencia permite crear una clase nueva basada en otra existente. La clase "hija" hereda los métodos y atributos de la clase "padre".

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        return "..."  # Comportamiento por defecto

class Perro(Animal):  # Perro hereda de Animal
    def hablar(self):  # Sobrescribe el método
        return "Guau!"

class Gato(Animal):   # Gato hereda de Animal
    def hablar(self):  # Sobrescribe el método
        return "Miau!"

class Pez(Animal):    # Pez hereda de Animal
    pass              # No sobrescribe hablar(), usa el de Animal
```

```python
# Podemos instanciar cualquiera de las clases
animal = Animal("Genérico")
perro = Perro("Firulais")
gato = Gato("Michi")
pez = Pez("Nemo")

print(animal.hablar())  # "..."   (usa el método de Animal)
print(perro.hablar())   # "Guau!" (usa su propio método)
print(gato.hablar())    # "Miau!" (usa su propio método)
print(pez.hablar())     # "..."   (hereda el método de Animal)
```

### Polimorfismo

Polimorfismo significa "muchas formas". Es cuando diferentes clases tienen el mismo método, pero cada una lo implementa de forma diferente.

```python
animales = [Animal("X"), Perro("Firulais"), Gato("Michi"), Pez("Nemo")]

for animal in animales:
    print(animal.hablar())  # Mismo método, diferente resultado
# Imprime:
# ...
# Guau!
# Miau!
# ...
```

El código que usa estos objetos no necesita saber qué tipo de animal es. Solo sabe que puede llamar a `hablar()` y cada uno responderá a su manera.

### Clase abstracta (ABC)

Una clase abstracta define la "interfaz" que deben seguir las clases hijas. Es como un contrato: "todas las clases que hereden de mí deben tener estos métodos".

```python
from abc import ABC, abstractmethod

class Coleccion(ABC):
    """Clase base abstracta para colecciones."""

    @abstractmethod
    def agregar(self, elemento):
        pass

    @abstractmethod
    def sacar(self):
        pass
```

- `ABC` = Abstract Base Class (clase base abstracta)
- `@abstractmethod` = indica que las subclases **deben** implementar este método

Si intentás instanciar `Coleccion()` directamente, Python lanza un error. Y si una subclase no implementa todos los métodos abstractos, también da error.

---

## Pilas y Colas

Ahora veamos dos estructuras de datos que comparten una interfaz común pero se comportan diferente.

### ¿Qué tienen en común?

Ambas son colecciones donde:
- Podés **agregar** elementos
- Podés **sacar** elementos
- Podés **ver el primero** sin sacarlo
- Podés verificar si **está vacía**
- Podés **recorrer** los elementos

### ¿En qué se diferencian?

| Estructura | Orden | Analogía |
|------------|-------|----------|
| **Pila** (Stack) | LIFO - Last In, First Out | Pila de platos |
| **Cola** (Queue) | FIFO - First In, First Out | Fila del banco |

### Pila (LIFO)

El último en entrar es el primero en salir.

```
Operación          Pila [base ... tope]
---------          ----
inicial            []
agregar(1)         [1]
agregar(2)         [1, 2]
agregar(3)         [1, 2, 3]
sacar() → 3        [1, 2]      ← sale el último
sacar() → 2        [1]
```

**Usos reales:**
- Ctrl+Z (deshacer)
- Botón "atrás" del navegador
- Llamadas a funciones en un programa

### Cola (FIFO)

El primero en entrar es el primero en salir.

```
Operación          Cola [frente ... final]
---------          ----
inicial            []
agregar(1)         [1]
agregar(2)         [1, 2]
agregar(3)         [1, 2, 3]
sacar() → 1        [2, 3]      ← sale el primero
sacar() → 2        [3]
```

**Usos reales:**
- Sistema de turnos
- Cola de impresión
- Mensajes pendientes

---

## Polimorfismo en acción

Una vez implementadas, podés usar Pila y Cola de forma intercambiable:

```python
def procesar(coleccion):
    """Funciona con cualquier Coleccion (Pila o Cola)."""
    coleccion.agregar("A")
    coleccion.agregar("B")
    coleccion.agregar("C")

    while not coleccion.esta_vacia():
        print(coleccion.sacar())

procesar(Pila())   # Imprime: C, B, A (LIFO)
procesar(Cola())   # Imprime: A, B, C (FIFO)
```

El mismo código produce resultados diferentes según el tipo de colección. ¡Eso es polimorfismo!

---

## Ejercicios

1. **ejercicio_simple.py**: Implementar la clase base `Coleccion` y la clase `Pila`
2. **ejercicio_complejo.py**: Implementar la clase `Cola` usando la misma interfaz
