
from sympy import integrate, pi, sin, symbols

# Define symbols
t = symbols('t')

# Given current and capacitance
i_t_given = 30 * sin(450 * t + 40 * pi / 180)
C_given = 175e-6  # Capacitance in Farads

# Calculating the voltage V(t)
V_t_given = (1 / C_given) * integrate(i_t_given, t)
V_t_simplified = V_t_given.simplify()

# Display the simplified voltage expression
print(f"Simplified Voltage Expression: {V_t_simplified}")
