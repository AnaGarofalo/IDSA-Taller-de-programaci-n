"""
SOLUCIONES - No mirar hasta haber intentado resolver los ejercicios
"""

from abc import ABC, abstractmethod


# Ejercicio simple: Clase base Coleccion y Pila

class Coleccion(ABC):
    """Clase base abstracta para colecciones de elementos."""

    @abstractmethod
    def agregar(self, elemento):
        pass

    @abstractmethod
    def sacar(self):
        pass

    @abstractmethod
    def primero(self):
        pass

    @abstractmethod
    def esta_vacia(self):
        pass

    @abstractmethod
    def __iter__(self):
        pass


class Pila(Coleccion):
    """Pila (Stack) - Estructura LIFO."""

    def __init__(self):
        self.elementos = []

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def sacar(self):
        if self.esta_vacia():
            return None
        return self.elementos.pop()

    def primero(self):
        if self.esta_vacia():
            return None
        return self.elementos[-1]

    def esta_vacia(self):
        return len(self.elementos) == 0

    def __iter__(self):
        # Recorrer del tope (último) hacia la base (primero)
        for i in range(len(self.elementos) - 1, -1, -1):
            yield self.elementos[i]


# Ejercicio complejo: Cola

class Cola(Coleccion):
    """Cola (Queue) - Estructura FIFO."""

    def __init__(self):
        self.elementos = []

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def sacar(self):
        if self.esta_vacia():
            return None
        return self.elementos.pop(0)

    def primero(self):
        if self.esta_vacia():
            return None
        return self.elementos[0]

    def esta_vacia(self):
        return len(self.elementos) == 0

    def __iter__(self):
        # Recorrer del frente (primero) hacia el final (último)
        for elemento in self.elementos:
            yield elemento


# Ejemplo de polimorfismo

def demo_polimorfismo():
    """Demuestra cómo el mismo código funciona con Pila y Cola."""

    def procesar(coleccion):
        coleccion.agregar("A")
        coleccion.agregar("B")
        coleccion.agregar("C")

        print("Elementos:", list(coleccion))

        print("Sacando:")
        while not coleccion.esta_vacia():
            print(f"  {coleccion.sacar()}")

    print("=== PILA (LIFO) ===")
    procesar(Pila())

    print("\n=== COLA (FIFO) ===")
    procesar(Cola())


if __name__ == "__main__":
    demo_polimorfismo()
