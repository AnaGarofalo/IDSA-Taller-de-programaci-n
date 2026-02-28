"""
EJERCICIO: Paréntesis balanceados

Implementá la función parentesis_balanceados que verifique si una expresión
tiene los paréntesis, corchetes y llaves correctamente balanceados.

Una expresión está balanceada si:
- Cada símbolo de apertura tiene su correspondiente cierre
- Los símbolos se cierran en el orden correcto

Símbolos válidos: (), [], {}

Ejemplo:
    parentesis_balanceados("()")           → True
    parentesis_balanceados("([{}])")       → True
    parentesis_balanceados("([])")         → True
    parentesis_balanceados("(")            → False  (no se cierra)
    parentesis_balanceados(")")            → False  (no se abrió)
    parentesis_balanceados("([)]")         → False  (orden incorrecto)
    parentesis_balanceados("")             → True   (vacío está balanceado)
    parentesis_balanceados("hola")         → True   (sin paréntesis)
    parentesis_balanceados("(a + b) * c")  → True
"""


def parentesis_balanceados(expresion):
    """
    Verifica si los paréntesis, corchetes y llaves están balanceados.

    Args:
        expresion: String con la expresión a verificar

    Returns:
        True si está balanceado, False si no
    """
    # TODO: Implementar verificación con pila
    pass
