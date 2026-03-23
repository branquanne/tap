def get_input():
    num_ads, cost_per_ad = map(int, input().split())

    arr = list(map(int, input().split()))

    return arr, num_ads, cost_per_ad


def main():
    arr, num_ads, cost_per_ad = get_input()

    res = solve(arr, num_ads, cost_per_ad)

    print(res)


def solve(arr, num_ads, cost_per_ad):
    res = arr[0]
    maxEnd = arr[0]

    for i in range(1, num_ads):
        temp = arr[i] - cost_per_ad

        maxEnd = max(maxEnd + temp, temp)

        res = max(res, maxEnd)

    return res


if __name__ == "__main__":
    main()
