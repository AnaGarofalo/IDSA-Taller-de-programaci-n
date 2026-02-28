"""
SOLUCIONES - No mirar hasta haber intentado resolver los ejercicios
"""


# Ejercicio simple: Identificar complejidad
def identificar_complejidad(numero_funcion):
    complejidades = {
        1: "O(n)",      # Un loop
        2: "O(1)",      # Solo accede al primer elemento
        3: "O(n^2)",    # Dos loops anidados
        4: "O(log n)",  # Divide a la mitad en cada paso
        5: "O(1)",      # Solo operaciones simples
        6: "O(n)",      # Dos loops secuenciales = O(n) + O(n) = O(n)
    }
    return complejidades.get(numero_funcion)


# Ejercicio complejo: Encontrar pares que suman un objetivo
def encontrar_pares_rapido(lista, objetivo):
    vistos = set()
    pares = set()

    for num in lista:
        complemento = objetivo - num
        if complemento in vistos:
            par = (min(complemento, num), max(complemento, num))
            pares.add(par)
        vistos.add(num)

    return list(pares)
