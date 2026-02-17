# Solve the robot tour optimisation problem using the nearest neighbour using 2-opt.
import sys
from math import hypot


def read_input():
    points = []
    n = None

    for line in sys.stdin:
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if n is None:
            n = int(s)
        else:
            x, y = map(int, s.split())
            points.append((x, y))

    return n, points


def find_dist(a, b):
    return hypot(a[0] - b[0], a[1] - b[1])


def nearest_neighbour(points):
    n = len(points)
    if n == 0:
        return []

    unvisited = set(range(1, n))
    tour = [0]
    curr = 0

    while unvisited:
        next = min(unvisited, key=lambda i: find_dist(points[curr], points[i]))
        tour.append(next)
        unvisited.remove(next)
        curr = next

    return tour


def two_opt(order, points):
    n = len(order)
    if n <= 2:
        return order

    best = order[:]
    best_len = tour_length(best, points)
    improved = True
    while improved:
        improved = False
        for i in range(1, n - 2):
            for j in range(i + 1, n - 1):
                new_order = best[:i] + best[i : j + 1][::-1] + best[j + 1 :]
                new_len = tour_length(new_order, points)
                if new_len < best_len:
                    best, best_len = new_order, new_len
                    improved = True
                    break
            if improved:
                break

    return best


def tour_length(order, points):
    total = 0.0
    for i in range(len(order) - 1):
        total += find_dist(points[order[i]], points[order[i + 1]])
    total += find_dist(points[order[-1]], points[order[0]])
    return total


def main():
    n, points = read_input()
    if not points:
        return

    tour = nearest_neighbour(points)
    tour = two_opt(tour, points)

    print(len(points))
    for i in tour:
        x, y = points[i]
        print(f"{x} {y}")


if __name__ == "__main__":
    main()
