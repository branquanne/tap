# Create and sovle the robot tour optimisation problem using the nearest neighbour heuristic.
from math import sqrt
import sys


def distance(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def find_nearest_neighbour(unvisited_neighbours, current_pos):
    min_distance = float('inf')
    nearest = None

    for point in unvisited_neighbours:
        dist = distance(current_pos, point)
        if dist < min_distance:
            min_distance = dist
            nearest = point

    return nearest


def main():
    temp = []
    for line in sys.stdin:
        line = line.strip()
        if line and not line.startswith("#"):
            temp.append(line)
            
    n = int(temp[0])
    points = []
    for i in range(1, n + 1):
        x, y = map(int, temp[i].split())
        points.append((x, y))
    
    visited = [points[0]]
    unvisited = set(points[1:])
    current_pos = points[0]

    while unvisited:
        nearest = find_nearest_neighbour(unvisited, current_pos)
        visited.append(nearest)
        unvisited.remove(nearest)
        current_pos = nearest
        
    print(n)
    for point in visited:
        print(f"{point[0]} {point[1]}")
    

if __name__ == "__main__":
    main()
