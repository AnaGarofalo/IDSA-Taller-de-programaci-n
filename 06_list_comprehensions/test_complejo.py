import pytest
from ejercicio_complejo import procesar_datos


def test_caso_completo():
    productos = [
        {"nombre": "Laptop", "precio": 1000, "stock": 5},
        {"nombre": "Mouse", "precio": 50, "stock": 0},
        {"nombre": "Teclado", "precio": 80, "stock": 10}
    ]
    resultado = procesar_datos(productos)

    assert len(resultado) == 2
    assert resultado[0] == {"nombre": "Laptop", "precio_final": 900.0}
    assert resultado[1] == {"nombre": "Teclado", "precio_final": 72.0}


def test_lista_vacia():
    assert procesar_datos([]) == []


def test_todos_sin_stock():
    productos = [
        {"nombre": "A", "precio": 100, "stock": 0},
        {"nombre": "B", "precio": 200, "stock": 0}
    ]
    assert procesar_datos(productos) == []


def test_todos_con_stock():
    productos = [
        {"nombre": "A", "precio": 100, "stock": 1},
        {"nombre": "B", "precio": 200, "stock": 5}
    ]
    resultado = procesar_datos(productos)
    assert len(resultado) == 2
    assert resultado[0]["precio_final"] == 90.0
    assert resultado[1]["precio_final"] == 180.0


def test_descuento_correcto():
    productos = [{"nombre": "Item", "precio": 1000, "stock": 1}]
    resultado = procesar_datos(productos)
    # 10% de descuento: 1000 * 0.9 = 900
    assert resultado[0]["precio_final"] == 900.0


def test_estructura_resultado():
    productos = [{"nombre": "Test", "precio": 50, "stock": 3}]
    resultado = procesar_datos(productos)

    # Debe tener solo nombre y precio_final
    assert "nombre" in resultado[0]
    assert "precio_final" in resultado[0]
    assert "precio" not in resultado[0]
    assert "stock" not in resultado[0]


def test_conserva_nombre():
    productos = [{"nombre": "Producto ABC", "precio": 100, "stock": 1}]
    resultado = procesar_datos(productos)
    assert resultado[0]["nombre"] == "Producto ABC"


def test_precio_decimal():
    productos = [{"nombre": "Item", "precio": 33, "stock": 1}]
    resultado = procesar_datos(productos)
    # 33 * 0.9 = 29.7
    assert resultado[0]["precio_final"] == pytest.approx(29.7)


def test_stock_exactamente_cero():
    productos = [
        {"nombre": "A", "precio": 100, "stock": 0},
        {"nombre": "B", "precio": 100, "stock": 1}
    ]
    resultado = procesar_datos(productos)
    assert len(resultado) == 1
    assert resultado[0]["nombre"] == "B"


def test_no_modifica_original():
    productos = [{"nombre": "Item", "precio": 100, "stock": 1}]
    procesar_datos(productos)
    # El original no debe cambiar
    assert productos[0]["precio"] == 100
    assert "precio_final" not in productos[0]
