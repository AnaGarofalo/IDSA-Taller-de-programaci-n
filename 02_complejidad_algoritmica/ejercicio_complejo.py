"""
EJERCICIO: Optimizar búsqueda de pares que suman un objetivo

La función encontrar_pares_lento encuentra todos los pares de números
en una lista que suman un valor objetivo. Funciona, pero es muy lenta (O(n²)).

Tu tarea: Implementá encontrar_pares_rapido que haga lo mismo pero en O(n).

Ejemplo:
    encontrar_pares_rapido([1, 2, 3, 4, 5], 6) → [(1, 5), (2, 4)]
    encontrar_pares_rapido([3, 3], 6)          → [(3, 3)]
    encontrar_pares_rapido([1, 2, 3], 10)      → []
    encontrar_pares_rapido([], 5)              → []

Cada par debe aparecer una sola vez como tupla (menor, mayor).
"""


# Esta es la versión lenta - NO LA MODIFIQUES, es solo referencia
def encontrar_pares_lento(lista, objetivo):
    """
    Versión O(n²) - muy lenta para listas grandes.
    """
    pares = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == objetivo:
                par = (min(lista[i], lista[j]), max(lista[i], lista[j]))
                if par not in pares:
                    pares.append(par)
    return pares


# Esta es la que tenés que implementar
def encontrar_pares_rapido(lista, objetivo):
    """
    Encuentra todos los pares de números que suman el objetivo.
    Esta versión debe ser O(n).

    Args:
        lista: Lista de números
        objetivo: El valor que deben sumar los pares

    Returns:
        Lista de tuplas (a, b) donde a + b = objetivo y a <= b
    """
    # TODO: Implementar versión O(n)
    pass
