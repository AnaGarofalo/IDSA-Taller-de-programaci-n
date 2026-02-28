from ejercicio_complejo import ListaEnlazadaInvertible
from ejercicio_simple import ListaEnlazada


def test_hereda_de_lista_enlazada():
    """ListaEnlazadaInvertible debe heredar de ListaEnlazada."""
    assert issubclass(ListaEnlazadaInvertible, ListaEnlazada)


def test_invertir_varios_elementos():
    lista = ListaEnlazadaInvertible()
    lista.agregar(3)
    lista.agregar(2)
    lista.agregar(1)
    # Con agregar al principio: [1, 2, 3]

    lista.invertir()
    assert lista.a_lista() == [3, 2, 1]


def test_invertir_dos_elementos():
    lista = ListaEnlazadaInvertible()
    lista.agregar("b")
    lista.agregar("a")
    # ["a", "b"]

    lista.invertir()
    assert lista.a_lista() == ["b", "a"]


def test_invertir_un_elemento():
    lista = ListaEnlazadaInvertible()
    lista.agregar(42)

    lista.invertir()
    assert lista.a_lista() == [42]


def test_invertir_lista_vacia():
    lista = ListaEnlazadaInvertible()
    lista.invertir()  # No debe dar error
    assert lista.a_lista() == []


def test_invertir_cinco_elementos():
    lista = ListaEnlazadaInvertible()
    for i in range(5, 0, -1):  # 5, 4, 3, 2, 1
        lista.agregar(i)
    # Resultado: [1, 2, 3, 4, 5]

    lista.invertir()
    assert lista.a_lista() == [5, 4, 3, 2, 1]


def test_invertir_dos_veces():
    lista = ListaEnlazadaInvertible()
    lista.agregar(3)
    lista.agregar(2)
    lista.agregar(1)
    # [1, 2, 3]

    lista.invertir()
    lista.invertir()
    assert lista.a_lista() == [1, 2, 3]  # Vuelve al original


def test_invertir_strings():
    lista = ListaEnlazadaInvertible()
    lista.agregar("tercero")
    lista.agregar("segundo")
    lista.agregar("primero")
    # ["primero", "segundo", "tercero"]

    lista.invertir()
    assert lista.a_lista() == ["tercero", "segundo", "primero"]


def test_agregar_despues_de_invertir():
    lista = ListaEnlazadaInvertible()
    lista.agregar(2)
    lista.agregar(1)
    # [1, 2]

    lista.invertir()  # [2, 1]

    lista.agregar(3)  # Se agrega al principio → [3, 2, 1]
    assert lista.a_lista() == [3, 2, 1]


def test_estructura_correcta_despues_de_invertir():
    lista = ListaEnlazadaInvertible()
    lista.agregar(30)
    lista.agregar(20)
    lista.agregar(10)
    # [10, 20, 30]

    lista.invertir()

    # Verificar que la estructura interna es correcta
    assert lista.cabeza.valor == 30
    assert lista.cabeza.siguiente.valor == 20
    assert lista.cabeza.siguiente.siguiente.valor == 10
    assert lista.cabeza.siguiente.siguiente.siguiente is None
