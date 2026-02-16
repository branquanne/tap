# Solve the robot tour optimisation problem using the nearest pair heuristic.
import sys
from math import sqrt


def main():
    n = None
    points = read_input(n)

    visited = [0]
    unvisited = set(range(1, len(points)))

    while unvisited:
        v_indx, uv_indx, dist = find_nearest_pair(unvisited, visited, points)

        insert_pos = visited.index(v_indx) + 1
        visited.insert(insert_pos, uv_indx)
        unvisited.remove(uv_indx)

    for point in visited:
        x, y = points[point]
        print(f"{x} {y}")


def read_input(n):
    points = []

    for line in sys.stdin:
        line.strip()
        if line.startswith("#") or not line:
            continue
        if n == None:
            n = int(line)
        else:
            x, y = map(int, line.split())
            points.append((x, y))

    return points


def find_distance(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def find_nearest_pair(unvisited, visited, points):
    min_dist = float("inf")
    best_v_indx = None
    best_uv_indx = None

    for v_indx in visited:
        for uv_indx in unvisited:
            dist = find_distance(points[v_indx], points[uv_indx])
            if dist < min_dist:
                min_dist = dist
                best_v_indx = v_indx
                best_uv_indx = uv_indx

    return best_v_indx, best_uv_indx, min_dist


if __name__ == "__main__":
    main()
