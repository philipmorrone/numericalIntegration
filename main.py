import math

def myf(x):
    #return math.exp(x)  
    return x**3
    #return math.exp((-1)*x)
    #return math.sin(math.pi*x)

def ni(a,b,n,rule,f):
    deltax = (b-a)/n
    points = []
    trapPoints = []
    midpoints = []
    final = []
    if rule == "midpoint":
        for i in range(n+1):
            x = a + (i*deltax)
            points.append(x)
        for j in range(len(points)-1):
            midpoints.append((points[j] + points[j+1])/2)
        for k in range(len(midpoints)):
            final.append(f(midpoints[k]))
        print(sum(final)*deltax)
        
    elif rule == "trapezoid":
        for i in range(n+1):
            x = a + (i*deltax)
            trapPoints.append(x)
        for j in range(len(trapPoints)):
            if j == 0 or j == len(trapPoints)-1:
                final.append(f(trapPoints[j])*0.5)
            else:    
                final.append(f(trapPoints[j]))
        print(trapPoints, sum(final)*deltax)

ni(2,18,8,"trapezoid",myf)
