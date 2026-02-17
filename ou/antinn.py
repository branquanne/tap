# We choose N = 100 because of exr2.in


def output_points(points):
    print(len(points))
    for x, y in points:
        print(f"{x} {y}")


def generate_anti_nn():
    n = 100
    points = []

    cluster_spacing = 2000
    tail_spacing = 500
    n_cluster = max(4, int(n * 0.2))

    for i in range(n_cluster):
        x = 0
        y = (i + 1) * cluster_spacing
        points.append((x, y))

    n_tail = n - n_cluster
    points.append((0, 0))

    for i in range(1, n_tail):
        x = i * tail_spacing
        y = 0
        points.append((x, y))

    points.sort(key=lambda p: (p[0] ** 2 + p[1] ** 2))
    return points


def main():
    points = generate_anti_nn()
    output_points(points)


if __name__ == "__main__":
    main()
