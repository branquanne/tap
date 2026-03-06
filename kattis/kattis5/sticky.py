n = int(input())

stickLengths = list(map(int, input().split()))
stickLengths.sort()

isPossible = False

for x in range(n-2):
    if stickLengths[x] + stickLengths[x +1] > stickLengths[x + 2] and stickLengths[x] + stickLengths[x +2] > stickLengths[x + 1] and stickLengths[x + 2] + stickLengths[x +1] > stickLengths[x]:
        isPossible = True
        break

if isPossible:
    print("possible")
else:
    print("impossible")