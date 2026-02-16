islands, bridges = map(int, input().split())

conquered = []
armySize = 0

adjacent = [[] for _ in range(islands + 1)]

for _ in range(bridges):
    a, b = map(int, input().split())
    adjacent[a].append(b)
    adjacent[b].append(a)

armies = [0]
for _ in range(islands):
    armies.append(int(input()))

conquered = set([1])
armySize = armies[1]

changed = True
while changed:
    changed = False
    for island in list(conquered):
        for neighbor in adjacent[island]:
            if neighbor not in conquered and armies[neighbor] < armySize:
                conquered.add(neighbor)
                armySize += armies[neighbor]
                changed = True

print(armySize)
