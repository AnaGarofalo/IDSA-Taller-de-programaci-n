# Tips para los ejercicios

## Ejercicio simple (factorial)

- Pensá: ¿cuál es el caso más simple donde ya sabés la respuesta sin calcular nada?
- Pensá: ¿cómo podés expresar factorial(n) en términos de factorial de un número más chico?

## Ejercicio complejo (aplanar)

- Recorré cada elemento de la lista
- Si el elemento es una lista, aplanalo recursivamente
- Si no es una lista, agregalo al resultado
- Para verificar si algo es una lista: `isinstance(elemento, list)`
