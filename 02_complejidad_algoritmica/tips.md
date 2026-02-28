# Tips para los ejercicios

## Ejercicio simple (identificar_complejidad)

Contá los loops y pensá cómo crece el tiempo con más datos:
- Sin loops sobre n → probablemente O(1)
- Un loop → probablemente O(n)
- Loops anidados → probablemente O(n²)
- Dividir a la mitad en cada paso → probablemente O(log n)

## Ejercicio complejo (encontrar_pares_rapido)

Para cada número, pensá: ¿qué número necesitaría para llegar al objetivo?
Ese número es el "complemento" (objetivo - número_actual).

Si podés buscar el complemento en O(1), resolvés el problema en O(n) total.
¿Qué estructura de datos te permite buscar en O(1)?
