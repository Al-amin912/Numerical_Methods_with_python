import numpy as np
import matplotlib.pyplot as plt

def lagrange(x, y, t):
    p = 0

    for i in range(len(x)):
        xi, yi = x[i], y[i]
        term = yi
        for j in range(len(x)):
            if i == j:
                continue
            term *= ((t - x[j]) / (xi - x[j]))

        p += term
    return p

def display_coefficients(x, y):
    for i, coefficient in enumerate(y):
        print(f'Coefficient {i}: {coefficient}')

# Given data points
x_data = []
y_data = []
n=4
for i in range(1, n+1):
    x, y = map(float, input("Enter the x and y values separated by commas: ").split(","))
    x_data.append(x)
    y_data.append(y)
t_point=float( input("Enter the the vlue of x "))
# Interpolate at a specific point
interpolated_value = lagrange(x_data, y_data, t_point)

# Display coefficients
display_coefficients(x_data, y_data)

# Plotting the interpolation polynomial along with the data points
x_plot = np.linspace(min(x_data), max(x_data), 100)
y_plot = [lagrange(x_data, y_data, x) for x in x_plot]

plt.scatter(x_data, y_data, label='Data Points', color='red')
plt.plot(x_plot, y_plot, label='Lagrange Interpolation Polynomial')
plt.scatter(t_point, interpolated_value, label=f'Interpolation at {t_point}', color='green')
plt.xlabel('x')
plt.ylabel('Interpolated y')
plt.legend()
plt.show()
