from ejercicio_simple import ArbolBinario, Nodo


def test_arbol_vacio_no_contiene():
    arbol = ArbolBinario()
    assert arbol.contiene(5) == False


def test_agregar_raiz():
    arbol = ArbolBinario()
    arbol.agregar(5)
    assert arbol.raiz is not None
    assert arbol.raiz.valor == 5


def test_contiene_raiz():
    arbol = ArbolBinario()
    arbol.agregar(5)
    assert arbol.contiene(5) == True


def test_agregar_izquierda():
    arbol = ArbolBinario()
    arbol.agregar(5)
    arbol.agregar(3)
    assert arbol.raiz.izquierdo is not None
    assert arbol.raiz.izquierdo.valor == 3


def test_agregar_derecha():
    arbol = ArbolBinario()
    arbol.agregar(5)
    arbol.agregar(8)
    assert arbol.raiz.derecho is not None
    assert arbol.raiz.derecho.valor == 8


def test_contiene_varios():
    arbol = ArbolBinario()
    arbol.agregar(5)
    arbol.agregar(3)
    arbol.agregar(8)
    assert arbol.contiene(5) == True
    assert arbol.contiene(3) == True
    assert arbol.contiene(8) == True


def test_no_contiene():
    arbol = ArbolBinario()
    arbol.agregar(5)
    arbol.agregar(3)
    arbol.agregar(8)
    assert arbol.contiene(4) == False
    assert arbol.contiene(10) == False
    assert arbol.contiene(1) == False


def test_estructura_completa():
    arbol = ArbolBinario()
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

    assert arbol.raiz.valor == 5
    assert arbol.raiz.izquierdo.valor == 3
    assert arbol.raiz.derecho.valor == 8
    assert arbol.raiz.izquierdo.izquierdo.valor == 1
    assert arbol.raiz.izquierdo.derecho.valor == 4
    assert arbol.raiz.derecho.derecho.valor == 9


def test_contiene_profundo():
    arbol = ArbolBinario()
    arbol.agregar(5)
    arbol.agregar(3)
    arbol.agregar(8)
    arbol.agregar(1)
    arbol.agregar(4)
    arbol.agregar(9)

    assert arbol.contiene(1) == True
    assert arbol.contiene(4) == True
    assert arbol.contiene(9) == True


def test_agregar_duplicados():
    arbol = ArbolBinario()
    arbol.agregar(5)
    arbol.agregar(5)
    # Los duplicados van a la derecha
    assert arbol.raiz.derecho is not None
    assert arbol.raiz.derecho.valor == 5


def test_solo_izquierda():
    arbol = ArbolBinario()
    arbol.agregar(5)
    arbol.agregar(4)
    arbol.agregar(3)
    arbol.agregar(2)

    assert arbol.contiene(5) == True
    assert arbol.contiene(4) == True
    assert arbol.contiene(3) == True
    assert arbol.contiene(2) == True
    assert arbol.contiene(6) == False


def test_solo_derecha():
    arbol = ArbolBinario()
    arbol.agregar(1)
    arbol.agregar(2)
    arbol.agregar(3)
    arbol.agregar(4)

    assert arbol.contiene(1) == True
    assert arbol.contiene(2) == True
    assert arbol.contiene(3) == True
    assert arbol.contiene(4) == True
    assert arbol.contiene(0) == False
