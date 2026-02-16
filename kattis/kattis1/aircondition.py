n = int(input())
if n == 0:
    print(n)
    exit()

intervals = []

for _ in range(n):
    a, b = map(int, input().split())
    intervals.append((a, b))

intervals.sort(key=lambda x: x[1])

rooms = 0
last_room_temp = 0

for start, end in intervals:
    if start > last_room_temp or last_room_temp == 0:
        rooms += 1
        last_room_temp = end

print(rooms)
