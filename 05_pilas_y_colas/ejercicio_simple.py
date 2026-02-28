"""
EJERCICIO: Clase base Coleccion y Pila

Parte 1: Implementá la clase base Coleccion con los métodos:
- agregar(elemento): Lanza NotImplementedError
- sacar(): Lanza NotImplementedError
- primero(): Lanza NotImplementedError
- esta_vacia(): Lanza NotImplementedError
- __iter__(): Lanza NotImplementedError

Parte 2: Implementá la clase Pila que hereda de Coleccion:
- agregar(elemento): Agrega un elemento al tope de la pila
- sacar(): Saca y devuelve el elemento del tope (o None si está vacía)
- primero(): Devuelve el elemento del tope SIN sacarlo (o None si está vacía)
- esta_vacia(): Devuelve True si la pila está vacía
- __iter__(): Permite recorrer la pila del tope hacia la base

Recordá: La pila es LIFO (Last In, First Out)

Ejemplo:
    pila = Pila()

    pila.agregar(1)
    pila.agregar(2)
    pila.agregar(3)

    pila.primero()    → 3       (no lo saca)
    pila.sacar()      → 3       (lo saca)
    pila.sacar()      → 2
    pila.primero()    → 1
    pila.esta_vacia() → False
    pila.sacar()      → 1
    pila.esta_vacia() → True
    pila.sacar()      → None    (pila vacía)

    pila.agregar(1)
    pila.agregar(2)
    for elemento in pila:
        print(elemento)
    # Imprime:
    # 2
    # 1
"""

from abc import ABC, abstractmethod


class Coleccion(ABC):
    """
    Clase base abstracta para colecciones de elementos.
    Define la interfaz que deben implementar Pila y Cola.

    ABC = Abstract Base Class
    @abstractmethod = indica que las subclases DEBEN implementar este método
    """

    @abstractmethod
    def agregar(self, elemento):
        """Agrega un elemento a la colección."""
        pass

    @abstractmethod
    def sacar(self):
        """Saca y devuelve un elemento de la colección."""
        pass

    @abstractmethod
    def primero(self):
        """Devuelve el próximo elemento a salir SIN sacarlo."""
        pass

    @abstractmethod
    def esta_vacia(self):
        """Verifica si la colección está vacía."""
        pass

    @abstractmethod
    def __iter__(self):
        """Permite recorrer la colección con un for."""
        pass


class Pila(Coleccion):
    """
    Pila (Stack) - Estructura LIFO (Last In, First Out).
    El último elemento en entrar es el primero en salir.
    """

    def __init__(self):
        """Inicializa una pila vacía."""
        self.elementos = []

    def agregar(self, elemento):
        """
        Agrega un elemento al tope de la pila.

        Args:
            elemento: El elemento a agregar
        """
        # TODO: Implementar
        pass

    def sacar(self):
        """
        Saca y devuelve el elemento del tope de la pila.

        Returns:
            El elemento del tope, o None si la pila está vacía
        """
        # TODO: Implementar
        pass

    def primero(self):
        """
        Devuelve el elemento del tope SIN sacarlo.

        Returns:
            El elemento del tope, o None si la pila está vacía
        """
        # TODO: Implementar
        pass

    def esta_vacia(self):
        """
        Verifica si la pila está vacía.

        Returns:
            True si no hay elementos, False si hay al menos uno
        """
        # TODO: Implementar
        pass

    def __iter__(self):
        """
        Permite recorrer la pila del tope hacia la base.

        Yields:
            Los elementos de la pila en orden LIFO
        """
        # TODO: Implementar (usá yield)
        pass
