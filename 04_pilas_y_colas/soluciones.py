"""
SOLUCIONES - No mirar hasta haber intentado resolver los ejercicios
"""


# Ejercicio simple: Paréntesis balanceados
def parentesis_balanceados(expresion):
    pila = []
    pares = {'(': ')', '[': ']', '{': '}'}

    for char in expresion:
        if char in pares:
            pila.append(char)
        elif char in pares.values():
            if not pila:
                return False
            ultimo = pila.pop()
            if pares[ultimo] != char:
                return False

    return len(pila) == 0


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
