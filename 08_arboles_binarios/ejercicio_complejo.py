"""
EJERCICIO: Recorrido inorden

Extendé la clase ArbolBinario del ejercicio simple agregando el método
recorrido_inorden() que devuelve una lista con todos los valores en orden
ascendente.

IMPORTANTE: Usamos herencia para no repetir código. La clase
ArbolBinarioConRecorrido hereda de ArbolBinario (ejercicio simple),
así que ya tiene los métodos agregar() y contiene().

El recorrido inorden visita: izquierda → raíz → derecha

Ejemplo:
    arbol = ArbolBinarioConRecorrido()
    arbol.agregar(5)
    arbol.agregar(3)
    arbol.agregar(8)
    arbol.agregar(1)
    arbol.agregar(4)

    #       5
    #      / \\
    #     3   8
    #    / \\
    #   1   4

    arbol.recorrido_inorden()  → [1, 3, 4, 5, 8]

Otro ejemplo:
    arbol_vacio = ArbolBinarioConRecorrido()
    arbol_vacio.recorrido_inorden()  → []

Pista: Usá recursividad. El patrón es:
    1. Recorrer subárbol izquierdo
    2. Visitar la raíz
    3. Recorrer subárbol derecho
"""

from ejercicio_simple import ArbolBinario


class ArbolBinarioConRecorrido(ArbolBinario):
    """
    Árbol binario con recorrido inorden.
    Hereda agregar() y contiene() de ArbolBinario.
    """

    def recorrido_inorden(self):
        """
        Devuelve una lista con los valores en orden ascendente.

        Returns:
            Lista con todos los valores ordenados de menor a mayor
        """
        # TODO: Implementar
        pass
