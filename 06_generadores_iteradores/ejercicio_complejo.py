"""
EJERCICIO: Generador de chunks (bloques)

Implementá el generador en_chunks que divida una lista en sublistas
de tamaño fijo.

Esto es muy útil para procesar datos grandes en bloques, por ejemplo:
- Procesar 1000 registros de a 100
- Enviar datos a una API en lotes
- Cargar datos en memoria de forma controlada

Ejemplo:
    datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    list(en_chunks(datos, 3)) → [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
    list(en_chunks(datos, 5)) → [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
    list(en_chunks(datos, 20)) → [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]

    list(en_chunks([], 3)) → []

    # Uso típico:
    for bloque in en_chunks(datos_grandes, 100):
        procesar(bloque)  # Procesa 100 elementos por vez
"""


def en_chunks(datos, tamanio):
    """
    Generador que divide una lista en bloques de tamaño fijo.

    Args:
        datos: Lista a dividir
        tamanio: Tamaño de cada bloque

    Yields:
        Sublistas de longitud `tamanio` (la última puede ser más corta)
    """
    # TODO: Implementar generador de chunks
    pass
