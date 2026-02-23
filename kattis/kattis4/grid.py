import sys
from collections import deque


def bfs():
    X, Y = map(int, sys.stdin.readline().split())
    grid = []

    for _ in range(X):
        line = sys.stdin.readline()
        grid.append(line)

    queue = deque([(0, 0, 0)])

    visited = set()
    visited.add((0, 0))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y, moves = queue.popleft()

        if x == X - 1 and y == Y - 1:
            print(moves)
            return
        jump = int(grid[x][y])

        if jump == 0:
            continue

        for dx, dy in directions:
            new_x = x + (dx * jump)
            new_y = y + (dy * jump)
            if 0 <= new_x < X and 0 <= new_y < Y:
                if (new_x, new_y) not in visited:
                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y, moves + 1))

    print(-1)


if __name__ == "__main__":
    bfs()
