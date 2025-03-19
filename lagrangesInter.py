
def lagrange(x, y, t):
    
    p = 0

    for i in range(0,len(x)):
        xi, yi = x[i], y[i]
        term = yi
        for j in range(len(x)):
            if i == j:
                continue
            term *= ((t - x[j]) / (xi - x[j]))

        p += term
    return p
# question e jai valu thakbe
x = [0, 2, 3,5,6]
y = [5, 7, 8,10,12]
t = 4
p = lagrange(x, y, t)
print(p)




     
 

     