# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 22:56:20 2024

@author: Dea
"""

import numpy as np
import pandas as pd

# Definir los datos de entrada
x = np.array([[1, -1, -1], [1, 1, -1], [1, -1, 1], [1, 1, 1]])  # Matriz de entrada
w_cero = np.array([1, 1, 1])  # Vector de pesos inicial
y = np.array([-1, -1, -1, 1])  # Vector de salidas esperadas
alfa = 0.5  # Tasa de aprendizaje

w_act = w_cero  # Inicializar los pesos actuales con los pesos iniciales

# Listas para almacenar los datos de cada iteración
iteraciones = []  # Número de iteración
dots = []  # Producto punto
y_signs = []  # Signo de la salida
w_acts = []  # Pesos actuales

# Iterar sobre cada fila de la matriz de entrada
for i in range(len(x)):
    p = x[i, :]  # Vector de entrada actual
    dot = np.dot(w_act, p)  # Calcular el producto punto
    y_sign = np.sign(dot)  # Calcular el signo de la salida

    # Actualizar los pesos si la salida no coincide con la salida esperada
    if y[i] != y_sign:
        y_resta = y[i] - y_sign
        producto_alfa = alfa * (y_resta * p)
        w_act = w_act + producto_alfa

    # Almacenar los valores de esta iteración
    iteraciones.append(i + 1)
    dots.append(dot)
    y_signs.append(y_sign)
    w_acts.append(w_act)

# Crear un DataFrame para mostrar los resultados
df = pd.DataFrame({
    "Iteración (X0-X4)": iteraciones,
    "Dot": dots,
    "y_sign": y_signs,
    "w_act": w_acts
})

print(df)  # Imprimir el DataFrame con los resultados
