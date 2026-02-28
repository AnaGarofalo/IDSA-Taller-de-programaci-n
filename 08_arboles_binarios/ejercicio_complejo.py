"""
EJERCICIO: Recorrido inorden

Implementá el método recorrido_inorden() que devuelve una lista con todos
los valores del árbol en orden ascendente.

El recorrido inorden visita: izquierda → raíz → derecha

Ejemplo:
    arbol = ArbolBinario()
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
    arbol_vacio = ArbolBinario()
    arbol_vacio.recorrido_inorden()  → []

Pista: Usá recursividad. El patrón es:
    1. Recorrer subárbol izquierdo
    2. Visitar la raíz
    3. Recorrer subárbol derecho
"""


class Nodo:
    """Un nodo del árbol binario."""

    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinario:
    """Árbol binario de búsqueda."""

    def __init__(self):
        """Inicializa un árbol vacío."""
        self.raiz = None

    def agregar(self, valor):
        """Agrega un valor al árbol."""
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._agregar_recursivo(self.raiz, valor)

    def _agregar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
            else:
                self._agregar_recursivo(nodo.izquierdo, valor)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
            else:
                self._agregar_recursivo(nodo.derecho, valor)

    def contiene(self, valor):
        """Verifica si un valor está en el árbol."""
        return self._contiene_recursivo(self.raiz, valor)

    def _contiene_recursivo(self, nodo, valor):
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        if valor < nodo.valor:
            return self._contiene_recursivo(nodo.izquierdo, valor)
        return self._contiene_recursivo(nodo.derecho, valor)

    def recorrido_inorden(self):
        """
        Devuelve una lista con los valores en orden ascendente.

        Returns:
            Lista con todos los valores ordenados de menor a mayor
        """
        # TODO: Implementar
        pass
