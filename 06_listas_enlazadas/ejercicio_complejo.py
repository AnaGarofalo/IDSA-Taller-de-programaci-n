"""
EJERCICIO: Invertir lista enlazada

Extendé la clase ListaEnlazada del ejercicio simple agregando el método
invertir() que invierte el orden de los elementos.

IMPORTANTE: Usamos herencia para no repetir código. La clase
ListaEnlazadaInvertible hereda de ListaEnlazada (ejercicio simple),
así que ya tiene los métodos agregar() y a_lista().

La inversión debe ser "in-place", es decir, modificar la lista original
en lugar de crear una nueva.

Ejemplo:
    lista = ListaEnlazadaInvertible()
    lista.agregar(3, 0)
    lista.agregar(2, 0)
    lista.agregar(1, 0)
    lista.a_lista()      → [1, 2, 3]

    lista.invertir()
    lista.a_lista()      → [3, 2, 1]

Casos borde:
    - Lista vacía: no hace nada
    - Un elemento: no hace nada (ya está invertida)
"""

from ejercicio_simple import ListaEnlazada


class ListaEnlazadaInvertible(ListaEnlazada):
    """
    Lista enlazada que puede invertirse.
    Hereda agregar() y a_lista() de ListaEnlazada.
    """

    def invertir(self):
        """
        Invierte la lista enlazada in-place.

        Después de llamar a este método, los elementos están en orden inverso.
        """
        # TODO: Implementar
        pass
