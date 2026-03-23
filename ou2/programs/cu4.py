# A program that approximates a solution to the travelling salesman problem with
# an ellipse-inspired heuristic. This will require some linear algebra, but it will be
# documented in such a way that it's hopefully easy to follow.
#
# Explaination of heuristic (The ellipse name comes from keeping track of the distance to 2 points, similar to the 2 focii of an ellipse):
# 1. We find the furthest pair of points. If we see their distance as a diagonal of a square all points must be inside this square,
# but most distributions likely fall within an ellipse. We then rotate all points using a rotation matrix (explained later)
# in order to end up with the following:
# ^              .           .
# |      .   .       .          .
# |  A--------------------------------B
# |       .   .        .         .
# |          .     .        .            
# ------------------------------------------>
#   Example visualisation of data oriented s.t the x-axis is parallell with the line between the two points.
# ^      .
# |    .    .  
# |  A   .   B
# |   .    .       
# |     .         
# -------------->
#   Example of extreme non-eliptic case
#
# 2. We use the fact that we have rotated all points so that they fit into the coordinate system above in order to 
# easily split them into the topside points and botside points by positive/negative y-coordinate. The idea is to walk
# along the topside to B and then back to A through the botside. 
#
# 3. Having made the rotation of all points we simply choose the topside points in increasing order of x-coordinate
# followed by the botside points in decreasing order of x-coordinate.
#
# ^            /-..\       /-.-\
# |   /--.---./     \.----/     \.----\
# |  A                                 B
# |   \---.   .        .-\       .----/
# |        \-./\---.--/   \.----/            
# ------------------------------------------>
#   Illustration of the solution generated for the first problem
#
# Run the program using python .\TSPEllipseHeuristic.py < inputFile
# Input: A file of input data formated as
# n     // The number of nodes
# x1 y1 // The coordinates of the first node
# x2 y2 // The coordinates of the second node
# .  .
# .  .
# .  .
# xn yn // The final set of coordinates.
# 
# Outputs the path chosen and it's total distance.

import sys
import math

