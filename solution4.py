def rk4_solver(f, y0, x0, tf, h):#solution (a)
    #solution (b) implement start
    x = x0
    y = y0
    while x <= tf:
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)
        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        x = x + h
    return y


def f(x, y):
    return -2*x*y #solutioon (a)

y0 = 1
x0 = 0
xf = 0.2
h =0.05
#solution (b) finished 

y_sol = rk4_solver(f, y0, x0, xf, h)

print("Solution at x = ", xf, " is: ", y_sol)#solution (c)