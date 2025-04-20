import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the differential equation: dy/dt = -2y
def model(y, t):
    dydt = -2 * y
    return dydt

# Initial condition: y(0) = 1
y0 = 1

# Time points where the solution is computed
t = np.linspace(0, 5, 100)

# Solve the ODE
y = odeint(model, y0, t)

# Plot the result
plt.plot(t, y)
plt.xlabel('Time t')
plt.ylabel('Solution y(t)')
plt.title('Solution of dy/dt = -2y')
plt.grid()
plt.show()
