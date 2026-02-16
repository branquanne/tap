import re

in_string = input()

n = int(input())

arr = []
for _ in range(n):
    arr.append(input())

in_string_temp = in_string.replace(".", r"\.")
in_string = in_string_temp.replace("*", ".*")

regex = r"^" + in_string + r"$"
pattern = re.compile(regex)

for i in range(0, n):
    if pattern.fullmatch(arr[i]):
        print(arr[i])
