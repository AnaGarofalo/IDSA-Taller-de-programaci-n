# Tips para los ejercicios

## Ejercicio simple (agregar y a_lista)

Para agregar:
- Crear un nuevo Nodo con el valor
- Si la lista está vacía, el nuevo nodo es la cabeza
- Si no, recorrer hasta el último nodo y conectar el nuevo

Para a_lista:
- Crear una lista vacía de Python
- Recorrer cada nodo y agregar su valor a la lista

## Ejercicio complejo (invertir)

Necesitás cambiar hacia dónde apunta cada nodo:
- El primero debe apuntar a None (se convierte en el último)
- Cada nodo debe apuntar al anterior
- El último se convierte en la cabeza

Usá tres variables: `anterior`, `actual`, `siguiente`. En cada paso:
1. Guardá el siguiente (para no perderlo)
2. Hacé que actual apunte al anterior
3. Avanzá: anterior = actual, actual = siguiente
