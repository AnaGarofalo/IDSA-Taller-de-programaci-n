"""
SOLUCIONES - No mirar hasta haber intentado resolver los ejercicios
"""


# Ejercicio simple: Pila
class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, elemento):
        self.elementos.append(elemento)

    def desapilar(self):
        if self.esta_vacia():
            return None
        return self.elementos.pop()

    def tope(self):
        if self.esta_vacia():
            return None
        return self.elementos[-1]

    def esta_vacia(self):
        return len(self.elementos) == 0

    def mostrar(self):
        if self.esta_vacia():
            print("(pila vacía)")
            return

        # Sacar todos los elementos guardándolos en una pila auxiliar
        auxiliar = Pila()
        while not self.esta_vacia():
            elemento = self.desapilar()
            print(elemento)
            auxiliar.apilar(elemento)

        # Restaurar la pila original
        while not auxiliar.esta_vacia():
            self.apilar(auxiliar.desapilar())


# Ejercicio complejo: Cola de atención
class ColaDeAtencion:
    def __init__(self):
        self.clientes = []

    def agregar(self, cliente):
        self.clientes.append(cliente)

    def atender(self):
        if self.esta_vacia():
            return None
        return self.clientes.pop(0)

    def siguiente(self):
        if self.esta_vacia():
            return None
        return self.clientes[0]

    def cantidad(self):
        return len(self.clientes)

    def esta_vacia(self):
        return len(self.clientes) == 0

    def mostrar(self):
        if self.esta_vacia():
            print("(cola vacía)")
            return

        # Sacar todos los clientes guardándolos en una cola auxiliar
        auxiliar = ColaDeAtencion()
        while not self.esta_vacia():
            cliente = self.atender()
            print(cliente)
            auxiliar.agregar(cliente)

        # Restaurar la cola original
        while not auxiliar.esta_vacia():
            self.agregar(auxiliar.atender())
