from decimal import Decimal, ROUND_HALF_UP
import sys

HUNDRED = Decimal("100")
CENT = Decimal("0.01")

def round_cent_up(x: Decimal) -> Decimal:
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def minimum_months(t):
    r, b, m = t
    months = 0

    while b > 0 and months < 1200:
        rate = round_cent_up((r / HUNDRED) * b)

        new_balance = b + rate - m
        months += 1

        if new_balance >= b:
            return "impossible"

        b = new_balance

    if b>0:
        return "impossible"
    return months


def main():
    n = int(input())

    lines = []

    for _ in range(n):
        line = list(map(Decimal, input().split()))
        lines.append(line)

    for line in lines:
        print(minimum_months(tuple(line)))


if __name__ == "__main__":
    main()