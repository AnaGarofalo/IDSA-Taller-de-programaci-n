"""
EJERCICIO: Generador de números pares

Implementá el generador pares_hasta que genere (yield) todos los números
pares desde 0 hasta n (inclusive si n es par).

IMPORTANTE: Debe ser un generador (usar yield), no una función que retorna lista.

Ejemplo:
    list(pares_hasta(10)) → [0, 2, 4, 6, 8, 10]
    list(pares_hasta(7))  → [0, 2, 4, 6]
    list(pares_hasta(0))  → [0]
    list(pares_hasta(-1)) → []

    # También se puede usar con for:
    for par in pares_hasta(6):
        print(par)
    # Imprime: 0, 2, 4, 6
"""


def pares_hasta(n):
    """
    Generador que produce números pares desde 0 hasta n.

    Args:
        n: Límite superior (inclusive si es par)

    Yields:
        Números pares: 0, 2, 4, ... hasta n
    """
    # TODO: Implementar generador con yield
    pass
