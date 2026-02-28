import pytest
import types
from ejercicio_complejo import en_chunks


def test_es_generador():
    """Verifica que en_chunks es un generador."""
    resultado = en_chunks([1, 2, 3], 2)
    assert isinstance(resultado, types.GeneratorType), \
        "en_chunks debe ser un generador (usar yield)"


def test_chunks_exactos():
    datos = [1, 2, 3, 4, 5, 6]
    assert list(en_chunks(datos, 2)) == [[1, 2], [3, 4], [5, 6]]


def test_chunks_con_resto():
    datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert list(en_chunks(datos, 3)) == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]


def test_chunk_mayor_que_lista():
    datos = [1, 2, 3]
    assert list(en_chunks(datos, 10)) == [[1, 2, 3]]


def test_chunk_igual_a_lista():
    datos = [1, 2, 3, 4, 5]
    assert list(en_chunks(datos, 5)) == [[1, 2, 3, 4, 5]]


def test_lista_vacia():
    assert list(en_chunks([], 3)) == []


def test_chunk_de_1():
    datos = [1, 2, 3]
    assert list(en_chunks(datos, 1)) == [[1], [2], [3]]


def test_strings():
    datos = ["a", "b", "c", "d", "e"]
    assert list(en_chunks(datos, 2)) == [["a", "b"], ["c", "d"], ["e"]]


def test_se_puede_iterar():
    datos = [1, 2, 3, 4, 5, 6]
    resultado = []
    for chunk in en_chunks(datos, 2):
        resultado.append(sum(chunk))
    assert resultado == [3, 7, 11]  # 1+2, 3+4, 5+6


def test_no_modifica_original():
    datos = [1, 2, 3, 4, 5]
    list(en_chunks(datos, 2))
    assert datos == [1, 2, 3, 4, 5]


def test_chunks_grandes():
    datos = list(range(100))
    chunks = list(en_chunks(datos, 30))
    assert len(chunks) == 4  # 30 + 30 + 30 + 10
    assert len(chunks[0]) == 30
    assert len(chunks[-1]) == 10
