# takes in three points of a html5 canvas triangle and gives two points to
#connect to make the circumcenter and the radius
import numpy
TrianglePoints = [(20,120),(200,150),(75,200)]
maxnum=30
linelist=[]
sidelist=[]

def findslope ((xone,yone),(xtwo,ytwo)):
    return ((float(ytwo-yone)/float(xtwo-xone)))

def findyint (slope,(x,y)):
    return (-slope*x+y)

def finddxanddy (slope,maxnum):
    dx = maxnum/((slope**2+1)**.5)
    dy = dx*slope
    return(dx,dy)

def findmidpoint ((xone,yone),(xtwo,ytwo)):
    return (float(xtwo+xone)/2,float(ytwo+yone)/2)

def findintersection ((m1,b1),(m2,b2)):
    a = numpy.array([[-m1,1],[-m2,1]])
    b = numpy.array([b1,b2])
    return(numpy.linalg.solve(a,b))

def addpoints((xone,yone),(xtwo,ytwo)):
    return(xone+xtwo,yone+ytwo)

def finddistance ((xone,yone),(xtwo,ytwo)):
    return ((float(xtwo-xone)**2+float(ytwo-yone)**2)**.5)

slope1 = findslope(TrianglePoints[0],TrianglePoints[1])
slope1 = -1/slope1 #inverse reciprocal = perpendicular
midpoint1 = findmidpoint(TrianglePoints[0],TrianglePoints[1])
yint1 = findyint(slope1,midpoint1)
slope2 = findslope(TrianglePoints[1],TrianglePoints[2])
slope2 = -1/slope2 
midpoint2 = findmidpoint(TrianglePoints[1],TrianglePoints[2])    
yint2 = findyint(slope2,midpoint2)
print midpoint1, midpoint2, (slope1,yint1),(slope2,yint2)
circleorigin = findintersection((slope1,yint1),(slope2,yint2))

for points in range(0,3):
    if points<2:
        sidelist.append(finddistance(TrianglePoints[points],TrianglePoints[points+1]))
    else:
        sidelist.append(finddistance(TrianglePoints[points],TrianglePoints[0]))
#print sidelist
p = sum(sidelist) #perimeter
s = p/2 #semiperimeter
a=sidelist[0]
b=sidelist[1]
c=sidelist[2]
circleradius = (a*b*c)/(4*(s*(s-a)*(s-b)*(s-c))**.5)
print circleorigin, circleradius

