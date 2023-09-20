# Análisis de Circuitos con Capacitores

Este repositorio contiene scripts en Python para analizar circuitos que involucran capacitores. Estos scripts calculan las expresiones de corriente y voltaje en los capacitores y también trazan las formas de onda correspondientes.

## Archivos

1. `Capacitor_Voltage_Expression.py` - Contiene el código para calcular la expresión del voltaje para una corriente dada que pasa a través de un capacitor de 175 µF.

   - Fórmula: \( V(t) = rac{1}{C} \int i(t) \, dt \)
2. `Current_Expression_Capacitor.py` - Contiene el código para calcular la expresión de la corriente para un voltaje dado en un capacitor de 75 µF y también traza la forma de onda.

   - Fórmula: \( i(t) = C rac{dV(t)}{dt} \)

## Requisitos

- Python 3.x
- sympy
- matplotlib
- numpy

## Instalación

Instale los paquetes requeridos utilizando pip:

```bash
pip install sympy matplotlib numpy
```
