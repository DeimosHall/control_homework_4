#!/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define constants
a = 1
b = 1
T = 0.5

# Define the differential equation
def model(y, t):
    dydt = -a*y + b
    return dydt

# Define the time span
t = np.linspace(0, 10, 1000)

# Define the initial conditions
y0 = 0

# Resolve the differential equation
y = odeint(model, y0, t)

# Graph the response to the unit step
plt.plot(t, y, 'b-', label='y(t)')
plt.plot([0, 10], [1, 1], 'r--', label='Step')
plt.xlabel('Tiempo')
plt.ylabel('y(t)')
plt.title('Respuesta al escalón unitario')
plt.legend()
plt.show()