def main():
    # Reads input
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            inp=f.readlines()
    else:
        inp=sys.stdin.readlines()

    # Removes comment rows at the start
    k = 0
    while(inp[k][0] == '#'):
        k += 1

    # Reads all the nodes
    numNodes = int(inp[k])
    nodes = []

    for i in range(numNodes):
        newNode = inp[i+k+1].strip().split(" ")
        x = float(newNode[0])
        y = float(newNode[1])
        nodes.append((x, y, i))
    
    longestEdge = (0, 0, 0)
    # Find the longest edge. This step is the most time consuming.
    for i in range(numNodes):   # Iterate over all nodes
        for j in range(i, numNodes): # Iterate over all nodes with higher index than i (Thus only takes i->j but not j->i avoiding doubles)
            if euclidDist(nodes[i], nodes[j]) > longestEdge[2]:
                longestEdge = (i, j, euclidDist(nodes[i], nodes[j]))
                
    # By now we have the longest edge. We find the points in the coordinate system have a vector between them:
    # ^                  B
    # |            /---/
    # |       /---/
    # |  /---/
    # | A
    # |---------------------------->            
    #   Illustration of a straight line from A to B in the xy plane. 
    
    A = nodes[longestEdge[0]]
    B = nodes[longestEdge[1]]
    dist = (A[0] - B[0], A[1] - B[1])

    # Now we want to find the rotation matrix which makes this vector into the x-axis
    # What is neat is that Euclidean distance is preserved under 
    # rotation of the coordinate system. I.e if r(a) is where the rotation places a then:
    # dist(a, b) = dist(r(a), r(b)). 
    #
    # Rotation matrices are of the form,    a and b are:
    #       --------------                  ----     ----              -------
    # R =   |cos v -sin v|              a = |x1| b = |x2| dist = a-b = |xDist|
    #       |sin v  cos v|                  |y1|     |y2|              |yDist|
    #       --------------                  ----     ----              -------
    #
    # We want the y-distance to equal 0. 
    # I.e we want to solve Ra-Rb = R(a-b) = Rdist= [x, 0]
    # Thus we want to find v such that sin v*xDist + cos v*yDist = 0 
    # 
    # We will solve this using the bisection algorithm. At v = 0 we have done nothing (cos 0 = 1, sin 0 = 0 gives R = I)
    # We increase v gradually until we find a value for yDist with opposite sign. Then we test values in the middle for which sign they have 
    # until we converge to a v that gives yDist ~ 0. 
    #
    #
    initialSign = sign(yDist(dist, 0))
    x = 0 # This is roughly 6 degrees. 
    residual = yDist(dist, x)
    while initialSign == sign(residual) and abs(residual) > 0.001:
        residual = yDist(dist, x)
        x += 0.1

    delta = 0.001 # We are satisfied with an angle within 0.001 of the real one.
    epsilon = 0.001* dist[1] # We want a yDist at most 1/1000 of the prior one. 

    start = 0
    end = x
    center = (start + end)/ 2
    residual = yDist(dist, center)
    while abs(start-end) > delta and residual > epsilon:
        center = (start + end)/ 2
        
        residual = yDist(dist, center)
        if sign(residual) == initialSign: # True x is in the right bracket.
            start = center
        else:
            end = center
    
    # By now center should be an angle that creates pretty much the transformation we want. We apply it to all points.
    # As a neat consequence in this new world we're creating we no longer need to keep track of A and B as they will be the points with
    # The lowest and highest x values respectively (otherwise two points would be further away)        

    rotationAngle = center
    print("#Angle of rotation (in radians): ", end="")
    print(rotationAngle)
    rotatedNodes = []
    for node in nodes:
        rotatedNodes.append(rotate(node, rotationAngle))
        
    # We can now proceed to step 2 of the algorithm. 
    topSide = []
    botSide = []
    for node in rotatedNodes:
        # If y is positive
        if node[1] > 0:
            topSide.append(node)
        else:
            botSide.append(node)
           
    # Sorts the two arrays        
    topSide.sort(key = tupleVal1)
    botSide.sort(key = tupleVal1, reverse=True)
        
    # Step 3: Creating the path
    path = []
    for node in topSide:
        path.append(node)
    for node in botSide:
        path.append(node)
        
    #print(path)

    # Calculating total distance and printing path
    totDist = 0
    #print(path)
    print("#Path: ")
    print("#", end = "")
    for i in range(len(path)-1):
        prev = path[i]
        new = path[i+1]
        totDist += euclidDist(prev, new)
        print(prev[2], end="  ")
    print(path[-1][2])
    # Adds returning to home node
    totDist += euclidDist(path[0], path[-1])
    
    # Print total distance
    print("#Total distance: " + str(totDist))
    print(numNodes)
    for node in path:
        print(str(int(nodes[node[2]][0])), end=" ")
        print(str(int(nodes[node[2]][1])))

# Calculates the Euclidean distance between 2 points a, b
def euclidDist(a, b):
    ax = a[0]
    ay = a[1]
    bx = b[0]
    by = b[1]
    xDist = ax-bx
    yDist = ay-by
    # Squaring means we need no absolute value, negative xDist, yDist are allowed.
    return math.sqrt(xDist*xDist + yDist*yDist)

# Grabs the first value out of a tuple
def tupleVal1(a):
    return a[0]

# Grabs the second value out of a tuple
def tupleVal2(a):
    return a[1]

# Finds the sign of a value x
def sign(x):
    if x >= 0:
        return 1
    if x < 0:
        return -1
    
# Finds yDist
def yDist(dist, v):
    return math.sin(v)*dist[0]+math.cos(v)*dist[1]

# Applying rotation matrix
def rotate(a, v):
    newX = math.cos(v)*a[0]-math.sin(v)*a[1]
    newY = math.sin(v)*a[0]+math.cos(v)*a[1]
    return (newX, newY, a[2])
    
main()