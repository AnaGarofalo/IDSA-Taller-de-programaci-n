from ejercicio_simple import ListaEnlazada, Nodo


def test_lista_nueva_vacia():
    lista = ListaEnlazada()
    assert lista.a_lista() == []


# Tests para agregar sin posición (al principio por defecto)

def test_agregar_sin_posicion():
    """agregar(valor) debe agregar al principio (posicion=0)."""
    lista = ListaEnlazada()
    lista.agregar(5)
    assert lista.a_lista() == [5]


def test_agregar_varios_sin_posicion():
    """Varios agregar() sin posición agregan al principio."""
    lista = ListaEnlazada()
    lista.agregar(3)
    lista.agregar(2)
    lista.agregar(1)
    assert lista.a_lista() == [1, 2, 3]


# Tests para agregar con posición 0 (explícito)

def test_agregar_posicion_cero():
    """agregar(valor, 0) es igual que agregar(valor)."""
    lista = ListaEnlazada()
    lista.agregar(5, 0)
    assert lista.a_lista() == [5]


def test_agregar_varios_posicion_cero():
    lista = ListaEnlazada()
    lista.agregar(3, 0)
    lista.agregar(2, 0)
    lista.agregar(1, 0)
    assert lista.a_lista() == [1, 2, 3]


# Tests para agregar al final

def test_agregar_al_final():
    lista = ListaEnlazada()
    lista.agregar(1, 0)
    lista.agregar(2, 1)
    lista.agregar(3, 2)
    assert lista.a_lista() == [1, 2, 3]


def test_agregar_posicion_mayor_a_tamaño():
    """Si la posición es mayor al tamaño, agrega al final."""
    lista = ListaEnlazada()
    lista.agregar(1)
    lista.agregar(2, 100)  # posición 100, pero solo hay 1 elemento
    assert lista.a_lista() == [1, 2]


# Tests para agregar en el medio

def test_agregar_en_medio():
    lista = ListaEnlazada()
    lista.agregar(1, 0)
    lista.agregar(3, 1)
    lista.agregar(2, 1)  # Insertar entre 1 y 3
    assert lista.a_lista() == [1, 2, 3]


def test_agregar_en_varias_posiciones():
    lista = ListaEnlazada()
    lista.agregar(10, 0)   # [10]
    lista.agregar(40, 1)   # [10, 40]
    lista.agregar(20, 1)   # [10, 20, 40]
    lista.agregar(30, 2)   # [10, 20, 30, 40]
    assert lista.a_lista() == [10, 20, 30, 40]


# Tests de sobrecarga (mismo método, diferentes formas de llamar)

def test_sobrecarga_equivalencia():
    """agregar(x) y agregar(x, 0) deben ser equivalentes."""
    lista1 = ListaEnlazada()
    lista2 = ListaEnlazada()

    lista1.agregar(1)
    lista1.agregar(2)

    lista2.agregar(1, 0)
    lista2.agregar(2, 0)

    assert lista1.a_lista() == lista2.a_lista()


# Tests generales

def test_agregar_strings():
    lista = ListaEnlazada()
    lista.agregar("mundo")
    lista.agregar("hola")
    assert lista.a_lista() == ["hola", "mundo"]


def test_a_lista_no_modifica():
    lista = ListaEnlazada()
    lista.agregar(1)
    lista.agregar(2, 1)

    resultado1 = lista.a_lista()
    resultado2 = lista.a_lista()

    assert resultado1 == resultado2 == [1, 2]


def test_estructura_nodos():
    lista = ListaEnlazada()
    lista.agregar(20, 0)
    lista.agregar(10, 0)

    assert lista.cabeza is not None
    assert lista.cabeza.valor == 10
    assert lista.cabeza.siguiente is not None
    assert lista.cabeza.siguiente.valor == 20
    assert lista.cabeza.siguiente.siguiente is None


def test_agregar_none():
    lista = ListaEnlazada()
    lista.agregar(None)
    assert lista.a_lista() == [None]


def test_agregar_cero():
    lista = ListaEnlazada()
    lista.agregar(0)
    assert lista.a_lista() == [0]
