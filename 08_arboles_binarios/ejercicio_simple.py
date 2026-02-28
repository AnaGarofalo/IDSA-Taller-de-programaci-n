"""
EJERCICIO: Árbol binario de búsqueda básico

Completá la clase ArbolBinario implementando los métodos:
1. agregar(valor): Agrega un valor al árbol en la posición correcta
2. contiene(valor): Devuelve True si el valor está en el árbol, False si no

La clase Nodo ya está implementada, no la modifiques.

Recordá la regla del BST:
- Valores menores van a la izquierda
- Valores mayores van a la derecha

Ejemplo:
    arbol = ArbolBinario()

    arbol.contiene(5)    → False  (árbol vacío)

    arbol.agregar(5)
    arbol.agregar(3)
    arbol.agregar(8)

    #     5
    #    / \\
    #   3   8

    arbol.contiene(5)    → True
    arbol.contiene(3)    → True
    arbol.contiene(8)    → True
    arbol.contiene(4)    → False
    arbol.contiene(10)   → False
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
        """
        Agrega un valor al árbol en la posición correcta.

        Args:
            valor: El valor a agregar
        """
        # TODO: Implementar
        pass

    def contiene(self, valor):
        """
        Verifica si un valor está en el árbol.

        Args:
            valor: El valor a buscar

        Returns:
            True si el valor está en el árbol, False si no
        """
        # TODO: Implementar
        pass
