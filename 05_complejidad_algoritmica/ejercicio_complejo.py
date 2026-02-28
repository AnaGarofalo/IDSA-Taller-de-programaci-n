"""
EJERCICIO: Optimizar búsqueda de duplicados

La función buscar_duplicados_lento encuentra todos los elementos que aparecen
más de una vez en una lista. Funciona, pero es muy lenta (O(n²)).

Tu tarea: Implementá buscar_duplicados_rapido que haga lo mismo pero en O(n).

Ejemplo:
    buscar_duplicados_rapido([1, 2, 3, 2, 4, 3]) → [2, 3]
    buscar_duplicados_rapido([1, 2, 3])          → []
    buscar_duplicados_rapido([1, 1, 1])          → [1]
    buscar_duplicados_rapido([])                 → []

El orden del resultado no importa, pero cada duplicado debe aparecer una sola vez.
"""


# Esta es la versión lenta - NO LA MODIFIQUES, es solo referencia
def buscar_duplicados_lento(lista):
    """
    Versión O(n²) - muy lenta para listas grandes.
    """
    duplicados = []
    for i in range(len(lista)):
        if lista[i] in duplicados:
            continue
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                duplicados.append(lista[i])
                break
    return duplicados


# Esta es la que tenés que implementar
def buscar_duplicados_rapido(lista):
    """
    Encuentra todos los elementos que aparecen más de una vez.
    Esta versión debe ser O(n).

    Args:
        lista: Lista de elementos (pueden ser números o strings)

    Returns:
        Lista con los elementos duplicados (cada uno aparece una sola vez)
    """
    # TODO: Implementar versión O(n)
    pass
