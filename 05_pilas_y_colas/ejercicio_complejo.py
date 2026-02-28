"""
EJERCICIO: Cola de atención

Implementá la clase ColaDeAtencion que simule un sistema de turnos.

La clase debe tener estos métodos:
- agregar(cliente): Agrega un cliente al final de la cola
- atender(): Atiende (y saca) al primer cliente de la cola, retorna su nombre
- siguiente(): Retorna el nombre del próximo cliente SIN sacarlo de la cola
- cantidad(): Retorna cuántos clientes hay esperando
- esta_vacia(): Retorna True si no hay clientes esperando
- mostrar(): Imprime todos los clientes en la cola

Ejemplo:
    cola = ColaDeAtencion()

    cola.agregar("Ana")
    cola.agregar("Luis")
    cola.agregar("María")

    cola.cantidad()    → 3
    cola.siguiente()   → "Ana"    (no la saca)
    cola.cantidad()    → 3        (sigue siendo 3)

    cola.atender()     → "Ana"    (la saca)
    cola.cantidad()    → 2
    cola.siguiente()   → "Luis"

    cola.atender()     → "Luis"
    cola.atender()     → "María"
    cola.esta_vacia()  → True
    cola.atender()     → None     (no hay nadie)
    cola.siguiente()   → None     (no hay nadie)

    cola.agregar("Ana")
    cola.agregar("Luis")
    cola.mostrar()
    # Imprime:
    # Ana
    # Luis
"""


class ColaDeAtencion:
    """Sistema de cola de atención por turnos."""

    def __init__(self):
        """Inicializa una cola vacía."""
        self.clientes = []

    def agregar(self, cliente):
        """
        Agrega un cliente al final de la cola.

        Args:
            cliente: Nombre del cliente a agregar
        """
        # TODO: Implementar
        pass

    def atender(self):
        """
        Atiende al primer cliente de la cola (lo saca).

        Returns:
            El nombre del cliente atendido, o None si la cola está vacía
        """
        # TODO: Implementar
        pass

    def siguiente(self):
        """
        Muestra quién es el próximo cliente SIN sacarlo de la cola.

        Returns:
            El nombre del próximo cliente, o None si la cola está vacía
        """
        # TODO: Implementar
        pass

    def cantidad(self):
        """
        Retorna la cantidad de clientes esperando.

        Returns:
            Número de clientes en la cola
        """
        # TODO: Implementar
        pass

    def esta_vacia(self):
        """
        Verifica si la cola está vacía.

        Returns:
            True si no hay clientes, False si hay al menos uno
        """
        # TODO: Implementar
        pass

    def mostrar(self):
        """
        Imprime todos los clientes en la cola, del primero al último.

        IMPORTANTE: No lo resuelvas con un for que recorra la lista,
        usá los métodos que implementaste arriba.
        """
        # TODO: Implementar
        pass
