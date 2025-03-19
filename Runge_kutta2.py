
import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return -2*x*y

def rk4_solver(f, x0, y0, tf, h):
    x_values = np.arange(x0, tf + h, h)
    y_values = []

    x = x0
    y = y0
    for x in x_values:
        y_values.append(y)
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)
        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6

    return x_values, y_values


x0 = float(input("Enter the initial condition (x0): "))
y0= float(input("Enter the initial condition (y0): "))
tf = float(input("Enter the value of x: "))
h = float(input("Enter the step size (h): "))


x_values, y_values = rk4_solver(f, x0, y0, tf, h)
print("value,",y_values)

# Plot the result
plt.plot(x_values, y_values, label='Runge-Kutta 4th Order')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.show()