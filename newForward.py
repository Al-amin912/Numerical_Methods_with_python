import numpy as np
import matplotlib.pyplot as plt
xpoints = []
ypoints = []
delta = []
deltasquare = []
deltacube = []

# Input number of points
n = int(input("Number of points: "))

# Input data points
for i in range(1, n+1):
    x, y = map(float, input("Enter the x and y values separated by commas: ").split(","))
    xpoints.append(x)
    ypoints.append(y)

# Calculate first-order differences
for i in range(len(ypoints)-1):
    value = ypoints[i+1] - ypoints[i]
    delta.append(value)

print("Table of first-order differences:", delta)

# Calculate second-order differences
for i in range(len(delta)-1):
    value = delta[i+1] - delta[i]
    deltasquare.append(value)

print("Table of second-order differences:", deltasquare)

# Calculate third-order differences
for i in range(len(deltasquare)-1):
    value = deltasquare[i+1] - deltasquare[i]
    deltacube.append(value)

print("Table of third-order differences:", deltacube)
def newton(x):
    h = xpoints[1] - xpoints[0]
    p = (x - xpoints[0]) / h
    yvalue = ypoints[0] + p * delta[0] + p * (p - 1) * deltasquare[0] / 2 + p * (p - 1) * (p - 2) * deltacube[0] / 6
    return yvalue

x = float(input("Enter the value of x for interpolation: "))

# Perform interpolation
yvalue=newton(x)
print("Interpolated y value at x =", x, "is", yvalue)

# Plotting the interpolation polynomial along with the data points
x_plot = np.linspace(min(xpoints), max(xpoints), 100)
y_plot = newton(x_plot)

plt.scatter(xpoints, ypoints, label='Data Points', color='red')
plt.plot(x_plot, y_plot, label="Newton's Forward Difference Interpolation Polynomial")
plt.scatter(x, yvalue, label='Interpolation at', color='green')
plt.xlabel('x')
plt.ylabel('Interpolated y')
plt.legend()
plt.show()

