import pytest
from ejercicio_complejo import busqueda_binaria


def test_elemento_en_medio():
    assert busqueda_binaria([1, 3, 5, 7, 9], 5) == 2


def test_elemento_al_inicio():
    assert busqueda_binaria([1, 3, 5, 7, 9], 1) == 0


def test_elemento_al_final():
    assert busqueda_binaria([1, 3, 5, 7, 9], 9) == 4


def test_elemento_no_existe():
    assert busqueda_binaria([1, 3, 5, 7, 9], 4) == -1


def test_elemento_menor_que_todos():
    assert busqueda_binaria([1, 3, 5, 7, 9], 0) == -1


def test_elemento_mayor_que_todos():
    assert busqueda_binaria([1, 3, 5, 7, 9], 100) == -1


def test_lista_vacia():
    assert busqueda_binaria([], 5) == -1


def test_lista_un_elemento_encontrado():
    assert busqueda_binaria([42], 42) == 0


def test_lista_un_elemento_no_encontrado():
    assert busqueda_binaria([42], 10) == -1


def test_lista_dos_elementos():
    assert busqueda_binaria([1, 5], 1) == 0
    assert busqueda_binaria([1, 5], 5) == 1
    assert busqueda_binaria([1, 5], 3) == -1


def test_lista_grande():
    lista = list(range(0, 1000, 2))  # [0, 2, 4, 6, ..., 998]
    assert busqueda_binaria(lista, 500) == 250
    assert busqueda_binaria(lista, 501) == -1  # número impar no está


def test_numeros_negativos():
    assert busqueda_binaria([-10, -5, 0, 5, 10], -5) == 1
    assert busqueda_binaria([-10, -5, 0, 5, 10], 0) == 2
