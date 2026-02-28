import pytest
from abc import ABC
from ejercicio_simple import Coleccion, Pila


# Tests para la clase base Coleccion

def test_coleccion_es_abstracta():
    """No se puede instanciar Coleccion directamente."""
    with pytest.raises(TypeError):
        Coleccion()


def test_coleccion_hereda_de_abc():
    """Coleccion debe heredar de ABC."""
    assert issubclass(Coleccion, ABC)


# Tests para Pila

def test_pila_hereda_de_coleccion():
    assert issubclass(Pila, Coleccion)


def test_pila_nueva_esta_vacia():
    pila = Pila()
    assert pila.esta_vacia() == True


def test_pila_agregar_un_elemento():
    pila = Pila()
    pila.agregar(1)
    assert pila.esta_vacia() == False
    assert pila.primero() == 1


def test_pila_agregar_varios_elementos():
    pila = Pila()
    pila.agregar(1)
    pila.agregar(2)
    pila.agregar(3)
    assert pila.primero() == 3  # LIFO: el último agregado


def test_pila_sacar_devuelve_ultimo():
    pila = Pila()
    pila.agregar(1)
    pila.agregar(2)
    pila.agregar(3)
    assert pila.sacar() == 3  # LIFO
    assert pila.sacar() == 2
    assert pila.sacar() == 1


def test_pila_sacar_vacia_devuelve_none():
    pila = Pila()
    assert pila.sacar() == None


def test_pila_primero_no_saca():
    pila = Pila()
    pila.agregar(1)
    pila.agregar(2)
    assert pila.primero() == 2
    assert pila.primero() == 2  # Sigue siendo 2
    assert pila.esta_vacia() == False


def test_pila_primero_vacia_devuelve_none():
    pila = Pila()
    assert pila.primero() == None


def test_pila_iterar():
    pila = Pila()
    pila.agregar(1)
    pila.agregar(2)
    pila.agregar(3)

    elementos = list(pila)
    assert elementos == [3, 2, 1]  # Del tope hacia la base


def test_pila_iterar_vacia():
    pila = Pila()
    elementos = list(pila)
    assert elementos == []


def test_pila_iterar_no_modifica():
    pila = Pila()
    pila.agregar(1)
    pila.agregar(2)

    list(pila)  # Iterar
    assert pila.primero() == 2  # No se modificó
    assert pila.esta_vacia() == False


def test_pila_con_strings():
    pila = Pila()
    pila.agregar("a")
    pila.agregar("b")
    assert pila.sacar() == "b"
    assert pila.sacar() == "a"


def test_pila_con_none():
    pila = Pila()
    pila.agregar(None)
    assert pila.esta_vacia() == False
    assert pila.primero() == None
    assert pila.sacar() == None
    assert pila.esta_vacia() == True
