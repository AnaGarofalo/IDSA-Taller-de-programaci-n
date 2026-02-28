from ejercicio_complejo import ArbolBinarioConRecorrido
from ejercicio_simple import ArbolBinario


def test_hereda_de_arbol_binario():
    """ArbolBinarioConRecorrido debe heredar de ArbolBinario."""
    assert issubclass(ArbolBinarioConRecorrido, ArbolBinario)


def test_inorden_vacio():
    arbol = ArbolBinarioConRecorrido()
    assert arbol.recorrido_inorden() == []


def test_inorden_un_elemento():
    arbol = ArbolBinarioConRecorrido()
    arbol.agregar(5)
    assert arbol.recorrido_inorden() == [5]


def test_inorden_tres_elementos():
    arbol = ArbolBinarioConRecorrido()
    arbol.agregar(5)
    arbol.agregar(3)
    arbol.agregar(8)

    #     5
    #    / \
    #   3   8

    assert arbol.recorrido_inorden() == [3, 5, 8]


def test_inorden_completo():
    arbol = ArbolBinarioConRecorrido()
    arbol.agregar(5)
    arbol.agregar(3)
    arbol.agregar(8)
    arbol.agregar(1)
    arbol.agregar(4)
    arbol.agregar(9)

    #       5
    #      / \
    #     3   8
    #    / \   \
    #   1   4   9

    assert arbol.recorrido_inorden() == [1, 3, 4, 5, 8, 9]


def test_inorden_solo_izquierda():
    arbol = ArbolBinarioConRecorrido()
    arbol.agregar(5)
    arbol.agregar(4)
    arbol.agregar(3)
    arbol.agregar(2)
    arbol.agregar(1)

    assert arbol.recorrido_inorden() == [1, 2, 3, 4, 5]


def test_inorden_solo_derecha():
    arbol = ArbolBinarioConRecorrido()
    arbol.agregar(1)
    arbol.agregar(2)
    arbol.agregar(3)
    arbol.agregar(4)
    arbol.agregar(5)

    assert arbol.recorrido_inorden() == [1, 2, 3, 4, 5]


def test_inorden_orden_insercion_aleatorio():
    arbol = ArbolBinarioConRecorrido()
    # Insertar en orden aleatorio
    arbol.agregar(7)
    arbol.agregar(2)
    arbol.agregar(9)
    arbol.agregar(1)
    arbol.agregar(5)
    arbol.agregar(8)
    arbol.agregar(10)

    # El inorden siempre devuelve ordenado
    assert arbol.recorrido_inorden() == [1, 2, 5, 7, 8, 9, 10]


def test_inorden_con_duplicados():
    arbol = ArbolBinarioConRecorrido()
    arbol.agregar(5)
    arbol.agregar(3)
    arbol.agregar(5)
    arbol.agregar(3)

    resultado = arbol.recorrido_inorden()
    assert resultado == [3, 3, 5, 5]


def test_inorden_negativos():
    arbol = ArbolBinarioConRecorrido()
    arbol.agregar(0)
    arbol.agregar(-5)
    arbol.agregar(5)
    arbol.agregar(-3)
    arbol.agregar(3)

    assert arbol.recorrido_inorden() == [-5, -3, 0, 3, 5]


def test_inorden_muchos_elementos():
    arbol = ArbolBinarioConRecorrido()
    valores = [50, 25, 75, 10, 30, 60, 90, 5, 15, 27, 35]
    for v in valores:
        arbol.agregar(v)

    resultado = arbol.recorrido_inorden()
    assert resultado == sorted(valores)
