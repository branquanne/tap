"""
This program generates a point set designed to perform poorly for the nearest neighbour heuristic.

Given a fixed number of points (N = 100), the algorithm creates:
- a vertical cluster of points far from the origin, and
- a long horizontal tail of points from the origin.

The points are then sorted by distance to the origin before being printed.

To run this file: python3 /path/to/antinn.py

Author: Bran Mjöberg Quanne - dv24bme
"""


# Print points in the expected format:
# first line is N, followed by N lines "x y"
def output_points(points):
    print(len(points))
    for x, y in points:
        print(f"{x} {y}")


# Generate an input instance that is supposedly challenging for nearest neighbour
def generate_anti_nn():
    n = 100
    points = []

    # Spacing controls how far apart generated structures are
    cluster_spacing = 2000
    tail_spacing = 500

    # Use 20% of points for the vertical cluster
    n_cluster = max(4, int(n * 0.2))

    # Build a vertical cluster at x = 0
    for i in range(n_cluster):
        x = 0
        y = (i + 1) * cluster_spacing
        points.append((x, y))

    # Build a horizontal tail starting from the origin
    n_tail = n - n_cluster
    points.append((0, 0))

    for i in range(1, n_tail):
        x = i * tail_spacing
        y = 0
        points.append((x, y))

    # Sort by squared distance to origin
    points.sort(key=lambda p: (p[0] ** 2 + p[1] ** 2))
    return points


# Main function delegates tasks
def main():
    points = generate_anti_nn()
    output_points(points)


# Entry point for program
if __name__ == "__main__":
    main()
