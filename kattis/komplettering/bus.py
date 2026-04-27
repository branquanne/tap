import sys
from bisect import bisect_left

data = list(map(int, sys.stdin.read().split()))
a, b, d, n = data[:4]
times = data[4 : 4 + n]

dp = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    next_i = bisect_left(times, times[i] + d)
dp[i] = min(a + dp[i + 1], b + dp[next_i])

print(dp[0])
