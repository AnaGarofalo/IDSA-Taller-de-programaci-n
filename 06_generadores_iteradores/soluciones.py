"""
SOLUCIONES - No mirar hasta haber intentado resolver los ejercicios
"""


# Ejercicio simple: Generador de pares
def pares_hasta(n):
    for i in range(0, n + 1, 2):
        yield i


# Ejercicio complejo: Generador de chunks
def en_chunks(datos, tamanio):
    for i in range(0, len(datos), tamanio):
        yield datos[i:i + tamanio]
