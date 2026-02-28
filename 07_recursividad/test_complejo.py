import pytest
from ejercicio_complejo import aplanar


def test_lista_ya_plana():
    assert aplanar([1, 2, 3]) == [1, 2, 3]


def test_un_nivel_anidamiento():
    assert aplanar([1, [2, 3], 4]) == [1, 2, 3, 4]


def test_dos_niveles_anidamiento():
    assert aplanar([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]


def test_multiples_sublistas():
    assert aplanar([[1, 2], [3, [4, 5]]]) == [1, 2, 3, 4, 5]


def test_lista_vacia():
    assert aplanar([]) == []


def test_listas_vacias_anidadas():
    assert aplanar([[[]]]) == []


def test_mezcla_vacias_y_valores():
    assert aplanar([1, [], [2, []], 3]) == [1, 2, 3]


def test_profundidad_tres():
    assert aplanar([[[1, 2]], [[3, 4]]]) == [1, 2, 3, 4]


def test_un_solo_elemento_anidado():
    assert aplanar([[[5]]]) == [5]


def test_strings_en_lista():
    assert aplanar(["a", ["b", "c"], "d"]) == ["a", "b", "c", "d"]


def test_tipos_mixtos():
    assert aplanar([1, ["hola", [True, 3.14]]]) == [1, "hola", True, 3.14]
