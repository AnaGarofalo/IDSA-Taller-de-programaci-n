"""
EJERCICIO: Cola usando la misma interfaz

Implementá la clase Cola que hereda de Coleccion (importada del ejercicio simple).
Debe implementar la misma interfaz que Pila, pero con comportamiento FIFO.

Métodos a implementar:
- agregar(elemento): Agrega un elemento al final de la cola
- sacar(): Saca y devuelve el elemento del frente (o None si está vacía)
- primero(): Devuelve el elemento del frente SIN sacarlo (o None si está vacía)
- esta_vacia(): Devuelve True si la cola está vacía
- __iter__(): Permite recorrer la cola del frente hacia el final

Recordá: La cola es FIFO (First In, First Out)

Ejemplo:
    cola = Cola()

    cola.agregar(1)
    cola.agregar(2)
    cola.agregar(3)

    cola.primero()    → 1       (no lo saca)
    cola.sacar()      → 1       (lo saca)
    cola.sacar()      → 2
    cola.primero()    → 3
    cola.esta_vacia() → False
    cola.sacar()      → 3
    cola.esta_vacia() → True
    cola.sacar()      → None    (cola vacía)

    cola.agregar(1)
    cola.agregar(2)
    for elemento in cola:
        print(elemento)
    # Imprime:
    # 1
    # 2

POLIMORFISMO:
Una vez implementada, podés usar Pila y Cola de forma intercambiable:

    def vaciar(coleccion):
        while not coleccion.esta_vacia():
            print(coleccion.sacar())

    vaciar(Pila())  # Funciona
    vaciar(Cola())  # También funciona!
"""

from ejercicio_simple import Coleccion


class Cola(Coleccion):
    """
    Cola (Queue) - Estructura FIFO (First In, First Out).
    El primer elemento en entrar es el primero en salir.
    """

    def __init__(self):
        """Inicializa una cola vacía."""
        self.elementos = []

    def agregar(self, elemento):
        """
        Agrega un elemento al final de la cola.

        Args:
            elemento: El elemento a agregar
        """
        # TODO: Implementar
        pass

    def sacar(self):
        """
        Saca y devuelve el elemento del frente de la cola.

        Returns:
            El elemento del frente, o None si la cola está vacía
        """
        # TODO: Implementar
        pass

    def primero(self):
        """
        Devuelve el elemento del frente SIN sacarlo.

        Returns:
            El elemento del frente, o None si la cola está vacía
        """
        # TODO: Implementar
        pass

    def esta_vacia(self):
        """
        Verifica si la cola está vacía.

        Returns:
            True si no hay elementos, False si hay al menos uno
        """
        # TODO: Implementar
        pass

    def __iter__(self):
        """
        Permite recorrer la cola del frente hacia el final.

        Yields:
            Los elementos de la cola en orden FIFO
        """
        # TODO: Implementar (usá yield)
        pass
