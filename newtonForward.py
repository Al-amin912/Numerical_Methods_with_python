

def newton_forward_difference(x, y, t):
    """
    Find the Newton polynomial through the points (x, y) and return its value at t.
    """

    # Newton Forward Difference Interpolation [By Bottom Science]

    # Check that the input arrays have the same length
    if len(x) != len(y):
        raise ValueError("The arrays x and y must have the same length.")

    # Initialize the polynomial
    p = y.copy()

    # Loop over the differences
    for i in range(1, len(x)):
        # Update the polynomial
        for j in range(len(x) - i):
            p[j] = (p[j + 1] - p[j]) / (x[i + j] - x[j])

    # Evaluate the polynomial at t
    result = p[0]
    for i in range(1, len(x)):
        term = p[i]
        for j in range(i):
            term *= (t - x[j])
        result += term

    return result

# DATA POINTS (x,y)

x = [0, 1, 2]
y = [0, 1, 4]
t = 0.5
p = newton_forward_difference(x, y, t)
print(p)

#Output - 1.5