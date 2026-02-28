from ejercicio_simple import ListaEnlazada, Nodo


def test_lista_nueva_vacia():
    lista = ListaEnlazada()
    assert lista.a_lista() == []


# Tests para agregar_al_principio

def test_agregar_al_principio_un_elemento():
    lista = ListaEnlazada()
    lista.agregar_al_principio(5)
    assert lista.a_lista() == [5]


def test_agregar_al_principio_varios():
    lista = ListaEnlazada()
    lista.agregar_al_principio(3)
    lista.agregar_al_principio(2)
    lista.agregar_al_principio(1)
    assert lista.a_lista() == [1, 2, 3]


def test_agregar_al_principio_strings():
    lista = ListaEnlazada()
    lista.agregar_al_principio("mundo")
    lista.agregar_al_principio("hola")
    assert lista.a_lista() == ["hola", "mundo"]


# Tests para agregar_al_final

def test_agregar_al_final_un_elemento():
    lista = ListaEnlazada()
    lista.agregar_al_final(5)
    assert lista.a_lista() == [5]


def test_agregar_al_final_varios():
    lista = ListaEnlazada()
    lista.agregar_al_final(1)
    lista.agregar_al_final(2)
    lista.agregar_al_final(3)
    assert lista.a_lista() == [1, 2, 3]


def test_agregar_al_final_strings():
    lista = ListaEnlazada()
    lista.agregar_al_final("hola")
    lista.agregar_al_final("mundo")
    assert lista.a_lista() == ["hola", "mundo"]


# Tests combinados

def test_combinar_principio_y_final():
    lista = ListaEnlazada()
    lista.agregar_al_final(2)
    lista.agregar_al_principio(1)
    lista.agregar_al_final(3)
    assert lista.a_lista() == [1, 2, 3]


def test_valores_mixtos():
    lista = ListaEnlazada()
    lista.agregar_al_final(1)
    lista.agregar_al_principio("cero")
    lista.agregar_al_final(2.0)
    assert lista.a_lista() == ["cero", 1, 2.0]


def test_a_lista_no_modifica():
    lista = ListaEnlazada()
    lista.agregar_al_final(1)
    lista.agregar_al_final(2)

    resultado1 = lista.a_lista()
    resultado2 = lista.a_lista()

    assert resultado1 == resultado2 == [1, 2]


def test_estructura_nodos_al_final():
    lista = ListaEnlazada()
    lista.agregar_al_final(10)
    lista.agregar_al_final(20)

    assert lista.cabeza is not None
    assert lista.cabeza.valor == 10
    assert lista.cabeza.siguiente is not None
    assert lista.cabeza.siguiente.valor == 20
    assert lista.cabeza.siguiente.siguiente is None


def test_estructura_nodos_al_principio():
    lista = ListaEnlazada()
    lista.agregar_al_principio(20)
    lista.agregar_al_principio(10)

    assert lista.cabeza is not None
    assert lista.cabeza.valor == 10
    assert lista.cabeza.siguiente is not None
    assert lista.cabeza.siguiente.valor == 20
    assert lista.cabeza.siguiente.siguiente is None


def test_agregar_cero():
    lista = ListaEnlazada()
    lista.agregar_al_final(0)
    assert lista.a_lista() == [0]


def test_agregar_none():
    lista = ListaEnlazada()
    lista.agregar_al_principio(None)
    assert lista.a_lista() == [None]
