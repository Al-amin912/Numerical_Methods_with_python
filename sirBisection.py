import time
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 4*x**2 + 3*x + 1
def bisection_method(func, a, b, epsilon, max_iterations):
    if func(a) * func(b) >= 0:
        raise ValueError("The bisection method requires that f(a) and f(b) have opposite signs.")
    
    iterations = 0
    
    while (b - a) >= epsilon and iterations < max_iterations:
        c = (a + b) / 2
        f_c = func(c)
        
        if abs(f_c) < epsilon:
            return c, iterations
        
        if func(a) * f_c < 0:
            b = c
        else:
            a = c
        
        iterations += 1
    
    return (a + b) / 2, iterations

# Interval [a, b]
a = 1
b = 2

# Tolerance level
epsilon = 1e-6

# Maximum number of iterations
max_iterations = 100

start_time = time.time()
root, iterations = bisection_method(f, a, b, epsilon, max_iterations)
execution_time = time.time() - start_time

# Calculate functional values in the interval
x_values = [a, root, b]
y_values = [f(a), f(root), f(b)]

# Calculate degrees of error curves and relative errors
error_degrees = [abs(f(root)) for _ in range(iterations)]
relative_errors = [error / abs(f(root)) for error in error_degrees]

print("Interval [a, b]:", "[", a, b, "]")
print("Initial guesses for the root:", a, b)
print("Number of iterations:", iterations)
print("Execution time (seconds):", execution_time)
print("Approximate root:", root)
print("Functional values at interval points:", y_values)
print("Degrees of error curves:", error_degrees)
print("Relative errors:", relative_errors)

# Plot the functional values and root
plt.plot(x_values, y_values, label='Function')
plt.scatter(root, f(root), color='red', marker='o', label='Root')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.title('Functional Values and Root')
plt.show()
