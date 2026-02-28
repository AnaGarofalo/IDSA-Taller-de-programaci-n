"""
SOLUCIONES - No mirar hasta haber intentado resolver los ejercicios
"""


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


# Ejercicio simple: Lista enlazada con sobrecarga pythónica
class ListaEnlazadaSimple:
    def __init__(self):
        self.cabeza = None

    def a_lista(self):
        resultado = []
        actual = self.cabeza
        while actual is not None:
            resultado.append(actual.valor)
            actual = actual.siguiente
        return resultado

    def agregar(self, valor, posicion=0):
        """
        Agrega en la posición indicada.
        Por defecto agrega al principio (posicion=0).

        Esto es "sobrecarga pythónica":
        - agregar(5)      → al principio
        - agregar(5, 2)   → en posición 2
        """
        nuevo = Nodo(valor)

        # Insertar al principio (o lista vacía)
        if posicion == 0 or self.cabeza is None:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
            return

        # Buscar la posición anterior donde insertar
        actual = self.cabeza
        for _ in range(posicion - 1):
            if actual.siguiente is None:
                break
            actual = actual.siguiente

        # Insertar después de 'actual'
        nuevo.siguiente = actual.siguiente
        actual.siguiente = nuevo


# Ejercicio complejo: Lista enlazada con invertir
class ListaEnlazadaCompleja:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor, posicion=0):
        nuevo = Nodo(valor)

        if posicion == 0 or self.cabeza is None:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
            return

        actual = self.cabeza
        for _ in range(posicion - 1):
            if actual.siguiente is None:
                break
            actual = actual.siguiente

        nuevo.siguiente = actual.siguiente
        actual.siguiente = nuevo

    def a_lista(self):
        resultado = []
        actual = self.cabeza
        while actual is not None:
            resultado.append(actual.valor)
            actual = actual.siguiente
        return resultado

    def invertir(self):
        anterior = None
        actual = self.cabeza

        while actual is not None:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente

        self.cabeza = anterior
