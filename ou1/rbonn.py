"""
This program solves the Traveling Sales Problem (TSP) by implementing the nearest neighbour algorithm.

Given a 2D space filled with N points, the algorithm searches for a tour by always selecting
the closest unvisited point from the current position.

To run this file with diagnostics (requires diagnostic file - tsp): python3 /path/to/rbonn.py < /path/to/yourinfile | /path/to/tsp
To run this file without diagnosticts: python3 /path/to/rbonn.py < /path/to/yourinfile

Author: Bran Mjöberg Quanne - dv24bme
"""

import sys
from math import sqrt, hypot


# Calculate distance between points using Euclidean distance
def find_distance(a, b):
    return hypot(a[0] - b[0], a[1] - b[1])


# Find a solution using nearest neighbour heuristic
def find_nearest_neighbour(unvisited_neighbours, current_pos):
    min_distance = float("inf")
    nearest = None

    # For every unvisited point, compare distance and keep the smallest one
    for point in unvisited_neighbours:
        dist = find_distance(current_pos, point)
        if dist < min_distance:
            min_distance = dist
            nearest = point

    return nearest


# Read the standard input and store the values
def read_input():
    points = []
    n = None

    # For every input line
    for line in sys.stdin:
        line = line.strip()

        # Ignore lines that start with '#' and empty lines
        if line.startswith("#") or not line:
            continue

        # First valid line is the number of following lines
        if n is None:
            n = int(line)

        # Map the points according to the format 'X Y'
        else:
            x, y = map(int, line.split())
            points.append((x, y))

    return n, points


# Main function delegates tasks
def main():
    n, points = read_input()

    # If no points were provided, print 0 and stop
    if not points:
        print(0)
        return

    # Start at first point and mark the rest as unvisited
    visited = [points[0]]
    unvisited = set(points[1:])
    current_pos = points[0]

    # Repeatedly visit the nearest unvisited point
    while unvisited:
        nearest = find_nearest_neighbour(unvisited, current_pos)
        visited.append(nearest)
        unvisited.remove(nearest)
        current_pos = nearest

    # Print the result
    print(n)
    for x, y in visited:
        print(f"{x} {y}")


# Entry point for program
if __name__ == "__main__":
    main()
