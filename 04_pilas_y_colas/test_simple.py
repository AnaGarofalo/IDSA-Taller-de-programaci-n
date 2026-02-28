import pytest
from ejercicio_simple import parentesis_balanceados


def test_parentesis_simples():
    assert parentesis_balanceados("()") == True


def test_corchetes_simples():
    assert parentesis_balanceados("[]") == True


def test_llaves_simples():
    assert parentesis_balanceados("{}") == True


def test_anidados():
    assert parentesis_balanceados("([{}])") == True


def test_multiples_grupos():
    assert parentesis_balanceados("()[]{}") == True


def test_combinacion_valida():
    assert parentesis_balanceados("([])") == True


def test_no_cerrado():
    assert parentesis_balanceados("(") == False


def test_no_abierto():
    assert parentesis_balanceados(")") == False


def test_orden_incorrecto():
    assert parentesis_balanceados("([)]") == False


def test_cierre_sin_apertura():
    assert parentesis_balanceados("())") == False


def test_apertura_sin_cierre():
    assert parentesis_balanceados("(()") == False


def test_string_vacio():
    assert parentesis_balanceados("") == True


def test_sin_parentesis():
    assert parentesis_balanceados("hola mundo") == True


def test_expresion_matematica():
    assert parentesis_balanceados("(a + b) * [c - d]") == True


def test_expresion_con_llaves():
    assert parentesis_balanceados("{x: (a + b)}") == True


def test_solo_texto_y_parentesis():
    assert parentesis_balanceados("funcion(arg)") == True


def test_mal_balanceado_complejo():
    assert parentesis_balanceados("{[}]") == False
