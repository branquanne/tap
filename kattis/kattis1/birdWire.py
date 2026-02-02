wireLength, distanceBetweenBirds, birds = map(int, input().split())

positions = []
for _ in range(birds):
    positions.append(int(input()))

positions.sort()

additionalBirds = 0

if positions:
    gap = positions[0] - 6
    additionalBirds += max(0, gap // distanceBetweenBirds)

    for i in range(len(positions) - 1):
        gap = positions[i + 1] - positions[i] - distanceBetweenBirds
        if gap > 0:
            additionalBirds += max(0, gap // distanceBetweenBirds)

    gap = wireLength - 6 - positions[-1]
    additionalBirds += max(0, gap // distanceBetweenBirds)
else:
    if wireLength > 11:
        gap = wireLength - 12
        additionalBirds += max(0, gap // distanceBetweenBirds + 1)

print(additionalBirds)
