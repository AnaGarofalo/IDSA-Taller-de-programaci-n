"""
SOLUCIONES - No mirar hasta haber intentado resolver los ejercicios
"""


# Ejercicio simple: Cuadrados de pares
def cuadrados_pares(lista):
    return [x ** 2 for x in lista if x % 2 == 0]


# Ejercicio complejo: Procesar datos
def procesar_datos(productos):
    return [
        {"nombre": p["nombre"], "precio_final": p["precio"] * 0.9}
        for p in productos
        if p["stock"] > 0
    ]
