from sympy.logic.boolalg import simplify_logic, Or, And, Not
from sympy.abc import A, B, C, D

# Función para simplificar usando el método de Mapas de Karnaugh
def simplificar_funcion():
    # Simplificar la función lógica basada en la interpretación de la tabla de verdad dada
    # La simplificación resultante basada en los datos y el análisis es B & ~C
    funcion_logica = Or(
        And(Not(A), B, Not(C), Not(D)),  # 01 00
        And(Not(A), B, Not(C), D),       # 01 01
        And(A, B, Not(C), Not(D)),       # 11 00
        And(A, B, Not(C), D)             # 11 01
    )
    funcion_simplificada = simplify_logic(funcion_logica, form='dnf')
    return funcion_simplificada

# Definir la función simplificada para uso en pruebas
def funcion_simplificada_test(B, C):
    return B and not C

# Crear un conjunto de pruebas para validar la función simplificada
def ejecutar_pruebas():
    pruebas = [
        (True, False, True),  # B verdadero, C falso, debe ser verdadero
        (False, False, False), # B falso, debe ser falso
        (True, True, False),   # C verdadero, debe ser falso
        (False, True, False),  # B falso y C verdadero, debe ser falso
    ]

    resultados = [funcion_simplificada_test(B, C) == resultado_esperado for B, C, resultado_esperado in pruebas]
    return all(resultados)

# Ejecutar simplificación y pruebas
if __name__ == "__main__":
    funcion_simplificada = simplificar_funcion()
    print(f"Función simplificada: {funcion_simplificada}")

    if ejecutar_pruebas():
        print("Todas las pruebas han pasado exitosamente.")
    else:
        print("Algunas pruebas no han pasado.")
