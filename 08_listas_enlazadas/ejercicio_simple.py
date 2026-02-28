"""
EJERCICIO: Lista enlazada básica

Completá la clase ListaEnlazada implementando los métodos:
1. a_lista(): Devuelve una lista de Python con todos los elementos
2. agregar_al_principio(valor): Agrega un elemento al inicio de la lista
3. agregar_al_final(valor): Agrega un elemento al final de la lista

La clase Nodo ya está implementada, no la modifiques.

Ejemplo:
    lista = ListaEnlazada()

    lista.a_lista()              → []

    lista.agregar_al_principio(5)
    lista.a_lista()              → [5]

    lista.agregar_al_final(10)
    lista.a_lista()              → [5, 10]

    lista.agregar_al_principio(1)
    lista.a_lista()              → [1, 5, 10]
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

    def a_lista(self):
        """
        Convierte la lista enlazada a una lista de Python.

        Returns:
            Lista de Python con los valores en orden
        """
        # TODO: Implementar
        pass

    def agregar_al_principio(self, valor):
        """
        Agrega un elemento al principio de la lista.
        Esta operación es O(1).

        Args:
            valor: El valor a agregar
        """
        # TODO: Implementar
        pass

    def agregar_al_final(self, valor):
        """
        Agrega un elemento al final de la lista.
        Esta operación es O(n) porque hay que recorrer toda la lista.

        Args:
            valor: El valor a agregar
        """
        # TODO: Implementar
        pass
