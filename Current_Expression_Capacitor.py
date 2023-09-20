
from sympy import diff, pi, sin, cos, symbols
import matplotlib.pyplot as plt
import numpy as np

# Define symbols
t = symbols('t')

# Given voltage and capacitance
V_t = 90 * sin(200 * t)
C = 75e-6  # Capacitance in Farads

# Take the derivative of the voltage to find the current
dV_dt = diff(V_t, t)

# Calculate the current
i_t = C * dV_dt

# Simplify the expression
i_t_simplified = i_t.simplify()

# Display the simplified current expression
print(f"Simplified Current Expression: {i_t_simplified}")

# Plotting the waveforms
t_values = np.linspace(0, 0.05, 500)  # 0 to 50 ms
i_values = 1.35e3 * np.cos(200 * 2 * np.pi * t_values)  # Converting angular frequency to Hz

plt.figure(figsize=(10, 6))
plt.title('Current Waveform')
plt.xlabel('Time (s)')
plt.ylabel('Current (A)')
plt.plot(t_values, i_values)
plt.grid(True)
plt.show()
