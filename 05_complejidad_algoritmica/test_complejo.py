import pytest
import time
from ejercicio_complejo import buscar_duplicados_rapido, buscar_duplicados_lento


def test_encuentra_duplicados():
    resultado = buscar_duplicados_rapido([1, 2, 3, 2, 4, 3])
    assert sorted(resultado) == [2, 3]


def test_sin_duplicados():
    assert buscar_duplicados_rapido([1, 2, 3]) == []


def test_todos_iguales():
    resultado = buscar_duplicados_rapido([1, 1, 1])
    assert resultado == [1]


def test_lista_vacia():
    assert buscar_duplicados_rapido([]) == []


def test_un_elemento():
    assert buscar_duplicados_rapido([5]) == []


def test_dos_iguales():
    assert buscar_duplicados_rapido([3, 3]) == [3]


def test_dos_diferentes():
    assert buscar_duplicados_rapido([3, 5]) == []


def test_multiples_duplicados():
    resultado = buscar_duplicados_rapido([1, 2, 1, 3, 2, 4, 3, 5])
    assert sorted(resultado) == [1, 2, 3]


def test_duplicados_strings():
    resultado = buscar_duplicados_rapido(["a", "b", "a", "c", "b"])
    assert sorted(resultado) == ["a", "b"]


def test_duplicado_una_vez_en_resultado():
    # Aunque 1 aparece 4 veces, solo debe estar una vez en el resultado
    resultado = buscar_duplicados_rapido([1, 1, 1, 1])
    assert resultado == [1]


def test_mismo_resultado_que_version_lenta():
    lista = [5, 3, 8, 3, 1, 8, 2, 5, 9]
    rapido = sorted(buscar_duplicados_rapido(lista))
    lento = sorted(buscar_duplicados_lento(lista))
    assert rapido == lento


def test_es_realmente_mas_rapido():
    """
    Verifica que la versión rápida es significativamente más rápida.
    Con O(n) vs O(n²), la diferencia debe ser notable en listas grandes.
    """
    # Crear lista grande con algunos duplicados
    lista_grande = list(range(5000)) + list(range(100))  # 5100 elementos, 100 duplicados

    # Medir versión rápida
    inicio = time.time()
    buscar_duplicados_rapido(lista_grande)
    tiempo_rapido = time.time() - inicio

    # Medir versión lenta
    inicio = time.time()
    buscar_duplicados_lento(lista_grande)
    tiempo_lento = time.time() - inicio

    # La versión rápida debería ser al menos 10 veces más rápida
    assert tiempo_rapido < tiempo_lento / 10, \
        f"La versión rápida ({tiempo_rapido:.3f}s) no es suficientemente más rápida que la lenta ({tiempo_lento:.3f}s)"
