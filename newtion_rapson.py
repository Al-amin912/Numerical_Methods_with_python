
def f(x):
    return x**3 - 6*x**2 + 11*x - 6

def df(x):
    return 3*x**2 -12*x +11

def newton_raphson(f, df, x0, tolerance, max_iteration):
    iterations = 0
    x = x0
    while abs(f(x)) > tolerance and iterations < max_iteration:
        x = x - f(x) / df(x)
        iterations += 1
    return x, iterations


x0 = float(input("Enter the start of the interval (a): "))
tolerance = float(input("Enter the tolerance: "))
max_iterations = int(input("Enter the maximum number of iterations: "))

root, iterations = newton_raphson(f, df,x0 ,tolerance ,max_iterations )
print("Root:", root)
print("Iterations:", iterations)
