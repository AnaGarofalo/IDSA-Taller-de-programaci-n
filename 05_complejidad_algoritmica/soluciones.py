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


# Ejercicio complejo: Buscar duplicados rápido
def buscar_duplicados_rapido(lista):
    vistos = set()
    duplicados = set()

    for elemento in lista:
        if elemento in vistos:
            duplicados.add(elemento)
        else:
            vistos.add(elemento)

    return list(duplicados)
