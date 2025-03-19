

#solution(a):
#and implement(b)
def newton_raphson(f, df, x0, tol=1e-6, max_iteration=):#solutioin d(using tolerence and maximum iteration)
    iteration = 0
    x = x0
    while abs(f(x)) > tol and iteration < max_iteration:
        x = x - f(x) / df(x)
        iteration += 1
    return x, iteration

def f(x):
    return x**3-6*x**2+11*x-6

def df(x):
    return 3*x**2-12*x+11
#implement finish(b finished)

root, iteration = newton_raphson(f, df,0)#solution c(taking initial ngauses is 0)
print("Root:", root)
print("Iterations:", iteration)#solution (e) result show with itaration and root