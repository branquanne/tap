n = int(input())

nums = []
for _ in range(n):
    nums.append(int(input().strip()))

coords = {
    '1': (0, 0), '2': (0, 1), '3': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '7': (2, 0), '8': (2, 1), '9': (2, 2),
                 '0': (3, 1)
}

def is_valid(num_str):
    for i in range(len(num_str) - 1):
        r1, c1 = coords[num_str[i]]
        r2, c2 = coords[num_str[i + 1]]

        if r2 < r1 or c2 < c1:
            return False
    return True

for k in nums:
    diff = 0
    while True:
        if k - diff >= 0 and is_valid(str(k - diff)):
            print(k - diff)
            break
        if is_valid(str(k + diff)):
            print(k + diff)
            break
        diff += 1