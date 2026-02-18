"""
This program solves the Traveling Sales Problem (TSP) by implementing the nearest pair insertion heuristic.

Given a 2D space filled with N points, the algorithm starts with one point in the tour and repeatedly finds
the nearest pair between:
- a point already in the current tour, and
- a point not yet visited.

The unvisited point is then inserted directly after the matched visited point in the tour.

To run this file with diagnostics (requires diagnostic file - tsp): python3 /path/to/rbonp.py < /path/to/yourinfile | /path/to/tsp
To run this file without diagnostics: python3 /path/to/rbonp.py < /path/to/yourinfile

Author: Bran Mjöberg Quanne - dv24bme
"""

import sys
from math import sqrt


# Main function delegates tasks
def main():
    n = None
    points = read_input(n)

    # Start at first point and mark the rest as unvisited
    visited = [0]
    unvisited = set(range(1, len(points)))

    # Repeatedly insert the nearest unvisited point next to its nearest visited point
    while unvisited:
        v_indx, uv_indx = find_nearest_pair(unvisited, visited, points)

        insert_pos = visited.index(v_indx) + 1
        visited.insert(insert_pos, uv_indx)
        unvisited.remove(uv_indx)

    # Print the result
    print(n)
    for point in visited:
        x, y = points[point]
        print(f"{x} {y}")


# Read the standard input and store the values
def read_input(n):
    points = []

    # For every input line
    for line in sys.stdin:
        line.strip()

        # Ignore lines that start with '#' and empty lines
        if line.startswith("#") or not line:
            continue

        # First valid line is the number of following lines
        if n == None:
            n = int(line)
        else:
            # Map the points according to the format 'X Y'
            x, y = map(int, line.split())
            points.append((x, y))

    return points


# Calculate distance between points using Euclidean distance
def find_distance(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


# Find the nearest pair between visited and unvisited points
def find_nearest_pair(unvisited, visited, points):
    min_dist = float("inf")
    best_v_indx = None
    best_uv_indx = None

    # Compare every visited point with every unvisited point
    for v_indx in visited:
        for uv_indx in unvisited:
            dist = find_distance(points[v_indx], points[uv_indx])
            if dist < min_dist:
                min_dist = dist
                best_v_indx = v_indx
                best_uv_indx = uv_indx

    return best_v_indx, best_uv_indx


# Entry point for program
if __name__ == "__main__":
    main()
