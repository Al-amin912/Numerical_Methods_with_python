def bisection(f,a,b,tol=0.00000000005,max_iteration=100):
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
    return x**3-6*x**2+11*x-6
#for error
root,iteration=bisection(f,4,5)
print("root is ",root)
print("iteration",iteration)