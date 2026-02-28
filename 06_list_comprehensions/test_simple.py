import pytest
from ejercicio_simple import cuadrados_pares


def test_mezcla_pares_impares():
    assert cuadrados_pares([1, 2, 3, 4, 5, 6]) == [4, 16, 36]


def test_solo_impares():
    assert cuadrados_pares([1, 3, 5]) == []


def test_solo_pares():
    assert cuadrados_pares([2, 4, 6]) == [4, 16, 36]


def test_lista_vacia():
    assert cuadrados_pares([]) == []


def test_incluye_cero():
    assert cuadrados_pares([0, 1, 2]) == [0, 4]


def test_numeros_negativos():
    # -2 es par, (-2)² = 4
    assert cuadrados_pares([-2, -1, 0, 1, 2]) == [4, 0, 4]


def test_un_elemento_par():
    assert cuadrados_pares([10]) == [100]


def test_un_elemento_impar():
    assert cuadrados_pares([7]) == []


def test_numeros_grandes():
    assert cuadrados_pares([100, 101, 102]) == [10000, 10404]


def test_muchos_pares():
    resultado = cuadrados_pares([2, 4, 6, 8, 10])
    assert resultado == [4, 16, 36, 64, 100]
