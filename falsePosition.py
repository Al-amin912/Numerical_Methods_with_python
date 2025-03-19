import math 
def false_position(f, a, b, tol=1e-6, max_iteration=1000):
    if f(a) * f(b) > 0:
        raise ValueError("a and b must have different signs.")   
       
    iteration = 0   
    while (b - a) / 2 > tol and iteration < max_iteration:
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if f(c) == 0:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iteration += 1
    return c, iteration

def f(x):
    return 3*x-math.cos(x)-1

root, iteration = false_position(f, 0, 1)
print("Root:", root)
print("Iterations:", iteration)
