import pytest
from ejercicio_simple import Coleccion, Pila
from ejercicio_complejo import Cola


# Tests para Cola

def test_cola_hereda_de_coleccion():
    assert issubclass(Cola, Coleccion)


def test_cola_nueva_esta_vacia():
    cola = Cola()
    assert cola.esta_vacia() == True


def test_cola_agregar_un_elemento():
    cola = Cola()
    cola.agregar(1)
    assert cola.esta_vacia() == False
    assert cola.primero() == 1


def test_cola_agregar_varios_elementos():
    cola = Cola()
    cola.agregar(1)
    cola.agregar(2)
    cola.agregar(3)
    assert cola.primero() == 1  # FIFO: el primero agregado


def test_cola_sacar_devuelve_primero():
    cola = Cola()
    cola.agregar(1)
    cola.agregar(2)
    cola.agregar(3)
    assert cola.sacar() == 1  # FIFO
    assert cola.sacar() == 2
    assert cola.sacar() == 3


def test_cola_sacar_vacia_devuelve_none():
    cola = Cola()
    assert cola.sacar() == None


def test_cola_primero_no_saca():
    cola = Cola()
    cola.agregar(1)
    cola.agregar(2)
    assert cola.primero() == 1
    assert cola.primero() == 1  # Sigue siendo 1
    assert cola.esta_vacia() == False


def test_cola_primero_vacia_devuelve_none():
    cola = Cola()
    assert cola.primero() == None


def test_cola_iterar():
    cola = Cola()
    cola.agregar(1)
    cola.agregar(2)
    cola.agregar(3)

    elementos = list(cola)
    assert elementos == [1, 2, 3]  # Del frente hacia el final


def test_cola_iterar_vacia():
    cola = Cola()
    elementos = list(cola)
    assert elementos == []


def test_cola_iterar_no_modifica():
    cola = Cola()
    cola.agregar(1)
    cola.agregar(2)

    list(cola)  # Iterar
    assert cola.primero() == 1  # No se modificó
    assert cola.esta_vacia() == False


def test_cola_con_strings():
    cola = Cola()
    cola.agregar("a")
    cola.agregar("b")
    assert cola.sacar() == "a"
    assert cola.sacar() == "b"


# Tests de polimorfismo

def test_polimorfismo_misma_interfaz():
    """Verifica que Pila y Cola tienen la misma interfaz."""
    pila = Pila()
    cola = Cola()

    # Ambos tienen los mismos métodos
    for metodo in ['agregar', 'sacar', 'primero', 'esta_vacia', '__iter__']:
        assert hasattr(pila, metodo)
        assert hasattr(cola, metodo)


def test_polimorfismo_mismo_codigo():
    """El mismo código funciona con Pila o Cola."""

    def cargar_y_vaciar(coleccion):
        coleccion.agregar("A")
        coleccion.agregar("B")
        coleccion.agregar("C")

        resultado = []
        while not coleccion.esta_vacia():
            resultado.append(coleccion.sacar())
        return resultado

    # Mismo código, diferente resultado
    resultado_pila = cargar_y_vaciar(Pila())
    resultado_cola = cargar_y_vaciar(Cola())

    assert resultado_pila == ["C", "B", "A"]  # LIFO
    assert resultado_cola == ["A", "B", "C"]  # FIFO


def test_polimorfismo_iterar():
    """Ambas colecciones son iterables."""

    def obtener_elementos(coleccion):
        coleccion.agregar(1)
        coleccion.agregar(2)
        coleccion.agregar(3)
        return list(coleccion)

    elementos_pila = obtener_elementos(Pila())
    elementos_cola = obtener_elementos(Cola())

    assert elementos_pila == [3, 2, 1]  # LIFO
    assert elementos_cola == [1, 2, 3]  # FIFO
