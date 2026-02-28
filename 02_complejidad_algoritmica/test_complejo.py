import time
from ejercicio_complejo import encontrar_pares_rapido, encontrar_pares_lento


def test_encuentra_pares_basico():
    resultado = encontrar_pares_rapido([1, 2, 3, 4, 5], 6)
    assert sorted(resultado) == [(1, 5), (2, 4)]


def test_sin_pares():
    assert encontrar_pares_rapido([1, 2, 3], 10) == []


def test_lista_vacia():
    assert encontrar_pares_rapido([], 5) == []


def test_un_elemento():
    assert encontrar_pares_rapido([5], 10) == []


def test_pares_con_mismo_numero():
    resultado = encontrar_pares_rapido([3, 3], 6)
    assert resultado == [(3, 3)]


def test_multiples_pares():
    resultado = encontrar_pares_rapido([1, 5, 3, 7, 4, 2, 6], 8)
    assert sorted(resultado) == [(1, 7), (2, 6), (3, 5)]


def test_numeros_negativos():
    resultado = encontrar_pares_rapido([-2, -1, 0, 1, 2, 3], 1)
    assert sorted(resultado) == [(-2, 3), (-1, 2), (0, 1)]


def test_par_con_cero():
    resultado = encontrar_pares_rapido([0, 5, -5, 10], 5)
    assert sorted(resultado) == [(-5, 10), (0, 5)]


def test_todos_iguales_no_suman():
    assert encontrar_pares_rapido([2, 2, 2], 5) == []


def test_pares_duplicados_solo_una_vez():
    # Aunque hay múltiples 3s, el par (3, 3) solo debe aparecer una vez
    resultado = encontrar_pares_rapido([3, 3, 3, 3], 6)
    assert resultado == [(3, 3)]


def test_mismo_resultado_que_version_lenta():
    lista = [1, 5, 7, 2, 9, 3, 8, 4, 6]
    objetivo = 10
    rapido = sorted(encontrar_pares_rapido(lista, objetivo))
    lento = sorted(encontrar_pares_lento(lista, objetivo))
    assert rapido == lento


def test_es_realmente_mas_rapido():
    """
    Verifica que la versión rápida es significativamente más rápida.
    Con O(n) vs O(n²), la diferencia debe ser notable en listas grandes.
    """
    # Crear lista grande
    lista_grande = list(range(3000))
    objetivo = 2999  # Solo algunos pares válidos

    # Medir versión rápida
    inicio = time.time()
    encontrar_pares_rapido(lista_grande, objetivo)
    tiempo_rapido = time.time() - inicio

    # Medir versión lenta
    inicio = time.time()
    encontrar_pares_lento(lista_grande, objetivo)
    tiempo_lento = time.time() - inicio

    # La versión rápida debería ser al menos 10 veces más rápida
    assert tiempo_rapido < tiempo_lento / 10, \
        f"La versión rápida ({tiempo_rapido:.3f}s) no es suficientemente más rápida que la lenta ({tiempo_lento:.3f}s)"
