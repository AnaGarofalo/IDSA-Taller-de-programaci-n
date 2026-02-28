# Generadores e Iteradores

## El problema

Imaginá que tenés un archivo de 10 GB con datos para analizar. Si hacés esto:

```python
datos = archivo.read()  # ¡10 GB en memoria!
```

Tu computadora probablemente se trabe. ¿La solución? Procesar los datos de a poco, sin cargar todo en memoria.

## ¿Qué es un generador?

Un generador es una función especial que **produce valores uno a la vez**, en lugar de crear una lista completa en memoria.

### La diferencia clave: `return` vs `yield`

```python
# Función normal - crea toda la lista de una
def pares_lista(n):
    resultado = []
    for i in range(0, n, 2):
        resultado.append(i)
    return resultado  # Devuelve todo junto

# Generador - produce de a uno
def pares_generador(n):
    for i in range(0, n, 2):
        yield i  # Devuelve uno y "pausa"
```

### ¿Cómo funciona `yield`?

1. Cuando la función llega a `yield`, devuelve el valor
2. La función se "pausa" y recuerda dónde quedó
3. La próxima vez que se pida un valor, continúa desde donde pausó
4. Cuando no hay más `yields`, el generador termina

### Ejemplo paso a paso

```python
def contar_hasta_3():
    print("Empezando...")
    yield 1
    print("Después del 1...")
    yield 2
    print("Después del 2...")
    yield 3
    print("Terminando...")

gen = contar_hasta_3()
# Todavía no pasó nada

print(next(gen))
# Imprime: Empezando...
# Imprime: 1

print(next(gen))
# Imprime: Después del 1...
# Imprime: 2

print(next(gen))
# Imprime: Después del 2...
# Imprime: 3

print(next(gen))
# Imprime: Terminando...
# Error: StopIteration (no hay más valores)
```

---

## Usando generadores

### Con un for loop

La forma más común:

```python
for numero in pares_generador(10):
    print(numero)
# Imprime: 0, 2, 4, 6, 8
```

### Convertir a lista

Si necesitás todos los valores:

```python
lista = list(pares_generador(10))
# [0, 2, 4, 6, 8]
```

### Con next()

Para obtener valores uno por uno:

```python
gen = pares_generador(10)
primero = next(gen)  # 0
segundo = next(gen)  # 2
```

---

## ¿Por qué usar generadores?

### 1. Ahorro de memoria

```python
# MAL - Crea una lista de 1 millón de elementos en memoria
cuadrados = [x**2 for x in range(1000000)]

# BIEN - Genera de a uno, casi sin usar memoria
cuadrados = (x**2 for x in range(1000000))
```

### 2. Datos infinitos

```python
def numeros_infinitos():
    n = 0
    while True:
        yield n
        n += 1

# Podés tomar los que necesites
gen = numeros_infinitos()
for _ in range(5):
    print(next(gen))  # 0, 1, 2, 3, 4
```

### 3. Procesamiento de archivos grandes

```python
def leer_lineas(archivo):
    with open(archivo) as f:
        for linea in f:
            yield linea.strip()

# Procesa línea por línea, sin cargar todo
for linea in leer_lineas("archivo_enorme.txt"):
    procesar(linea)
```

---

## Expresiones generadoras

Es como una list comprehension, pero con paréntesis:

```python
# List comprehension - crea lista en memoria
lista = [x**2 for x in range(1000)]

# Generator expression - genera de a uno
generador = (x**2 for x in range(1000))
```

Útil para pasar directamente a funciones:

```python
suma = sum(x**2 for x in range(1000))  # Eficiente
```

---

## Comparación de memoria

| Tipo | 1,000 elementos | 1,000,000 elementos |
|------|-----------------|---------------------|
| Lista | ~8 KB | ~8 MB |
| Generador | ~100 bytes | ~100 bytes |

El generador siempre usa la misma memoria, sin importar cuántos elementos.

---

## Ejercicios

1. **ejercicio_simple.py**: Crear un generador de números pares
2. **ejercicio_complejo.py**: Generador que procesa datos en chunks (bloques)
