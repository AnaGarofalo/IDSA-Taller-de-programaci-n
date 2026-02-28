"""
SOLUCIONES - No mirar hasta haber intentado resolver los ejercicios
"""


# Ejercicio simple: Factorial
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# Ejercicio complejo: Aplanar lista
def aplanar(lista_anidada):
    resultado = []
    for elemento in lista_anidada:
        if isinstance(elemento, list):
            resultado.extend(aplanar(elemento))
        else:
            resultado.append(elemento)
    return resultado
