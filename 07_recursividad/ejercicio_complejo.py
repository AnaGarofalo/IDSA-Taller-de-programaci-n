"""
EJERCICIO: Aplanar lista anidada

Implementá la función aplanar que convierta una lista con sublistas anidadas
en una lista plana (sin sublistas).

Las sublistas pueden estar anidadas a cualquier profundidad.

Ejemplo:
    aplanar([1, 2, 3])                → [1, 2, 3]        (ya está plana)
    aplanar([1, [2, 3], 4])           → [1, 2, 3, 4]
    aplanar([1, [2, [3, 4]], 5])      → [1, 2, 3, 4, 5]
    aplanar([[1, 2], [3, [4, 5]]])    → [1, 2, 3, 4, 5]
    aplanar([])                        → []
    aplanar([[[]]])                    → []              (listas vacías anidadas)
"""


def aplanar(lista_anidada):
    """
    Aplana una lista con sublistas anidadas.

    Args:
        lista_anidada: Lista que puede contener otras listas

    Returns:
        Una lista plana con todos los elementos
    """
    # TODO: Implementar aplanar recursivo
    pass
