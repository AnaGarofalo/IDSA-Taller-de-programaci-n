import pytest
from ejercicio_complejo import ListaEnlazada


def test_invertir_varios_elementos():
    lista = ListaEnlazada()
    lista.agregar(1)
    lista.agregar(2)
    lista.agregar(3)

    lista.invertir()
    assert lista.a_lista() == [3, 2, 1]


def test_invertir_dos_elementos():
    lista = ListaEnlazada()
    lista.agregar("a")
    lista.agregar("b")

    lista.invertir()
    assert lista.a_lista() == ["b", "a"]


def test_invertir_un_elemento():
    lista = ListaEnlazada()
    lista.agregar(42)

    lista.invertir()
    assert lista.a_lista() == [42]


def test_invertir_lista_vacia():
    lista = ListaEnlazada()
    lista.invertir()  # No debe dar error
    assert lista.a_lista() == []


def test_invertir_cinco_elementos():
    lista = ListaEnlazada()
    for i in range(1, 6):
        lista.agregar(i)

    lista.invertir()
    assert lista.a_lista() == [5, 4, 3, 2, 1]


def test_invertir_dos_veces():
    lista = ListaEnlazada()
    lista.agregar(1)
    lista.agregar(2)
    lista.agregar(3)

    lista.invertir()
    lista.invertir()
    assert lista.a_lista() == [1, 2, 3]  # Vuelve al original


def test_invertir_strings():
    lista = ListaEnlazada()
    lista.agregar("primero")
    lista.agregar("segundo")
    lista.agregar("tercero")

    lista.invertir()
    assert lista.a_lista() == ["tercero", "segundo", "primero"]


def test_agregar_despues_de_invertir():
    lista = ListaEnlazada()
    lista.agregar(1)
    lista.agregar(2)

    lista.invertir()  # [2, 1]

    lista.agregar(3)  # Se agrega al final
    assert lista.a_lista() == [2, 1, 3]


def test_estructura_correcta_despues_de_invertir():
    lista = ListaEnlazada()
    lista.agregar(10)
    lista.agregar(20)
    lista.agregar(30)

    lista.invertir()

    # Verificar que la estructura interna es correcta
    assert lista.cabeza.valor == 30
    assert lista.cabeza.siguiente.valor == 20
    assert lista.cabeza.siguiente.siguiente.valor == 10
    assert lista.cabeza.siguiente.siguiente.siguiente is None
