"""
EJERCICIO: Pila

Implementá la clase Pila que simule una pila (stack) con comportamiento LIFO
(Last In, First Out - el último en entrar es el primero en salir).

La clase debe tener estos métodos:
- apilar(elemento): Agrega un elemento arriba de la pila
- desapilar(): Saca y devuelve el elemento de arriba de la pila
- tope(): Devuelve el elemento de arriba SIN sacarlo
- esta_vacia(): Devuelve True si la pila está vacía
- mostrar(): Imprime todos los elementos de la pila

Ejemplo:
    pila = Pila()

    pila.apilar(1)
    pila.apilar(2)
    pila.apilar(3)

    pila.tope()       → 3       (no lo saca)
    pila.desapilar()  → 3       (lo saca)
    pila.desapilar()  → 2
    pila.tope()       → 1
    pila.esta_vacia() → False
    pila.desapilar()  → 1
    pila.esta_vacia() → True
    pila.desapilar()  → None    (pila vacía)
    pila.tope()       → None    (pila vacía)

    pila.apilar(1)
    pila.apilar(2)
    pila.mostrar()
    # Imprime:
    # 2
    # 1
"""


class Pila:
    """Estructura de datos LIFO (Last In, First Out)."""

    def __init__(self):
        """Inicializa una pila vacía."""
        self.elementos = []

    def apilar(self, elemento):
        """
        Agrega un elemento arriba de la pila.

        Args:
            elemento: El elemento a agregar
        """
        # TODO: Implementar
        pass

    def desapilar(self):
        """
        Saca y devuelve el elemento de arriba de la pila.

        Returns:
            El elemento de arriba, o None si la pila está vacía
        """
        # TODO: Implementar
        pass

    def tope(self):
        """
        Devuelve el elemento de arriba SIN sacarlo.

        Returns:
            El elemento de arriba, o None si la pila está vacía
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

    def mostrar(self):
        """
        Imprime todos los elementos de la pila, del tope hacia abajo.

        IMPORTANTE: No lo resuelvas con un for que recorra la lista,
        usá los métodos que implementaste arriba.
        """
        # TODO: Implementar
        pass
