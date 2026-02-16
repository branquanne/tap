n = int(input())

if n == 0:
    print(1)

if n == 1:
    print(1)

if n == 2:
    print(2)

way1, way2, way3 = 1, 1, 2

for _ in range(3, n + 1):
    next_way = way1 + way2 + way3
    way1, way2, way3 = way2, way3, next_way

print(way3)
