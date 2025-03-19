xpoints = []
ypoints =[]
delta = []
deltasquare = []
deltacube = []
n =int(input("number of point ="))
for i in range (1,n+1):
    x,y =(input("enter the x and y vaues seperated by commas"))
    xpoints.append(x)
    ypoints.append(y)
    
tot =0
while tot<len(xpoints)-1:
    value = ypoints[(tot+1)] -ypoints[tot] 
    delta.append(value)
    tot = tot +1

print("table of first order differences",delta) 
tot =0
while tot<len(delta)-1:
    value = delta[(tot+1)] -delta[tot] 
    deltasquare.append(value)
    tot = tot +1 
    
print("table of second order differences",deltasquare)    
tot =0
while tot<len(deltasquare)-1:
    value = deltasquare[(tot+1)] -deltasquare[tot] 
    deltacube.append(value)
    tot = tot +1
print("table of third order differences",deltacube)

x = float(input("enter the value of x for interpolation:")) 

h=xpoints[1]-xpoints[0]
p = (x - xpoints[0])/h
print("p=",p)
print("h=",h)
yvalue = ypoints[0] + p*delta[0] + p*(p-1)*deltasquare[0]/2 + p*(p-1)(p-2)*deltacube[0]/6

print("Interpolated y value at x =", x, "is", yvalue)