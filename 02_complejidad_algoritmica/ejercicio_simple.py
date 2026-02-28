"""
EJERCICIO: Identificar complejidad

Mirá las funciones definidas abajo y completá identificar_complejidad()
para que devuelva la complejidad de cada una.

Las opciones son: "O(1)", "O(n)", "O(n^2)", "O(log n)"

Ejemplo:
    identificar_complejidad(1) → "O(n)"   (porque funcion_1 tiene un loop)
    identificar_complejidad(2) → "O(1)"   (porque funcion_2 es constante)
    etc.
"""


# ----- FUNCIONES A ANALIZAR (no las modifiques) -----

def funcion_1(lista):
    """Suma todos los elementos."""
    total = 0
    for x in lista:
        total += x
    return total


def funcion_2(lista):
    """Devuelve el primer elemento."""
    if len(lista) > 0:
        return lista[0]
    return None


def funcion_3(lista):
    """Compara cada elemento con todos los demás."""
    contador = 0
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] == lista[j]:
                contador += 1
    return contador


def funcion_4(n):
    """Divide n a la mitad repetidamente."""
    pasos = 0
    while n > 1:
        n = n // 2
        pasos += 1
    return pasos


def funcion_5(lista):
    """Hace tres operaciones simples."""
    a = lista[0] if lista else 0
    b = lista[-1] if lista else 0
    return a + b


def funcion_6(lista):
    """Recorre la lista dos veces (secuencialmente)."""
    maximo = lista[0] if lista else 0
    for x in lista:
        if x > maximo:
            maximo = x

    minimo = lista[0] if lista else 0
    for x in lista:
        if x < minimo:
            minimo = x

    return maximo - minimo


# ----- TU FUNCIÓN (completá esta) -----

def identificar_complejidad(numero_funcion):
    """
    Devuelve la complejidad Big O de la función indicada.

    Args:
        numero_funcion: Número del 1 al 6 indicando qué función analizar

    Returns:
        String con la complejidad: "O(1)", "O(n)", "O(n^2)", o "O(log n)"
    """
    # TODO: Analizar cada función y devolver su complejidad
    # Ejemplo: if numero_funcion == 1: return "O(n)"
    pass
