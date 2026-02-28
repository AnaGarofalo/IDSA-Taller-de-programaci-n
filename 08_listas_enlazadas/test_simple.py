import pytest
from ejercicio_simple import ListaEnlazada, Nodo


def test_lista_nueva_vacia():
    lista = ListaEnlazada()
    assert lista.a_lista() == []


def test_agregar_un_elemento():
    lista = ListaEnlazada()
    lista.agregar(5)
    assert lista.a_lista() == [5]


def test_agregar_varios_elementos():
    lista = ListaEnlazada()
    lista.agregar(5)
    lista.agregar(10)
    lista.agregar(3)
    assert lista.a_lista() == [5, 10, 3]


def test_mantiene_orden():
    lista = ListaEnlazada()
    lista.agregar(1)
    lista.agregar(2)
    lista.agregar(3)
    lista.agregar(4)
    assert lista.a_lista() == [1, 2, 3, 4]


def test_agregar_strings():
    lista = ListaEnlazada()
    lista.agregar("hola")
    lista.agregar("mundo")
    assert lista.a_lista() == ["hola", "mundo"]


def test_agregar_valores_mixtos():
    lista = ListaEnlazada()
    lista.agregar(1)
    lista.agregar("dos")
    lista.agregar(3.0)
    assert lista.a_lista() == [1, "dos", 3.0]


def test_a_lista_no_modifica():
    lista = ListaEnlazada()
    lista.agregar(1)
    lista.agregar(2)

    resultado1 = lista.a_lista()
    resultado2 = lista.a_lista()

    assert resultado1 == resultado2 == [1, 2]


def test_estructura_nodos():
    lista = ListaEnlazada()
    lista.agregar(10)
    lista.agregar(20)

    # Verificar que la estructura interna es correcta
    assert lista.cabeza is not None
    assert lista.cabeza.valor == 10
    assert lista.cabeza.siguiente is not None
    assert lista.cabeza.siguiente.valor == 20
    assert lista.cabeza.siguiente.siguiente is None


def test_agregar_cero():
    lista = ListaEnlazada()
    lista.agregar(0)
    assert lista.a_lista() == [0]


def test_agregar_none():
    lista = ListaEnlazada()
    lista.agregar(None)
    assert lista.a_lista() == [None]
