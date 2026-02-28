# Tips para los ejercicios

## Ejercicio simple (Pila)

### Métodos básicos

Podés usar una lista interna para guardar los elementos. Pensá qué métodos de lista te sirven:
- `append()` agrega al final
- `pop()` saca del final y lo devuelve
- Acceder al último elemento: `lista[-1]`

Para `tope()` y `desapilar()`, acordate de verificar primero si la pila está vacía.

### El método mostrar()

Este es el más difícil porque **no podés recorrer la lista directamente** con un for.

Pensalo así: ¿cómo mostrarías todos los elementos si solo podés usar `desapilar()`, `apilar()`, `tope()` y `esta_vacia()`?

<details>
<summary>Pista 1</summary>

Vas a necesitar una estructura auxiliar para no perder los elementos.

</details>

<details>
<summary>Pista 2</summary>

Usá una **pila auxiliar**. Desapilá de la original, mostrá el elemento, y apilalo en la auxiliar.

</details>

<details>
<summary>Pista 3</summary>

Después de mostrar todo, tenés que restaurar la pila original. Pensá: si desapilaste todo a una auxiliar, ¿en qué orden quedaron? ¿Cómo los devolvés?

</details>

---

## Ejercicio complejo (ColaDeAtencion)

### Métodos básicos

Usá una lista interna para guardar los clientes. Recordá que es una COLA (FIFO): el primero que llega es el primero en irse.

- `append()` agrega al final (llega un cliente nuevo)
- `pop(0)` saca del principio (se atiende al primero)
- Acceder al primero: `lista[0]`

Para `atender()` y `siguiente()`, verificá primero si la cola está vacía.

### El método mostrar()

Igual que en la Pila, **no podés recorrer la lista directamente**.

<details>
<summary>Pista 1</summary>

Usá una **cola auxiliar**. Atendé de la original, mostrá el cliente, y agregalo a la auxiliar.

</details>

<details>
<summary>Pista 2</summary>

A diferencia de la pila, en la cola el orden se mantiene. Cuando pasás todos los clientes de la original a la auxiliar, quedan en el mismo orden.

</details>

<details>
<summary>Pista 3</summary>

Para restaurar, simplemente pasá todos los clientes de la auxiliar de vuelta a la original.

</details>
