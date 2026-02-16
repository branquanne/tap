k = int(input().strip())
myN = input().strip()
friendN = input().strip()

numSame = 0
numDiff = 0

n = len(myN)

for i in range(n):
    if myN[i] == friendN[i]:
        numSame += 1
    else:
        numDiff += 1

result = min(numSame, k) + min(numDiff, n - k)
print(result)
