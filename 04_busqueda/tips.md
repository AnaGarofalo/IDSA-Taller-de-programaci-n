# Tips para los ejercicios

## Ejercicio simple (busqueda_lineal)

Recorré la lista con un `for` usando `enumerate` para tener el índice, y compará cada elemento con el objetivo.

## Ejercicio complejo (busqueda_binaria)

Usá dos variables (`izquierda` y `derecha`) para ir achicando el rango de búsqueda. El medio se calcula como:
```python
medio = (izquierda + derecha) // 2
```
