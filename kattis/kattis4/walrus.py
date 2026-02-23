import sys

n = int(sys.stdin.readline().strip())

plates = []

for line in sys.stdin:
    plates.append(int(line.strip()))


can_be = [False] * (2000 + 1)
can_be[0] = True

for plate in plates:
    for i in range(2000, plate - 1, -1):
        if can_be[i - plate]:
            can_be[i] = True

best_over = None
for i in range(1000, 2001):
    if can_be[i]:
        best_over = i
        break

best_under = None
for i in range(1000, -1, -1):
    if can_be[i] == True:
        best_under = i
        break


if best_over is None:
    print(best_under)
elif best_under is None:
    print(best_over)
elif best_over - 1000 <= 1000 - best_under:
    print(best_over)
else:
    print(best_under)
