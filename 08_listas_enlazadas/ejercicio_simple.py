"""
EJERCICIO: Lista enlazada básica

Completá la clase ListaEnlazada implementando los métodos:
- agregar(valor): Agrega un elemento al final de la lista
- a_lista(): Devuelve una lista de Python con todos los elementos

La clase Nodo ya está implementada, no la modifiques.

Ejemplo:
    lista = ListaEnlazada()

    lista.a_lista()      → []

    lista.agregar(5)
    lista.a_lista()      → [5]

    lista.agregar(10)
    lista.a_lista()      → [5, 10]

    lista.agregar(3)
    lista.a_lista()      → [5, 10, 3]
"""


class Nodo:
    """Un nodo de la lista enlazada."""

    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class ListaEnlazada:
    """Lista enlazada simple."""

    def __init__(self):
        """Inicializa una lista vacía."""
        self.cabeza = None

    def agregar(self, valor):
        """
        Agrega un elemento al final de la lista.

        Args:
            valor: El valor a agregar
        """
        # TODO: Implementar
        pass

    def a_lista(self):
        """
        Convierte la lista enlazada a una lista de Python.

        Returns:
            Lista de Python con los valores en orden
        """
        # TODO: Implementar
        pass
