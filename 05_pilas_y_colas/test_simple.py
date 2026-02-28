import pytest
from ejercicio_simple import Pila


def test_pila_nueva_esta_vacia():
    pila = Pila()
    assert pila.esta_vacia() == True


def test_apilar_un_elemento():
    pila = Pila()
    pila.apilar(5)
    assert pila.esta_vacia() == False


def test_apilar_varios_elementos():
    pila = Pila()
    pila.apilar(1)
    pila.apilar(2)
    pila.apilar(3)
    assert pila.tope() == 3


def test_desapilar_devuelve_ultimo():
    pila = Pila()
    pila.apilar(1)
    pila.apilar(2)
    pila.apilar(3)
    assert pila.desapilar() == 3


def test_orden_lifo():
    pila = Pila()
    pila.apilar("primero")
    pila.apilar("segundo")
    pila.apilar("tercero")
    assert pila.desapilar() == "tercero"
    assert pila.desapilar() == "segundo"
    assert pila.desapilar() == "primero"


def test_tope_no_saca_elemento():
    pila = Pila()
    pila.apilar(42)
    assert pila.tope() == 42
    assert pila.tope() == 42
    assert pila.esta_vacia() == False


def test_desapilar_pila_vacia():
    pila = Pila()
    assert pila.desapilar() is None


def test_tope_pila_vacia():
    pila = Pila()
    assert pila.tope() is None


def test_flujo_completo():
    pila = Pila()

    pila.apilar(1)
    pila.apilar(2)
    assert pila.tope() == 2

    assert pila.desapilar() == 2
    assert pila.tope() == 1

    pila.apilar(3)
    assert pila.tope() == 3

    assert pila.desapilar() == 3
    assert pila.desapilar() == 1
    assert pila.esta_vacia() == True


def test_apilar_despues_de_vaciar():
    pila = Pila()
    pila.apilar(1)
    pila.desapilar()
    assert pila.esta_vacia() == True

    pila.apilar(2)
    assert pila.esta_vacia() == False
    assert pila.tope() == 2


def test_mostrar(capsys):
    pila = Pila()
    pila.apilar(1)
    pila.apilar(2)
    pila.apilar(3)
    pila.mostrar()
    captured = capsys.readouterr()
    # Debe mostrar del tope hacia abajo
    assert "3" in captured.out
    assert "2" in captured.out
    assert "1" in captured.out


def test_mostrar_pila_vacia(capsys):
    pila = Pila()
    pila.mostrar()  # No debe dar error
