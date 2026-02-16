n = int(input())

if n == 0 or n == 1:
    print(1)

if n == 2:
    print(2)

arr = [1, 1, 2]

for i in range(3, n + 1):
    arr.append(arr[i - 1] + arr[i - 2] + arr[i - 3])

print(arr[n])
