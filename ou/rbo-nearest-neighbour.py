# Create and sovle the robot tour optimisation problem using the nearest neighbour heuristic.
import sys
from math import sqrt


def find_distance(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def find_nearest_neighbour(unvisited_neighbours, current_pos):
    min_distance = float("inf")
    nearest = None

    for point in unvisited_neighbours:
        dist = find_distance(current_pos, point)
        if dist < min_distance:
            min_distance = dist
            nearest = point

    return nearest


def read_input(n):
    points = []

    for line in sys.stdin:
        line.strip()
        if line.startswith("#") or not line:
            continue
        if n is None:
            n = int(line)
        else:
            x, y = map(int, line.split())
            points.append((x, y))

    return points


def main():
    n = None
    points = read_input(n)

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
        x, y = points[point]
        print(f"{x} {y}")


if __name__ == "__main__":
    main()
