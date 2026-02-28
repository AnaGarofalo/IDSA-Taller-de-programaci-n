"""
SOLUCIONES - No mirar hasta haber intentado resolver los ejercicios

Hay dos formas de resolver estos ejercicios:
- Versión RECURSIVA: Usa funciones auxiliares que se llaman a sí mismas
- Versión ITERATIVA: Usa un loop while para recorrer el árbol

Ambas son válidas. La recursiva es más elegante, la iterativa más explícita.
"""


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


# =============================================================================
# EJERCICIO SIMPLE - VERSIÓN RECURSIVA
# =============================================================================

class ArbolBinarioSimpleRecursivo:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._agregar_recursivo(self.raiz, valor)

    def _agregar_recursivo(self, nodo, valor):
        # Usamos una función auxiliar porque necesitamos pasar el nodo actual
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
        return self._contiene_recursivo(self.raiz, valor)

    def _contiene_recursivo(self, nodo, valor):
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        if valor < nodo.valor:
            return self._contiene_recursivo(nodo.izquierdo, valor)
        return self._contiene_recursivo(nodo.derecho, valor)


# =============================================================================
# EJERCICIO SIMPLE - VERSIÓN ITERATIVA (con while)
# =============================================================================

class ArbolBinarioSimpleIterativo:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
        nuevo = Nodo(valor)

        if self.raiz is None:
            self.raiz = nuevo
            return

        actual = self.raiz
        while True:
            if valor < actual.valor:
                if actual.izquierdo is None:
                    actual.izquierdo = nuevo
                    return
                actual = actual.izquierdo
            else:
                if actual.derecho is None:
                    actual.derecho = nuevo
                    return
                actual = actual.derecho

    def contiene(self, valor):
        actual = self.raiz

        while actual is not None:
            if valor == actual.valor:
                return True
            if valor < actual.valor:
                actual = actual.izquierdo
            else:
                actual = actual.derecho

        return False


# =============================================================================
# EJERCICIO COMPLEJO - VERSIÓN RECURSIVA
# =============================================================================

class ArbolBinarioComplejoRecursivo:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
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
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado

    def _inorden_recursivo(self, nodo, resultado):
        if nodo is None:
            return
        self._inorden_recursivo(nodo.izquierdo, resultado)
        resultado.append(nodo.valor)
        self._inorden_recursivo(nodo.derecho, resultado)


# =============================================================================
# EJERCICIO COMPLEJO - VERSIÓN ITERATIVA (con while y pila)
# =============================================================================

class ArbolBinarioComplejoIterativo:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
        nuevo = Nodo(valor)

        if self.raiz is None:
            self.raiz = nuevo
            return

        actual = self.raiz
        while True:
            if valor < actual.valor:
                if actual.izquierdo is None:
                    actual.izquierdo = nuevo
                    return
                actual = actual.izquierdo
            else:
                if actual.derecho is None:
                    actual.derecho = nuevo
                    return
                actual = actual.derecho

    def contiene(self, valor):
        actual = self.raiz

        while actual is not None:
            if valor == actual.valor:
                return True
            if valor < actual.valor:
                actual = actual.izquierdo
            else:
                actual = actual.derecho

        return False

    def recorrido_inorden(self):
        # Para hacer inorden iterativo, necesitamos una pila
        resultado = []
        pila = []
        actual = self.raiz

        while actual is not None or len(pila) > 0:
            # Ir lo más a la izquierda posible
            while actual is not None:
                pila.append(actual)
                actual = actual.izquierdo

            # Procesar el nodo
            actual = pila.pop()
            resultado.append(actual.valor)

            # Ir a la derecha
            actual = actual.derecho

        return resultado
