import pytest
from ejercicio_simple import busqueda_lineal


def test_elemento_en_medio():
    assert busqueda_lineal([3, 1, 7, 4, 9], 7) == 2


def test_elemento_al_inicio():
    assert busqueda_lineal([3, 1, 7, 4, 9], 3) == 0


def test_elemento_al_final():
    assert busqueda_lineal([3, 1, 7, 4, 9], 9) == 4


def test_elemento_no_existe():
    assert busqueda_lineal([3, 1, 7, 4, 9], 5) == -1


def test_lista_vacia():
    assert busqueda_lineal([], 3) == -1


def test_lista_un_elemento_encontrado():
    assert busqueda_lineal([42], 42) == 0


def test_lista_un_elemento_no_encontrado():
    assert busqueda_lineal([42], 10) == -1


def test_elementos_repetidos_devuelve_primero():
    # Si hay repetidos, devuelve la primera aparición
    assert busqueda_lineal([1, 5, 5, 5, 9], 5) == 1


def test_buscar_strings():
    assert busqueda_lineal(["ana", "luis", "maria"], "luis") == 1


def test_buscar_string_no_existe():
    assert busqueda_lineal(["ana", "luis", "maria"], "pedro") == -1
