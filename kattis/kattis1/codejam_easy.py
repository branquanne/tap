def get_input():
    n = int(input())
    lines = []
    for _ in range(n):
        lines.append(input().strip())

    return lines


def check_jams(line):
    target = "welcome to code jam"
    m = len(target)
    dp = [0] * (m + 1)
    dp[0] = 1

    for char in line:
        for j in range(m - 1, -1, -1):
            if char == target[j]:
                dp[j + 1] = (dp[j + 1] + dp[j]) % 10000

    return dp[m]


def main():
    lines = get_input()

    for case, line in enumerate(lines, start=1):
        ans = check_jams(line)
        print(f"Case #{case}: {ans:04d}")


if __name__ == "__main__":
    main()
