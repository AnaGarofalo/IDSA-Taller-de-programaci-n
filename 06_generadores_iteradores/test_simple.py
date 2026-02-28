import pytest
import types
from ejercicio_simple import pares_hasta


def test_es_generador():
    """Verifica que pares_hasta es un generador, no una función normal."""
    resultado = pares_hasta(10)
    assert isinstance(resultado, types.GeneratorType), \
        "pares_hasta debe ser un generador (usar yield)"


def test_pares_hasta_10():
    assert list(pares_hasta(10)) == [0, 2, 4, 6, 8, 10]


def test_pares_hasta_7():
    assert list(pares_hasta(7)) == [0, 2, 4, 6]


def test_pares_hasta_0():
    assert list(pares_hasta(0)) == [0]


def test_pares_hasta_1():
    assert list(pares_hasta(1)) == [0]


def test_pares_hasta_2():
    assert list(pares_hasta(2)) == [0, 2]


def test_pares_hasta_negativo():
    assert list(pares_hasta(-1)) == []


def test_pares_hasta_100():
    resultado = list(pares_hasta(100))
    assert len(resultado) == 51  # 0, 2, 4, ..., 100
    assert resultado[0] == 0
    assert resultado[-1] == 100


def test_se_puede_iterar_con_for():
    resultado = []
    for par in pares_hasta(6):
        resultado.append(par)
    assert resultado == [0, 2, 4, 6]


def test_se_puede_usar_next():
    gen = pares_hasta(10)
    assert next(gen) == 0
    assert next(gen) == 2
    assert next(gen) == 4
