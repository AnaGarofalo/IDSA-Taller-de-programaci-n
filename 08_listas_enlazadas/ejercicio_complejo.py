"""
EJERCICIO: Invertir lista enlazada

Completá el método invertir() de la clase ListaEnlazada que invierte
el orden de los elementos.

La inversión debe ser "in-place", es decir, modificar la lista original
en lugar de crear una nueva.

Ejemplo:
    lista = ListaEnlazada()
    lista.agregar(1)
    lista.agregar(2)
    lista.agregar(3)
    lista.a_lista()      → [1, 2, 3]

    lista.invertir()
    lista.a_lista()      → [3, 2, 1]

Otro ejemplo:
    lista = ListaEnlazada()
    lista.agregar("a")
    lista.agregar("b")
    lista.a_lista()      → ["a", "b"]

    lista.invertir()
    lista.a_lista()      → ["b", "a"]

Casos borde:
    - Lista vacía: no hace nada
    - Un elemento: no hace nada (ya está invertida)
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
        """Agrega un elemento al final de la lista."""
        nuevo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def a_lista(self):
        """Convierte la lista enlazada a una lista de Python."""
        resultado = []
        actual = self.cabeza
        while actual is not None:
            resultado.append(actual.valor)
            actual = actual.siguiente
        return resultado

    def invertir(self):
        """
        Invierte la lista enlazada in-place.

        Después de llamar a este método, los elementos están en orden inverso.
        """
        # TODO: Implementar
        pass
