import pytest
from ejercicio_simple import identificar_complejidad


def test_funcion_1_lineal():
    # funcion_1 tiene un loop que recorre toda la lista
    assert identificar_complejidad(1) == "O(n)"


def test_funcion_2_constante():
    # funcion_2 solo accede al primer elemento
    assert identificar_complejidad(2) == "O(1)"


def test_funcion_3_cuadratica():
    # funcion_3 tiene dos loops anidados
    assert identificar_complejidad(3) == "O(n^2)"


def test_funcion_4_logaritmica():
    # funcion_4 divide a la mitad en cada iteración
    assert identificar_complejidad(4) == "O(log n)"


def test_funcion_5_constante():
    # funcion_5 solo hace operaciones simples de acceso
    assert identificar_complejidad(5) == "O(1)"


def test_funcion_6_lineal():
    # funcion_6 tiene dos loops secuenciales (no anidados)
    # O(n) + O(n) = O(n)
    assert identificar_complejidad(6) == "O(n)"
