import math

def get_factors(n):
    if n < 4:
        return None
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return f"{i}x{n//i}"
    return None

def solve(n):
    r1 = get_factors(n)
    if r1:
        return r1

    for i in range(4, (n // 2) +1):
        r2 = get_factors(i)
        r3 = get_factors(n - i)
        if r2 and r3:
            return f"{r2} {r3}"

    for i in range(4, n-8):
        r4 = get_factors(i)
        if not r4:
            continue
        for j in range(4, n - i- 3):
            r5 = get_factors(j)
            r6 = get_factors(n -i -j)
            if r5 and r6:
                return f"{r4} {r5} {r6}"

    return "impossible"

def main():
    n = int(input().strip())
    print(solve(n))
    pass


if __name__ == "__main__":
    main()