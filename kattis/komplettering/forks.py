import sys

n = int(sys.stdin.readline())
counts = list(map(int, sys.stdin.readline().split()))

smallest = min(counts)
counts.remove(smallest)
second_smallest = min(counts)

print(smallest + second_smallest)
