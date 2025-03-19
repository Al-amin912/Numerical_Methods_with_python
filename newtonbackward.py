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

# Additional input
x = float(input("Enter the value of x for interpolation: "))

# Calculate p and h
h = xpoints[1] - xpoints[0]
p = (x - xpoints[3]) / h

print("p =", p)
print("h =", h)

# Perform interpolation
yvalue = ypoints[3] + p * delta[2] + p * (p - 1) * deltasquare[1] / 2 + p * (p - 1) * (p - 2) * deltacube[0] / 6

print("Interpolated y value at x =", x, "is", yvalue)
