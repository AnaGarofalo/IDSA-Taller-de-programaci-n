# Tips para los ejercicios

## Ejercicio simple (a_lista y agregar)

### Para a_lista:
- Crear una lista vacía de Python
- Recorrer cada nodo desde la cabeza
- Agregar cada valor a la lista

### Para agregar (sobrecarga pythónica):

El método tiene un parámetro con valor por defecto:

```python
def agregar(self, valor, posicion=0):
```

Esto permite llamarlo de dos formas:
- `agregar(5)` → usa posicion=0 (al principio)
- `agregar(5, 2)` → usa posicion=2

### Casos a manejar:

**Posición 0 (al principio)** - Es O(1), no hay que recorrer:
1. Crear un nuevo Nodo
2. El nuevo nodo apunta a la cabeza actual
3. La cabeza ahora es el nuevo nodo

**Otras posiciones** - Es O(n), hay que recorrer:
1. Crear un nuevo Nodo
2. Recorrer hasta la posición anterior (posicion - 1)
3. Insertar el nuevo nodo entre el actual y su siguiente

**Posición mayor al tamaño** - Agrega al final:
- Si mientras recorrés llegás a None, insertá ahí

---

## Ejercicio complejo (invertir)

Necesitás cambiar hacia dónde apunta cada nodo:
- El primero debe apuntar a None (se convierte en el último)
- Cada nodo debe apuntar al anterior
- El último se convierte en la cabeza

Usá tres variables: `anterior`, `actual`, `siguiente`. En cada paso:
1. Guardá el siguiente (para no perderlo)
2. Hacé que actual apunte al anterior
3. Avanzá: anterior = actual, actual = siguiente
