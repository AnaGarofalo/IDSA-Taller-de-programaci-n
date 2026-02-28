import pytest
from ejercicio_simple import bubble_sort


def test_lista_desordenada():
    assert bubble_sort([5, 3, 8, 1]) == [1, 3, 5, 8]


def test_lista_ya_ordenada():
    assert bubble_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_lista_orden_inverso():
    assert bubble_sort([4, 3, 2, 1]) == [1, 2, 3, 4]


def test_lista_vacia():
    assert bubble_sort([]) == []


def test_lista_un_elemento():
    assert bubble_sort([42]) == [42]


def test_lista_con_duplicados():
    assert bubble_sort([3, 1, 3, 2, 1]) == [1, 1, 2, 3, 3]


def test_lista_numeros_negativos():
    assert bubble_sort([3, -1, 2, -5]) == [-5, -1, 2, 3]


def test_lista_grande():
    lista = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert bubble_sort(lista) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
