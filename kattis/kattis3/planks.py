n = int(input())

if n == 0 or n == 1:
    print(1)

if n == 2:
    print(2)

a, b, c = 1, 1, 2

for _ in range(3, n + 1):
    next = a + b + c
    a, b, c = b, c, next

print(c)
