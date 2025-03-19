def f(x):
    return x**3 - 6*x**2 + 11*x - 6


def bisection(f, a, b, tolerance, max_iterations):
    if f(a) * f(b) > 0:
        raise ValueError("a and b must have different signs.")   
       
    iteration = 0   
    while iteration < max_iterations:
        c = (a + b) / 2
        if abs(f(c)) < tolerance:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iteration += 1
    return c, iteration

a = float(input("Enter the start of the interval (a): "))
b = float(input("Enter the end of the interval (b): "))
tolerance = float(input("Enter the tolerance: "))
max_iterations = int(input("Enter the maximum number of iterations: "))


root, iterations = bisection(f, a, b,tolerance,max_iterations)
print("Approximate root:",root)
print("Number of iterations:", iterations)
