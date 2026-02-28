"""
SOLUCIONES - No mirar hasta haber intentado resolver los ejercicios
"""


# Ejercicio simple: Bubble Sort
def bubble_sort(lista):
    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


# Ejercicio complejo: Ordenar registros
def ordenar_registros(lista_diccionarios, clave):
    lista = lista_diccionarios.copy()
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j][clave] < lista[min_idx][clave]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista
