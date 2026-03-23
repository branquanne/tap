import sys
import math

'''
Nearest neighbour algorithm for TSP problem, with starting point as farthest from centroid
and tie breaker for equal distances

Reads coordinates from input file given as first argument
Outputs the order of visited coordinates and distance statistics

Improves upon the basic nearest neighbour algorithm by starting from the coordinate farthest from the centroid
of all coordinates, and implementing a tie breaker when multiple unvisited coordinates are at the same nearest distance.
Tie breaker chooses the coordinate whose nearest unvisited neighbour is closer.

Example input:
# Small TSP graph test
5
-1 5
2 100
100 2
50 50
19 5

Example output:
# Input file distance: 377.60
# Total distance: 383.59
# Distance saved: -6.00
# 101.59% of the original
5
2 100
50 50
19 5
-1 5
100 2

Usage:
python3 03_my_algorithm.py ex1.in
'''

input = []
# stdin or first argument
input_file = sys.stdin
if len(sys.argv) > 1:
    input_file = open(sys.argv[1], 'r')

with input_file:
    # ignore comments in input file
    input = [x.strip() for x in input_file.readlines() if not (x.startswith("#"))]
    

number_of_coords = int(input[0])
coords = []

# make coordinates into list of tuples, starting from line 2
# we skip first coordinate since we will start from there
for i in range(1, number_of_coords + 1):
    x, y = map(int, input[i].split(" "))
    coords.append((x, y))

# Gets the point which is the centroid of the coordinates.
def calculate_centroid(coords):
    x_sum = 0
    y_sum = 0
    for coord in coords:
        x_sum += coord[0]
        y_sum += coord[1]
    return (x_sum / len(coords), y_sum / len(coords))

# Gets the point which is farthest from a specified point (in this case the centroid).
def get_farthest_from_centroid(coords, centroid):
    farthest_coord = None
    max_distance = -1
    for coord in coords:
        distance = math.dist(coord, centroid)
        if distance > max_distance:
            max_distance = distance
            farthest_coord = coord
    return farthest_coord

# nearest neighbour algorithm for TSP problem, with starting point as farthest from centroid, and tie breaker for equal distances
def algo(coords):
    unvisited = set(coords)
    visited_order = []

    centroid = calculate_centroid(coords)
    # set starting coord as farthest from centroid
    current_cord = get_farthest_from_centroid(coords, centroid)
    unvisited.remove(current_cord)
    visited_order.append(current_cord)

    # nearest neighbour algorithm (starting from farthest from centroid, and tie breaker for equal distances)
    while(unvisited):
            nearest_cord = None
            nearest_distance = math.inf
                
            # for every unvisited coord, find nearest
            for cord in unvisited:
                distance = math.dist(current_cord, cord)
                # check if nearest
                if distance < nearest_distance:
                    nearest_distance = distance
                    nearest_cord = cord
                elif distance == nearest_distance:
                    #tie breaker, choose the one with the shorter distance to closest unvisited
                    next_nearest_current = min((math.dist(nearest_cord, next_cord) for next_cord in unvisited
                                                if next_cord != nearest_cord and next_cord != cord),
                                               default=math.inf)
                    next_nearest_candidate = min((math.dist(cord, next_cord) for next_cord in unvisited
                                                 if next_cord != nearest_cord and next_cord != cord),
                                                default=math.inf)
                    # if the candidate's nearest unvisited neighbour is closer than the current nearest's nearest unvisited neighbour, choose the candidate
                    if next_nearest_candidate < next_nearest_current:
                        nearest_cord = cord

            # mark nearest as visited
            visited_order.append(nearest_cord)
            unvisited.remove(nearest_cord)
            current_cord = nearest_cord
    return visited_order

# calculates the total distance of the tour given by visited_order, including returning to the start
def calculate_total_distance(visited_order):
    total_distance = 0
    last_cord = None
    start_cord = None
    for cord in visited_order:
        if last_cord:
            total_distance += math.dist(last_cord, cord)
        last_cord = cord
        if not start_cord:
            start_cord = cord
    # return to start
    total_distance += math.dist(last_cord, start_cord)
    
    return total_distance

visited_order = algo(coords)
input_distance = calculate_total_distance(coords)
visited_distance = calculate_total_distance(visited_order)

print(f"# Input file distance: {input_distance:.2f}")
print(f"# Total distance: {visited_distance:.2f}")
print(f"# Distance saved: {input_distance - visited_distance:.2f}")
print(f"# {(visited_distance) / input_distance * 100:.2f}% of the original")

print(f"{number_of_coords}")
# print visited order
for cord in visited_order:
    print(f"{cord[0]} {cord[1]}")
