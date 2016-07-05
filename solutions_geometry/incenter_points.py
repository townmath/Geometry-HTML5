# takes in three points of a html5 canvas triangle and gives two points to
#connect to make the incenter
import numpy
TrianglePoints = [(20,20),(200,50),(75,100)]
maxnum=30
linelist=[]
sidelist=[]

# throw away
def findslope ((xone,yone),(xtwo,ytwo)):
    return ((float(ytwo-yone)/float(xtwo-xone)))

def findyint (slope,(x,y)):
    return (-slope*x+y)

def finddxanddy (slope,maxnum):
    dx = maxnum/((slope**2+1)**.5)
    dy = dx*slope
    return(dx,dy)

def findmidpoint ((xone,yone),(xtwo,ytwo)):
    return ((xtwo+xone)/2,(ytwo+yone)/2)

def findintersection ((m1,b1),(m2,b2)):
    a = numpy.array([[-m1,1],[-m2,1]])
    b = numpy.array([b1,b2])
    return(numpy.linalg.solve(a,b))

def addpoints((xone,yone),(xtwo,ytwo)):
    return(xone+xtwo,yone+ytwo)

def finddistance ((xone,yone),(xtwo,ytwo)):
    return ((float(xtwo-xone)**2+float(ytwo-yone)**2)**.5)

for point in range (0,2):
    slope1 = findslope(TrianglePoints[point],TrianglePoints[point+1])
    if point==0:
        thirdpoint=2
    else:
        thirdpoint=point-1
    slope2 = findslope(TrianglePoints[point],TrianglePoints[thirdpoint])
    dpoint1=finddxanddy(slope1,maxnum)
    realpoint1 = addpoints(dpoint1,TrianglePoints[point])
    dpoint2=finddxanddy(slope2,maxnum)
    realpoint2 = addpoints(dpoint2,TrianglePoints[point])
    midpoint = findmidpoint(realpoint1,realpoint2)
    slopeline=findslope(midpoint,TrianglePoints[point])
    yint=findyint(slopeline,midpoint)
    linelist.append((slopeline,yint))
#    print(slopeline,yint)
circleorigin = findintersection(linelist[0],linelist[1])
#or you could throw away everything above and use the formulas from wikipedia
for points in range(0,3):
    if points<2:
        sidelist.append(finddistance(TrianglePoints[points],TrianglePoints[points+1]))
    else:
        sidelist.append(finddistance(TrianglePoints[points],TrianglePoints[0]))
#print sidelist
p = sum(sidelist) #perimeter
s = p/2 #semiperimeter
circleradius = (((s-sidelist[0])*(s-sidelist[1])*(s-sidelist[2]))/s)**.5
print circleorigin, circleradius
xcoord=(sidelist[0]*TrianglePoints[2][0]+sidelist[1]*TrianglePoints[0][0]+sidelist[2]*TrianglePoints[1][0])/p
ycoord=(sidelist[0]*TrianglePoints[2][1]+sidelist[1]*TrianglePoints[0][1]+sidelist[2]*TrianglePoints[1][1])/p
print (xcoord, ycoord)
