# Tips para los ejercicios

## Ejercicio simple (a_lista, agregar_al_principio, agregar_al_final)

Para a_lista:
- Crear una lista vacía de Python
- Recorrer cada nodo desde la cabeza
- Agregar cada valor a la lista

Para agregar_al_principio (es O(1), no hay que recorrer nada):
- Crear un nuevo Nodo
- El nuevo nodo apunta a la cabeza actual
- La cabeza ahora es el nuevo nodo

Para agregar_al_final (es O(n), hay que recorrer todo):
- Crear un nuevo Nodo
- Si la lista está vacía, el nuevo nodo es la cabeza
- Si no, recorrer hasta el último nodo y conectar el nuevo

## Ejercicio complejo (invertir)

Necesitás cambiar hacia dónde apunta cada nodo:
- El primero debe apuntar a None (se convierte en el último)
- Cada nodo debe apuntar al anterior
- El último se convierte en la cabeza

Usá tres variables: `anterior`, `actual`, `siguiente`. En cada paso:
1. Guardá el siguiente (para no perderlo)
2. Hacé que actual apunte al anterior
3. Avanzá: anterior = actual, actual = siguiente
