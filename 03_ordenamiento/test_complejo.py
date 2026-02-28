import pytest
from ejercicio_complejo import ordenar_registros


def test_ordenar_por_numero():
    estudiantes = [
        {"nombre": "Ana", "nota": 8},
        {"nombre": "Luis", "nota": 6},
        {"nombre": "María", "nota": 9}
    ]
    resultado = ordenar_registros(estudiantes, "nota")
    assert resultado == [
        {"nombre": "Luis", "nota": 6},
        {"nombre": "Ana", "nota": 8},
        {"nombre": "María", "nota": 9}
    ]


def test_ordenar_por_texto():
    estudiantes = [
        {"nombre": "María", "nota": 9},
        {"nombre": "Ana", "nota": 8},
        {"nombre": "Luis", "nota": 6}
    ]
    resultado = ordenar_registros(estudiantes, "nombre")
    assert resultado == [
        {"nombre": "Ana", "nota": 8},
        {"nombre": "Luis", "nota": 6},
        {"nombre": "María", "nota": 9}
    ]


def test_lista_vacia():
    assert ordenar_registros([], "clave") == []


def test_un_elemento():
    datos = [{"x": 5}]
    assert ordenar_registros(datos, "x") == [{"x": 5}]


def test_ya_ordenada():
    datos = [{"valor": 1}, {"valor": 2}, {"valor": 3}]
    assert ordenar_registros(datos, "valor") == [
        {"valor": 1}, {"valor": 2}, {"valor": 3}
    ]


def test_orden_inverso():
    datos = [{"valor": 3}, {"valor": 2}, {"valor": 1}]
    assert ordenar_registros(datos, "valor") == [
        {"valor": 1}, {"valor": 2}, {"valor": 3}
    ]


def test_productos_por_precio():
    productos = [
        {"nombre": "Laptop", "precio": 1500},
        {"nombre": "Mouse", "precio": 25},
        {"nombre": "Teclado", "precio": 80}
    ]
    resultado = ordenar_registros(productos, "precio")
    assert resultado[0]["nombre"] == "Mouse"
    assert resultado[1]["nombre"] == "Teclado"
    assert resultado[2]["nombre"] == "Laptop"
