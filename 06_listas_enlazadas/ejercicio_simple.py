"""
EJERCICIO: Lista enlazada básica

Completá la clase ListaEnlazada implementando los métodos:
1. a_lista(): Devuelve una lista de Python con todos los elementos
2. agregar(valor, posicion=0): Agrega un elemento en la posición indicada

El método agregar usa "sobrecarga pythónica" con parámetros por defecto:
- agregar(5)      → agrega al principio (posición 0)
- agregar(5, 0)   → igual, al principio
- agregar(5, 2)   → agrega en la posición 2
- Si la posición es mayor al tamaño, agrega al final

La clase Nodo ya está implementada, no la modifiques.

Ejemplo:
    lista = ListaEnlazada()

    lista.a_lista()         → []

    lista.agregar(5)        # Agrega al principio (posicion=0)
    lista.a_lista()         → [5]

    lista.agregar(10, 1)    # Agrega en posición 1 (al final)
    lista.a_lista()         → [5, 10]

    lista.agregar(1)        # Agrega al principio
    lista.a_lista()         → [1, 5, 10]

    lista.agregar(7, 2)     # Agrega en posición 2 (entre 5 y 10)
    lista.a_lista()         → [1, 5, 7, 10]
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

    def agregar(self, valor, posicion=0):
        """
        Agrega un elemento en la posición indicada.

        Esta es "sobrecarga pythónica": un solo método que acepta
        diferentes combinaciones de parámetros.

        - agregar(5)      → agrega al principio (posicion=0 por defecto)
        - agregar(5, 2)   → agrega en la posición 2

        Args:
            valor: El valor a agregar
            posicion: Índice donde insertar (default=0, al principio)
        """
        # TODO: Implementar
        # Tip: posicion=0 es O(1), otras posiciones requieren recorrer
        pass
