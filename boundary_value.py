import numpy as np
import matplotlib.pyplot as plt

def finite_difference(N):
  """
  Solves the BVP using Finite Difference Method with N internal nodes.

  Args:
      N: Number of internal nodes.

  Returns:
      x: Array of points in the domain.
      y: Array of approximate solution values at each point.
  """
  h = 1.0 / (N + 1)  # Step size
  x = np.linspace(0, 1, N + 2)  # Grid points including boundaries
  
  # Tridiagonal matrix coefficients
  a = np.ones(N + 1)
  b = -2.0 * np.ones(N + 1)
  c = np.ones(N + 1)

  # Boundary conditions
  a[0] = 0.0
  c[N] = 0.0
  b[0] = 1.0  # Incorporate boundary condition at x=0, y(0) = 1
  b[N] = 1.0  # Incorporate boundary condition at x=1, y(1) = 2

  # Right-hand side vector
  f = x

  # Modify f for boundary conditions
  f[0] = 1.0 - b[0] * x[0]
  f[N] = 2.0 - b[N] * x[N]

  # Solve the tridiagonal system
  y = np.linalg.solve_tridiag(a, b, c, f)

  return x, y

# Example usage with N = 10
N = 10
x, y = finite_difference(N)

# Plot the solution
plt.plot(x, y, label="Numerical solution")

# Add exact solution for comparison (y = x^2 + 1)
plt.plot(x, x**2 + 1, label="Exact solution")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.title(f"Numerical solution with N = {N}")
plt.show()

# Print discussion on impact of changing N
print("**Impact of changing N:**")
print("Increasing the number of internal nodes (N) generally leads to a more accurate")
print("approximation of the solution. This is because the discretization error, caused by")
print("representing the continuous problem with a finite number of points, decreases with")
print("a finer mesh. However, there is a trade-off between accuracy and computational cost.")
print("As N increases, the size of the linear system and the computational effort required")
print("to solve it also increase.")
