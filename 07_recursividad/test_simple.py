import pytest
from ejercicio_simple import factorial


def test_factorial_cero():
    assert factorial(0) == 1


def test_factorial_uno():
    assert factorial(1) == 1


def test_factorial_dos():
    assert factorial(2) == 2


def test_factorial_tres():
    assert factorial(3) == 6


def test_factorial_cuatro():
    assert factorial(4) == 24


def test_factorial_cinco():
    assert factorial(5) == 120


def test_factorial_seis():
    assert factorial(6) == 720


def test_factorial_diez():
    assert factorial(10) == 3628800
