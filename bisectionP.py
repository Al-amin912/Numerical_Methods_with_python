def bisection(f,a,b,tol=1e-6,max_iteration=100):
    if f(a)*f(b)>0:
        raise ValueError("a and b must be differaent singn")   
       
    iteration=0   
    while(b-a)/2> tol and iteration<max_iteration:
        c=(a+b)/2
        if f(c)==0:
            break           
        elif f(c)*f(a)<0:
            b=c            
        else:
            a=c
        iteration +=1
    return c , iteration
def f(x):
    return x**2-4
root,iteration=bisection(f,0,3)
print(root)
print(iteration)