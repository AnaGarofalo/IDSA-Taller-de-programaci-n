"""
EJERCICIO: Procesar datos

Implementá la función procesar_datos que reciba una lista de productos y:
1. Filtre solo los productos con stock mayor a 0
2. Aplique un descuento del 10% al precio
3. Devuelva solo nombre y precio_final de cada producto

Ejemplo:
    productos = [
        {"nombre": "Laptop", "precio": 1000, "stock": 5},
        {"nombre": "Mouse", "precio": 50, "stock": 0},
        {"nombre": "Teclado", "precio": 80, "stock": 10}
    ]

    procesar_datos(productos) → [
        {"nombre": "Laptop", "precio_final": 900.0},
        {"nombre": "Teclado", "precio_final": 72.0}
    ]

    # El Mouse no aparece porque tiene stock 0

Otro ejemplo:
    procesar_datos([]) → []

    procesar_datos([
        {"nombre": "Monitor", "precio": 300, "stock": 0}
    ]) → []  # No hay productos con stock
"""


def procesar_datos(productos):
    """
    Procesa una lista de productos: filtra por stock y aplica descuento.

    Args:
        productos: Lista de diccionarios con nombre, precio y stock

    Returns:
        Lista de diccionarios con nombre y precio_final (con 10% de descuento)
        Solo incluye productos con stock > 0
    """
    # TODO: Implementar procesamiento de datos
    pass
