import pytest
from ejercicio_complejo import ColaDeAtencion


def test_cola_nueva_esta_vacia():
    cola = ColaDeAtencion()
    assert cola.esta_vacia() == True


def test_agregar_un_cliente():
    cola = ColaDeAtencion()
    cola.agregar("Ana")
    assert cola.esta_vacia() == False
    assert cola.cantidad() == 1


def test_agregar_varios_clientes():
    cola = ColaDeAtencion()
    cola.agregar("Ana")
    cola.agregar("Luis")
    cola.agregar("María")
    assert cola.cantidad() == 3


def test_siguiente_sin_sacar():
    cola = ColaDeAtencion()
    cola.agregar("Ana")
    cola.agregar("Luis")
    assert cola.siguiente() == "Ana"
    assert cola.cantidad() == 2  # No cambió


def test_atender_saca_cliente():
    cola = ColaDeAtencion()
    cola.agregar("Ana")
    cola.agregar("Luis")
    cliente = cola.atender()
    assert cliente == "Ana"
    assert cola.cantidad() == 1


def test_orden_fifo():
    cola = ColaDeAtencion()
    cola.agregar("Primero")
    cola.agregar("Segundo")
    cola.agregar("Tercero")
    assert cola.atender() == "Primero"
    assert cola.atender() == "Segundo"
    assert cola.atender() == "Tercero"


def test_atender_cola_vacia():
    cola = ColaDeAtencion()
    assert cola.atender() is None


def test_siguiente_cola_vacia():
    cola = ColaDeAtencion()
    assert cola.siguiente() is None


def test_cantidad_cola_vacia():
    cola = ColaDeAtencion()
    assert cola.cantidad() == 0


def test_flujo_completo():
    cola = ColaDeAtencion()

    # Llegan clientes
    cola.agregar("Ana")
    cola.agregar("Luis")
    assert cola.cantidad() == 2

    # Se atiende a Ana
    assert cola.atender() == "Ana"
    assert cola.cantidad() == 1

    # Llega otro cliente
    cola.agregar("María")
    assert cola.cantidad() == 2

    # Se ve quién sigue
    assert cola.siguiente() == "Luis"

    # Se atienden los demás
    assert cola.atender() == "Luis"
    assert cola.atender() == "María"
    assert cola.esta_vacia() == True


def test_agregar_despues_de_vaciar():
    cola = ColaDeAtencion()
    cola.agregar("Ana")
    cola.atender()
    assert cola.esta_vacia() == True

    cola.agregar("Luis")
    assert cola.esta_vacia() == False
    assert cola.siguiente() == "Luis"
