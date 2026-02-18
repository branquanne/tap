"""
This program solves the Traveling Sales Problem (TSP) by implementing the nearest neighbour algorithm with 2-opt.
By using 2-opt we effectively try to mirror the current best solution at any given position and test
if the mirrored solution is better than the current nearest neighbour-solution.

Given a 2D space filled with N points, the algorithm firstly searches for a tour using the nearest neighbour heuristic.
The improvement in this algorithm comes from the 2-opt segment. This part checks different segments of the already solved tour
and tries to reverse them inorder to increase efficiency.

To run this file with diagnostics (requires diagnostic file - tsp): python3 /path/to/rboto.py < /path/to/yourinfile | /path/to/tsp
To run this file without diagnosticts: python3 /path/to/rboto.py < /path/to/yourinfile

Author: Bran Mjöberg Quanne - dv24bme
"""

import sys
from math import hypot


# Read the standard input and store the values
def read_input():
    points = []
    n = None

    # For every input line
    for line in sys.stdin:
        s = line.strip()

        # Ignore lines that start with '#' and empty lines
        if not s or s.startswith("#"):
            continue
        # First valid line is the number of following lines
        if n is None:
            n = int(s)

        # Map the points according to the format 'X Y'
        else:
            x, y = map(int, s.split())
            points.append((x, y))

    return n, points


# Calculate distance between points using Euclidean distance
def find_dist(a, b):
    return hypot(a[0] - b[0], a[1] - b[1])


# Find a solution using nearest neighbour heuristic
def nearest_neighbour(points):
    n = len(points)
    if n == 0:
        return []

    # Start at first point and mark the rest unvisited
    unvisited = set(range(1, n))
    tour = [0]
    curr = 0

    # For every unvisited point, get the nearest neighbour and set it as visited -> jump to next point
    while unvisited:
        next = min(unvisited, key=lambda i: find_dist(points[curr], points[i]))
        tour.append(next)
        unvisited.remove(next)
        curr = next

    return tour


# 2-opt function that tries reversal of segments in the tour
def two_opt(order, points):
    n = len(order)
    if n <= 2:
        return order

    best = order[:]
    best_len = tour_length(best, points)
    improved = True

    # Continuous search for improvement
    while improved:
        improved = False

        # Try reversing segments [i -> j]
        for i in range(1, n - 2):
            for j in range(i + 1, n - 1):
                new_order = best[:i] + best[i : j + 1][::-1] + best[j + 1 :]
                new_len = tour_length(new_order, points)

                # If we got an improvement then start over again
                if new_len < best_len:
                    best, best_len = new_order, new_len
                    improved = True
                    break
            if improved:
                break

    return best


# Computes the total tour length using Euclidean distance
def tour_length(order, points):
    total = 0.0
    for i in range(len(order) - 1):
        total += find_dist(points[order[i]], points[order[i + 1]])
    total += find_dist(points[order[-1]], points[order[0]])
    return total


# Main function delegates tasks
def main():
    n, points = read_input()
    if not points:
        return

    # Firstly, use nearest neighbour. Secondly, refine using 2-opt
    tour = nearest_neighbour(points)
    tour = two_opt(tour, points)

    # Print the result
    print(n)
    for i in tour:
        x, y = points[i]
        print(f"{x} {y}")


# Entry point for program
if __name__ == "__main__":
    main()
