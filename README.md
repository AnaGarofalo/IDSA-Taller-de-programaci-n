# Taller de programación

Este curso contiene 8 temas con ejercicios prácticos para aprender conceptos de programación.

## Requisitos

- Python 3.8 o superior
- pytest (para correr los tests)

Para instalar pytest:

```bash
pip install pytest
```

## Estructura del curso

```
├── 01_list_comprehensions/
├── 02_complejidad_algoritmica/
├── 03_ordenamiento/
├── 04_busqueda/
├── 05_pilas_y_colas/
├── 06_listas_enlazadas/
├── 07_recursividad/
└── 08_arboles_binarios/
```

Cada carpeta contiene:

- `README.md` - Explicación del tema
- `ejercicio_simple.py` - Ejercicio inicial
- `ejercicio_complejo.py` - Ejercicio avanzado
- `test_simple.py` - Tests para el ejercicio simple
- `test_complejo.py` - Tests para el ejercicio complejo
- `tips.md` - Pistas para resolver los ejercicios (solo si te trabás)
- `soluciones.py` - Soluciones de ambos ejercicios (solo para verificar después de resolver)

## Cómo trabajar con cada clase

### Paso 1: Leer el README

Abrí el `README.md` de la carpeta y leé la explicación del tema. Tomáte tu tiempo para entender los conceptos y ejemplos.

### Paso 2: Resolver el ejercicio simple

1. Abrí `ejercicio_simple.py`
2. Leé las instrucciones y ejemplos en el docstring
3. Completá la función donde dice `# TODO`
4. Guardá el archivo

### Paso 3: Correr los tests

Desde la carpeta del ejercicio, ejecutá:

```bash
pytest test_simple.py -v
```

o en powershel

```bash
python -m pytest test_simple.py -v
```

La opción `-v` (verbose) muestra el detalle de cada test.

Si los tests fallan, revisá el mensaje de error y corregí tu código.

### Paso 4: Si te trabás

Abrí `tips.md` para ver pistas que te ayuden a resolver el ejercicio.

### Paso 5: Resolver el ejercicio complejo

Una vez que pasen todos los tests del ejercicio simple, repetí el proceso con `ejercicio_complejo.py`:

```bash
pytest test_complejo.py -v
```

## Comandos útiles

### Correr los tests de un ejercicio específico

```bash
# Ejercicio simple
pytest test_simple.py -v

# Ejercicio complejo
pytest test_complejo.py -v
```

### Correr todos los tests de una carpeta

```bash
pytest -v
```

### Correr un test específico

```bash
pytest test_simple.py::test_lista_vacia -v
```

### Ver solo los tests que fallan

```bash
pytest -v --tb=short
```

### Parar en el primer error

```bash
pytest -v -x
```

## Orden sugerido

Las clases están numeradas pero son independientes. Podés hacerlas en cualquier orden, aunque se sugiere:

1. **01_list_comprehensions** - Herramientas de Python
2. **02_complejidad_algoritmica** - Entender eficiencia
3. **03_ordenamiento** - Algoritmos clásicos
4. **04_busqueda** - Búsqueda lineal y binaria
5. **05_pilas_y_colas** - Estructuras básicas + herencia y polimorfismo
6. **06_listas_enlazadas** - Estructuras enlazadas + sobrecarga
7. **07_recursividad** - Funciones que se llaman a sí mismas
8. **08_arboles_binarios** - Estructuras jerárquicas

## Tips generales

- No mires los tips a menos que estés realmente trabado
- No mires las soluciones hasta haber resuelto el ejercicio (o haberlo intentado mucho)
- Si un test falla, leé bien el mensaje de error
- Probá tu código manualmente antes de correr los tests
- No uses funciones que el ejercicio te pide no usar (como `sorted()` en ordenamiento)
