def bisection_method(func, a, b, tolerance=1e-20, max_iterations=100):

    if func(a) * func(b) > 0:
        raise ValueError("The function must have different signs at the interval endpoints.")

    root = None
    iterations = 0

    while (b - a) / 2 > tolerance and iterations < max_iterations:
        c = (a + b) / 2
        if func(c) == 0:
            root = c
            break
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c

        iterations += 1

    root = (a + b) / 2
    return root, iterations

# Example usage:
def example_function(x):
    return x*2 - 4

root, iterations = bisection_method(example_function, 0, 3)
print("Root:", root)
print("Iterations:", iterations)
