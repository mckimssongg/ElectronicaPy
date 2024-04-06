# Importar las librerías necesarias para la simplificación lógica
from sympy.logic.boolalg import simplify_logic, Or, And, Not
from sympy.abc import A, B, C, D

# Función para simplificar usando el método de Mapas de Karnaugh
def simplificar_funcion():
    # Simplificar la función lógica
    funcion_simplificada = simplify_logic(Or(And(Not(A), Not(B), Not(C), Not(D)), 
                                             And(A, Not(B), Not(C), Not(D))), form='dnf')
    return funcion_simplificada

# Definir la función simplificada para uso en pruebas
def funcion_simplificada_test(B, C, D):
    return not B and not C and not D

# Crear un conjunto de pruebas para validar la función simplificada
def ejecutar_pruebas():
    pruebas = [
        (0, 0, 0, True),  # Todos falsos, debe ser verdadero según la simplificación
        (1, 0, 0, False), # B verdadero, debe ser falso
        (0, 1, 0, False), # C verdadero, debe ser falso
        (0, 0, 1, False), # D verdadero, debe ser falso
        (1, 1, 1, False), # Todos verdaderos, debe ser falso
        (1, 1, 0, False), # B y C verdaderos, debe ser falso
        (0, 1, 1, False), # C y D verdaderos, debe ser falso
    ]

    resultados = [funcion_simplificada_test(B, C, D) == resultado_esperado for B, C, D, resultado_esperado in pruebas]
    return all(resultados)

# Ejecutar simplificación y pruebas
if __name__ == "__main__":
    funcion_simplificada = simplificar_funcion()
    print(f"Función simplificada: {funcion_simplificada}")

    if ejecutar_pruebas():
        print("Todas las pruebas han pasado exitosamente.")
    else:
        print("Algunas pruebas no han pasado.")



