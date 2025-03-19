import numpy as np
import matplotlib as plt

def f(x):
    return x**2-4
xpoint =np.linspace(0,10,10)


aray =np.arange(0,10,1)
print(aray)
print(xpoint)
my_array = np.random.randint(0, 20, size=10)

print(my_array)
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = x**2+6

plt.plot(x, y, label='f(x)=x**2+6')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of y = x^2')

plt.legend()

# Display the plot
plt.show()

def simf(x):
    return x**3 + 6

    
